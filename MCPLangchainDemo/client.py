import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["math_server.py"],
                "transport":"stdio"
            },
            "weather":{
                "url":"http://localhost:8000/mcp",
                "transport":"streamable-http"
            }
        }
    )
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(
        model_name="llama3-8b-8192",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.0,
        max_tokens=8192
    )
    agent = create_react_agent(
        model,tools
    )

    math_result = await agent.invoke({"messages":[{"role":"user","content":"What is 2+2?"}]})

    print("math_result",math_result["messages"][-1].content)

asyncio.run(main())