from mcp.server.fastmcp import FastMCP

mcp = FastMcp("Math")

@mcp.tool()
def add(a:int,b:int)->  int:
    """
        __Summarry__
    Add two numbers
    """
    return a+b  

@mcp.tool()
def multiply(a:int,b:int)->int:
    """
    Multiply two numbers
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport = "stdios") 