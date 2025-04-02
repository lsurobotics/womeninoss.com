import os
import sys
import requests
import threading

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from genderComputer import GenderComputer

class GitHub:

    def __init__(self, token):
        self.headers = {"Accept": "application/vnd.github+json"}
        if token:
            self.headers["Authorization"] = f"token {token}"
        self.gc = GenderComputer()

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1,
                        status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('https://', adapter)
        self.timeout = 10

    def get_code_of_conduct(self, repo_url):
        try:
            owner, repo = repo_url.rstrip('/').split("/")[-2:]
            if not owner or not repo:
                raise Exception("Invalid Url")
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/CODE_OF_CONDUCT.md"
            response = self.session.get(
                url, headers=self.headers, timeout=self.timeout)
            if response.status_code == 200:
                return response.text
            else:
                raise Exception("CODE_OF_CONDUCT.md not found")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error in getting code of conduct: {str(e)}")

    def get_gender(self, first_name, location):
        try:
            return self.gc.resolveGender(first_name, location)
        except Exception:
            return "Unknown"

    def get_user_details(self, username):
        url = f"https://api.github.com/users/{username}"
        try:
            response = self.session.get(
                url, headers=self.headers, timeout=self.timeout)
            if response.status_code == 200:
                user_data = response.json()
                first_name = user_data["name"].split()[0] if user_data.get(
                    "name", "Unknown") else "Unknown"
                location = user_data.get("location", "Unknown")
                avatar_url = user_data.get("avatar_url", "")
                html_url = user_data.get("html_url", "Unknown")
                gender = self.get_gender(first_name, location)
                if gender == "female":
                    return {"url": html_url, "avatar_url": avatar_url, "username": username, "first_name": first_name, "location": location, "gender": gender}
            else:
                gender = self.get_gender(username, "Unknown")
                if gender == "female":
                    return {"url": f"https://github.com/{username}", "avatar_url": "", "username": username, "first_name": username, "location": "Unknown", "gender": gender}
            return None
        except requests.exceptions.Timeout:
            print(f"Request to {username} timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def fetch_contributors(self, owner, repo, page):
        url = f"https://api.github.com/repos/{owner}/{repo}/contributors?per_page=1000&page={page}"
        try:
            response = self.session.get(
                url, headers=self.headers, timeout=self.timeout)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"GitHub API error: {response.status_code}")
        except requests.exceptions.Timeout:
            print(
                f"Timeout while fetching contributors from page {page}. Retrying...")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request error while fetching contributors: {e}")
            return None

    def get_contributors(self, repo_url):
        try:
            owner, repo = repo_url.rstrip('/').split("/")[-2:]
            if not owner or not repo:
                raise Exception("Invalid URL")

            user_list = []
            page = 1
            threads = []
            lock = threading.Lock()

            def process_contributor(contributor):
                user_gender = self.get_user_details(contributor["login"])
                if user_gender:
                    with lock: 
                        user_list.append(user_gender)

            while True:
                contributors = self.fetch_contributors(owner, repo, page)
                if not contributors:
                    break

                for c in contributors:
                    thread = threading.Thread(
                        target=process_contributor, args=(c,))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

                page += 1

            return user_list
        except Exception as e:
            raise e
