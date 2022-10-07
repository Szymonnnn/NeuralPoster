import openai


class Ask:
    def __init__(self) -> None:
        pass

    def ask(self, text, tokens, temperature):
        Secret_Key = "" #Deleted for github
        openai.api_key = Secret_Key
        prompt = text
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=tokens, temperature=temperature)
        return response.choices[0]['text']