from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from github import GitHub
from agent import Agent

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")
FLASK_ENV = os.getenv("FLASK_ENV")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

agent = Agent(api_key=OPENAI_API_KEY, model_version=LLM_MODEL)
github = GitHub(token=GITHUB_TOKEN)

app = Flask(__name__)

CORS(app, resources={
     r"/*": {"origins": FLASK_ENV, "methods": ["POST", "OPTIONS"]}})


@app.route('/api/better-conduct', methods=['POST'])
def better_conduct():
    try:
        repo_url = request.get_json().get('repo_url')
        if not repo_url:
            return jsonify({"error": "Repository URL data not found"}), 400

        code_of_conduct = github.get_code_of_conduct(repo_url)
        agent_response = agent.main(code_of_conduct)
        return jsonify(
            {
                "feedback": agent_response["feedback"],
                "better_conduct": agent_response["better_conduct"]
            }
        ), 200

    except Exception as e:
        logger.error(e)
        return jsonify({"exception": str(e)}), 400


@app.route('/api/peer-connect', methods=['POST'])
def peer_connect():
    try:
        repo_url = request.get_json().get('repo_url')
        if not repo_url:
            return jsonify({"error": "Repository URL data not found"}), 400

        contributors = github.get_contributors(repo_url)
        return jsonify(
            {
                "contributors": contributors
            }
        ), 200

    except Exception as e:
        logger.error(e)
        return jsonify({"exception": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
