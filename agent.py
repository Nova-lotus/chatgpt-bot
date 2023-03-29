from langchain.memory import ConversationSummaryBufferMemory
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, load_tools
from langchain import SerpAPIWrapper
from dotenv import load_dotenv
import os
load_dotenv()


llm=ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10, memory_key="chat_history", return_messages=True)
memory.chat_memory.add_ai_message("System: You are Descartes, a philosophical AI Language model made by NovaLabs, Developed by  ☙𝕷𝖔𝖙𝖚𝖘❧#9931 in discord, and powered by OpenAI, you talk in Posh English, like a High Noblemen in English times, and view others as insignificant but yet open your services to them")



llm1 = OpenAI(temperature=0.5, model="text-curie-001")
tools = load_tools(['serpapi','llm-math', 'wikipedia', 'requests', 'wolfram-alpha'], llm=llm1)


agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)
