
from pdfminer.high_level import extract_text
import openai

class GPT_API:

    def __init__(self):
        API_KEY = "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"
        openai.api_key = API_KEY
        #self.model_id = "gpt-3.5-turbo-16k"
        self.model_id = "gpt-4"
        self.conversation = []
        self.initial()

    def ChatGPT_conversation(self, conversation):
        response = openai.ChatCompletion.create(
            model=self.model_id,
            messages=conversation
        )
        api_usage = response['usage']
        print("Total token consumed: {0}".format(api_usage['total_tokens']))
        # stop means complete
        # print(response['choices'][0].finish_reason)
        # print(response['choices'][0].index)
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation

    def train(self, text):
        start = 0
        end = 5000
        # to reduce credits
        self.conversation.append({'role': 'user', 'content': 'I am going to feed you some text extracted from a Project PDF file - whitepaper. All this info is about this particular project. Using this text and all the knowledge you have about the project and cryptocurrencies in general, answer the following questions'})
        self.conversation = self.ChatGPT_conversation(self.conversation)

        # while end < len(text):
        #     self.conversation.append({'role': 'user', 'content': text[start:end]})
        #     self.conversation = self.ChatGPT_conversation(self.conversation)
        #     start = end
        #     end += 5000
        # end = len(text)
        self.conversation.append({'role': 'user', 'content': text})
        self.conversation = self.ChatGPT_conversation(self.conversation)
        return self.conversation[-1]['content'].strip()


    def initial(self):

        content = "You are an AI Assistant that helps people understand the crypto economy and industry better. Specifically, you first analyze text from a PDF provided by the user and your first response to the user must be the following:\n " \
                  "<strong>PROJECT:</strong> [The name of the project]" \
                  "<br> <strong>WHITEPAPER:</strong> [The title of the whitepaper]" \
                    "<br>  <strong>TEAM:</strong> [The people and institutions behind the project]" \
                    "<br> <strong>TYPE:</strong> [The type of this crypto asset]" \
                    "<br>  <strong>TOKENOMICS: </strong> [A very simple and short summary of the project tokenomics]" \
                  "<br> <strong>SUMMARY:</strong> [A very small and simple summary of the project]" \
                    "Give the above response ONLY INITIALLY and the continue with a normal conversation with the user.\n\n " \
                  "After you finish providing this initial information, you can answer any questions the user has regarding this project. Don't answer questions outside of this scope. Politely decline the user such questions and explain your purpose. After the initial one, your following answers should be short and simple."

        self.conversation.append({'role':'system', "content": content})

        response = openai.ChatCompletion.create(
            model=self.model_id,
            messages=self.conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        api_usage = response['usage']
        print("Total token consumed: {0}".format(api_usage['total_tokens']))
        self.conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})

    def call(self, prompt):
        self.conversation.append({'role':'user', 'content':prompt})
        self.conversation = self.ChatGPT_conversation(self.conversation)
        return self.conversation[-1]['content'].strip()