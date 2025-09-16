from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}.", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}.", input_variables=["topic"]
)

model = ChatOpenAI()

praser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, praser),
    "linkedin_post": RunnableSequence(prompt2, model, praser),
})

response = parallel_chain.invoke({"topic": "Deep Fake"})

print(response)

