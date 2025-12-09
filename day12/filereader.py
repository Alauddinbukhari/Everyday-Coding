from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool

def read_file(path):
    with open(path, "r") as f:
        return f.read()

file_tool = Tool(
    name="file_reader",
    func=read_file,
    description="Reads text files"
)

llm = OpenAI(openai_api_key="YOUR_API_KEY")

agent = initialize_agent(
    [file_tool],
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

print(agent.run("Read the file 'notes.txt' and summarize it"))
