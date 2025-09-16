from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatOpenAI()

praser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Write a detailed report about {topic}.", input_variables=["topic"]    
)

prompt2 = PromptTemplate(
    template = "Summarize the following report in a concise manner: {text}", input_variables=[""]
)

report_gen_chain = prompt1 | model | praser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, prompt2 | model | praser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

response = final_chain.invoke({"topic": "The impact of AI on modern society"})

print(response)