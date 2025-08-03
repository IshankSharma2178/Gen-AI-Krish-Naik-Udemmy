# MCP DuckDuckGo Client

A Python client for the DuckDuckGo MCP (Model Context Protocol) server hosted on Smithery.ai.

## Features

- Search DuckDuckGo using MCP protocol
- Secure API key handling via environment variables
- Comprehensive error handling
- Easy-to-use async interface
- Command line and web interface options

## Setup

### 1. Install Dependencies

You have two options:

**Option A: Use the helper script**

```bash
python install_dependencies.py
```

**Option B: Manual installation**

```bash
pip install mcp langchain-mcp-adapters streamlit
```

### 2. Configure API Key

For security, set your Smithery API key as an environment variable:

**Windows:**

```cmd
set SMITHERY_API_KEY=your_api_key_here
```

**Linux/Mac:**

```bash
export SMITHERY_API_KEY=your_api_key_here
```

**Note:** If no environment variable is set, the script will use a default API key (not recommended for production).

## Usage

### Command Line Interface

Run the DuckDuckGo search client:

```bash
python duckduckgo_search.py
```

The script will:

1. Connect to the Smithery MCP server
2. List available tools
3. Execute a search for "latest OpenAI news"
4. Display the results in a clean format

### Web Interface (Streamlit)

For a web-based interface, run:

```bash
streamlit run duckduckgo_simple.py
```

This will open a web browser with a user-friendly interface for searching.

## Customization

### Command Line Version

To modify the search query, edit the `search_query` variable in `duckduckgo_search.py`:

```python
search_query = "your search query here"
```

### Web Interface

The web interface allows you to:

- Enter custom search queries
- Adjust the number of results (1-20)
- Use quick search buttons
- View results in a scrollable text area

## Error Handling

The script includes comprehensive error handling for:

- Missing dependencies
- Network connectivity issues
- Invalid API keys
- Server errors

## Files

- `duckduckgo_search.py` - ✅ **Working command line DuckDuckGo MCP client**
- `duckduckgo_simple.py` - ✅ **Working web interface using Streamlit**
- `duckduckgo_streamlit.py` - ⚠️ **Advanced version with retry logic**
- `duckduckgo_robust.py` - ⚠️ **Complex version with connection management**
- `install_dependencies.py` - ✅ **Helper script for dependency installation**
- `requirements.txt` - ✅ **Python dependencies list**

## Troubleshooting

1. **ImportError: No module named 'mcp'**

   - Run `python install_dependencies.py` or `pip install mcp`

2. **API key errors**

   - Verify your Smithery API key is correct
   - Set the `SMITHERY_API_KEY` environment variable

3. **Network errors**

   - Check your internet connection
   - Verify the Smithery server is accessible

4. **Streamlit errors**

   - Install Streamlit: `pip install streamlit`
   - Run with: `streamlit run duckduckgo_simple.py`

5. **Connection issues in Streamlit**
   - Use `duckduckgo_simple.py` for reliable web interface
   - The simple version handles async/await properly

## Example Output

```
🚀 DuckDuckGo MCP Search Client
----------------------------------------
🔍 Searching for: 'latest OpenAI news'

🔍 Search Results for: 'latest OpenAI news'
================================================================================
Found 10 search results:

1. News - OpenAI
   URL: https://openai.com/news/
   Summary: Stay up to speed on the rapid advancement of AI technology...

2. OpenAI News | Today's Latest Stories | Reuters
   URL: https://www.reuters.com/technology/openai/
   Summary: OpenAI chief executive Sam Altman had a call with Microsoft CEO...
================================================================================
```

## License

This project is for educational purposes. Please respect the terms of service for both DuckDuckGo and Smithery.ai.
