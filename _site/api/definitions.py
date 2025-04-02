LLM = {"feedback": {"system_role": "", "user_role": ""},
       "better_conduct": {"system_role": "", "user_role": ""}}


LLM["feedback"]["system_role"] = """
    You are an AI assistant helping a user review a code of conduct repository to ensure it is inclusive and fosters a welcoming environment for women. The goal is to provide feedback to eliminate any guidelines that promote sexist behavior while fostering a culture of inclusion. Focus on suggesting clear and actionable improvements related to policies, reporting mechanisms, and awareness training.
"""

LLM["feedback"]["user_role"] = """
    Provide feedback on the code of conduct in my repository. I am particularly interested in ensuring that the document promotes a welcoming environment for women, discourages sexist behavior, and encourages accountability.

    Code of conduct:

    ```__coc__```

    The code of conduct should be effective, however, as it does not tolerate sexist behavior. It can help create a more welcoming environment and attract individuals with similar moral values to your project.

    - Enforce clear policies that explicitly prohibit discrimination and harassment.
    - Ensure accountability by having a reporting mechanism in place.
    - Actively promote a culture of inclusion through training and awareness.

    - Output:
        Your response should be a simple text in markdawn and should contain:
        a short paragraph giving a general overview of the code of conduct
        a list of suggested improvements
        this list should only contain the topics of the items

    - Example Output:
        ```Your Code of Conduct is well-structured, clear, and comprehensive. However, if your goal is to specifically highlight support for women, you could enhance it by explicitly mentioning gender inclusivity, ensuring a safe space for women, and committing to proactive support. Here are some key improvements:

        #### Suggested Improvements
        1. **Explicit Support for Women**
        2. **Clearer Examples of Inclusive Behavior**
        3. **Strengthening Enforcement for Gender-Based Harassment**```

    Important: Do not use '```markdown' at the beginning and end of the text.        
"""

LLM["better_conduct"]["system_role"] = """
    You are an AI assistant helping a user improve a code of conduct repository to ensure it is inclusive and fosters a welcoming environment for women. The goal is to improve the code of conduct based on suggested improvements.
"""


LLM["better_conduct"]["user_role"] = """
    Please provide a new code of conduct with suggestions for improvements to ensure the document promotes a welcoming environment for women, discourages sexist behavior, and encourages accountability.

    Old Code of Conduct:

    ```__coc__```

    Improvements:
    ```__feedback__```

    - Result:

    Your response should be in plain text in markdawn containing the revised and improved content.

    Important: Do not use '```markdown' at the beginning and end of the text.
"""


def definitions():
    return LLM
