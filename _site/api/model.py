import openai


class Model:
    def __init__(self, api_key, llm_model):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.llm_model = llm_model

    def request_to_api(self, messages):
        try:
            response = openai.chat.completions.create(
                model=self.llm_model,
                messages=messages
            )
            return response
        except Exception as e:
            log_json = {"function": "model.request_to_api",
                        "messages": messages, "error": str(e)}
            raise Exception(log_json)

    def request(self, messages):
        try:
            response = self.request_to_api(messages=messages)
            if response:
                message = response.choices[0].message

                content = message.content if hasattr(
                    message, "content") else message["content"]
                return content
            else:
                raise Exception("No response from external API")
        except Exception as e:
            if "function" in e:
                raise Exception(e)
            log_json = {"function": "model.request",
                        "messages": messages, "error": str(e)}
            raise Exception(log_json)
