from langchain_community.tools import TavilySearchResults  # type: ignore
from langgraph.prebuilt.tool_node import ToolNode # type: ignore

def get_tools():
    """
    Returns the list of tools to be used in the chatbot.
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Creates a ToolNode for the chatbot.
    """
    return ToolNode(tools=tools)  # Use 'tool' instead of 'tools'
