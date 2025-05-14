import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from definitions import definitions
from model import Model


class Agent:
    def __init__(self, api_key, model_version):
        self.model = Model(api_key, model_version)
        self.definitions = definitions()

    def generate(self, code_conduct, definitions):
        messages = [
            {"role": "system", "content": definitions["system_role"]},
            {"role": "user", "content": definitions["user_role"].replace(
                "__coc__", code_conduct)}
        ]

        try:
            return self.model.request(messages)
        except Exception as e:
            if "function" in e:
                raise Exception(e)

            log_json = {"function": "agent.generate",
                        "code_conduct": code_conduct, "error": str(e)}
            raise Exception(log_json)

    def main(self, user_input):
        try:

            agent_response_feedback = self.generate(
                user_input, self.definitions["feedback"])
            better_conduct_definitions = self.definitions["better_conduct"]
            better_conduct_definitions["user_role"] = better_conduct_definitions["user_role"].replace(
                "__feedback__", agent_response_feedback)

            agent_response_conduct = self.generate(
                user_input, better_conduct_definitions)

            return {
                "feedback": agent_response_feedback,
                "better_conduct": agent_response_conduct
            }
        except Exception as e:
            raise Exception(e)
