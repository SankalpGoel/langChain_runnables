from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}.", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke in a detailed way: {joke}", input_variables=["joke"]
)

model = ChatOpenAI()

praser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, praser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, praser)
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

response = chain.invoke({"topic": "AI"})

print(response)