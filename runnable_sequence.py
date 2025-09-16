from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}.", input_variables=["topic"]
)

model = ChatOpenAI()

praser = StrOutputParser()

prompt2 = PromptTemplate(
    template= "Explain the following joke in a detailed way: {joke}", input_variables=["joke"]
)

chain = RunnableSequence(prompt1, model, praser, prompt2, model, praser)

response = chain.invoke({"topic": "AI"})

print(response)