import mcp
import os
import asyncio
import streamlit as st
from mcp.client.streamable_http import streamablehttp_client

# Get API key from environment variable for security
smithery_api_key = os.getenv("SMITHERY_API_KEY", "98d386f1-e6b8-4f98-b28a-e6db085ee5f4")
url = f"https://server.smithery.ai/@nickclyde/duckduckgo-mcp-server/mcp?api_key={smithery_api_key}&profile=free-orangutan-lkkLGK"

def search_duckduckgo_sync(query, max_results=10):
    """Synchronous wrapper for DuckDuckGo search"""
    try:
        # Run the async function in a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(search_duckduckgo_async(query, max_results))
        loop.close()
        return result
    except Exception as e:
        st.error(f"❌ Search error: {str(e)}")
        return None

async def search_duckduckgo_async(query, max_results=10):
    """Search DuckDuckGo using MCP server"""
    try:
        # Connect to the Smithery MCP server
        async with streamablehttp_client(url) as (read_stream, write_stream, _):
            async with mcp.ClientSession(read_stream, write_stream) as session:
                # Initialize the session
                await session.initialize()

                # List tools
                tools_result = await session.list_tools()
                tools = tools_result.tools
                
                if not tools:
                    st.error("❌ No tools available from the MCP server")
                    return None
                    
                # Find the search tool
                search_tool = None
                for tool in tools:
                    if tool.name == "search":
                        search_tool = tool
                        break

                if not search_tool:
                    st.error("❌ Search tool not found")
                    return None

                # Prepare search input
                search_inputs = {"query": query, "max_results": max_results}

                # Run the search
                search_result = await session.call_tool(search_tool.name, search_inputs)
                
                # Extract search results
                if hasattr(search_result, 'content') and search_result.content:
                    if isinstance(search_result.content, list) and len(search_result.content) > 0:
                        return search_result.content[0].text
                    else:
                        return str(search_result.content)
                else:
                    return "No results found"
                        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="DuckDuckGo MCP Search",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("🔍 DuckDuckGo MCP Search Client")
    st.markdown("Search the web using DuckDuckGo through MCP (Model Context Protocol)")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("Settings")
        max_results = st.slider("Max Results", 1, 20, 10)
        
        st.markdown("---")
        st.markdown("**About:**")
        st.markdown("This app uses the DuckDuckGo MCP server hosted on Smithery.ai to perform web searches.")
        
        st.markdown("---")
        st.markdown("**Status:**")
        if st.button("🔄 Test Connection"):
            with st.spinner("Testing connection..."):
                try:
                    results = search_duckduckgo_sync("test", 1)
                    if results:
                        st.success("✅ Connection successful!")
                    else:
                        st.error("❌ Connection failed")
                except Exception as e:
                    st.error(f"❌ Connection error: {str(e)}")
    
    # Main content
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Use session state to maintain search query
        if 'search_query' not in st.session_state:
            st.session_state.search_query = "latest OpenAI news"
        
        search_query = st.text_input(
            "Enter your search query:",
            value=st.session_state.search_query,
            placeholder="What would you like to search for?"
        )
        
        if st.button("🔍 Search", type="primary", use_container_width=True):
            if search_query.strip():
                # Update session state
                st.session_state.search_query = search_query
                
                # Perform search
                with st.spinner(f"🔍 Searching for: '{search_query}'..."):
                    results = search_duckduckgo_sync(search_query, max_results)
                
                if results:
                    st.success("✅ Search completed!")
                    st.text_area(
                        "Search Results:",
                        results,
                        height=400,
                        disabled=True
                    )
                else:
                    st.error("❌ No results found or an error occurred")
            else:
                st.warning("⚠️ Please enter a search query")
    
    with col2:
        st.markdown("### Quick Searches")
        quick_searches = [
            "latest AI news",
            "Python programming",
            "machine learning trends",
            "tech startup news"
        ]
        
        for quick_search in quick_searches:
            if st.button(quick_search, use_container_width=True):
                st.session_state.search_query = quick_search
                st.rerun()

if __name__ == "__main__":
    main() 