from openai import OpenAI


class Client:
    def __init__(self):
        self.client = self.connect_client()
        self.current_response = 0


    def connect_client(self):
         client =  OpenAI(base_url="http://localhost:8080/v1", api_key = "sk-no-key-required")
         client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
            {"role": "system",
            "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
            ])
         return client
    

    def submit_prompt(self, prompt):
        response = self.client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": prompt,}],
                model="gpt-4o-mini",)
        self.set_response(response)


    def set_response(self, response):
        self.response = response

    def get_response(self):
        return self.response




