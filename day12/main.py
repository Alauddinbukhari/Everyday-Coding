from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

# 1. Load your LLM
llm = OpenAI(openai_api_key="YOUR_API_KEY", temperature=0)

# 2. Load tools
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# 3. Create an agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 4. Ask something
response = agent.run("Who is Elon Musk's mother and what is 123 * 45?")
print(response)
