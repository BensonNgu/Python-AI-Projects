from langchain_core.messages import HumanMessage         
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()

MEMORY = {}

@tool
def remember(key: str, value: str) -> str:
    """Save a piece of information under a key."""
    MEMORY[key] = value
    return f"I'll remember that {key} is {value}."

@tool 
def recall(key: str) -> str:
    """Recall a saved pieced of information"""
    return MEMORY.get(key, " I don't remember that.")
    

def main():
    model = ChatOpenAI(temperature=0)   # higher temperature, more randomness 

    tools = [remember, recall] 

    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistance. Type 'quit' to exit.")
    print('You can ask me to perform calculations or chat with me.')

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")
        
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()


if __name__ == '__main__':
    main()
