# langChain_runnables

## Runnable: 
1. Task Specific
2. Runnable Primitives


## Task Specific:

Definition: These are core LangChain components that have been converted into Runnables so they can be used in pipelines.

Purpose: Perform task-specific operations like LLM calls, prompting, retrieval, etc.

Examples:

  ChatOpenAI

  Runs an LLM model.

  Prompt Template

  Formats prompts dynamically.

  Retriever Retrieves relevant documents



## Runnables Primitives:

Definition: These are fundamental building blocks for structuring execution logic in Al workflows.

Purpose: They help orchestrate execution by defining how different Runnables interact (sequentially, in parallel, conditionally, etc.).

Examples:

  RunnableSequence - Runs steps in order ( operator).

  RunnableParallel - Runs multiple steps simultaneously.

  RunnableMap - Maps the same input across multiple functions.

  RunnableBranch - Implements conditional execution (if-else logic).

  RunnableLambda - Wraps custom Python functions into Runnables.

  RunnablePassthrough - Just forwards input as output (acts as a placeholder).


### 1. RunnableSequence

RunnableSequence is a sequential chain of runnablesin LangChain that executes each step one after another, passing the output of one step as the input to the next.
It is useful when you need to compose multiple runnables togetherin a structured workflow.


### 2. RunnableParallel

RunnableParallelis a runnable primitivethat allows multiple runnables to execute in parallel.
Each runnable receives the same inputand processes it independently, producing a dictionary of outputs.


### 3. RunnablePassthrough

RunnablePassthroughis a special Runnable primitive that simply returns the input as outputwithout modifying it.


### 4. RunnableLambda

RunnableLambdais a runnable primitive that allows you to apply custom Python functionswithin an AI pipeline.
It acts as a middlewarebetween different AI components, enabling preprocessing, transformation, API calls, filtering, and post-processingin a LangChain workflow.


### 5. RunnableBranch

RunnableBranchis a control flow componentin LangChain that allows you to conditionally route input data to different chains or runnablesbased on custom logic.
It functions like an if/elif/elseblock for chains —where you define a set of condition functions, each associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching condition is executed. If no condition matches, a default runnableis used (if provided).







