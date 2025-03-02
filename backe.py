import os
from langchain_aws import ChatBedrock  # ✅ Correct import
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def chat_chatbot():
    demo_llm = ChatBedrock(  # ✅ Use ChatBedrock here
        credentials_profile_name='yourprofile',
        model_id='meta.llama3-70b-instruct-v1:0',  # Ensure the model is accessible in AWS Bedrock
        model_kwargs={
            "temperature": 0.5,
            "top_p": 0.9,
            "max_gen_len": 460  # ✅ Correct parameter for Llama 3
        }
    )
    return demo_llm

#response = chat_chatbot('Hello, what is your name?')
#print(response.content)  # ✅ Extracts only the text response
#nextstep
def chat_memory():
    llm_data=chat_chatbot()
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit=460)
    return memory
#nextstep
def demo_talk(input_text, memory):
    llm_chain_data = chat_chatbot()
    llm_talk = ConversationChain(llm = llm_chain_data, memory = memory, verbose= True)
#nextstep
    chat_reply = llm_talk.predict(input = input_text)
    return chat_reply 