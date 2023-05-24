import os
import streamlit as st
from langchain.llms import AzureOpenAI
from langchain.utilities import OpenWeatherMapAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


st.title('📣 PuheGPT')
st.subheader('Kirjoita puhe aiheesta...')

prompt = st.text_input('Aihe')

chat = AzureChatOpenAI(
    openai_api_version="2023-03-15-preview",
    deployment_name="chat",
)

template="Olet eduskunnan puhekirjoittaja. Kirjoita noin kolmen minuutin puhe aiheesta: {aihe}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

if prompt:
    with st.spinner("Botti kirjoittaa puheen..."):
        response = chat(chat_prompt.format_prompt(aihe=prompt, text=prompt).to_messages())
    st.success("Tekoälyn luonnos:")
    st.write(response.content)
