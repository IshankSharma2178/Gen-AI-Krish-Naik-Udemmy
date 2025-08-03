from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
import os  


class AINewsNode:
    def __init__(self,llm):
        """
        Initialize the AINewsNode with API keys for Tavily and GROQ.
        """
        self.tavily = TavilyClient()
        self.llm = llm
        # this is used to capture various steps in this file so that later can be use for steps shown
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the specified frequency.
        
        Args:
            state (dict): The state dictionary containing 'frequency'.
        
        Returns:
            dict: Updated state with 'news_data' key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'year': 'y'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'year': 366}

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days=days_map[frequency],
            # include_domains=["techcrunch.com", "venturebeat.com/ai", ...]  # Uncomment and add domains if needed
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        return state
    

    def summarize_news(self, state: dict) -> dict:
        """
        Summarize the fetched news using an LLM.
        Returns updated state with a clean markdown summary.
        """

        news_items = self.state['news_data']

        # Limit to top 10–15 articles to avoid overloading the LLM
        news_items = news_items[:15]

        # Clean and format articles string
        articles_str = "\n\n".join([
            f"- Title: {item.get('title', 'No title')}\n"
            f"  Date: {item.get('published_date', '')}\n"
            f"  URL: {item.get('url', '')}\n"
            f"  Content: {item.get('content', '')[:500]}..."  # Truncate to avoid token overflow
            for item in news_items
        ])

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are an AI journalist. Summarize the following AI news articles in clean markdown format.
            Include:
            - **Date** in `YYYY-MM-DD` format (IST timezone)
            - A clear and concise summary of each article
            - The source URL as a clickable link
            Sort entries by latest date first.

            Format each entry like this:
            ### YYYY-MM-DD
            - [Brief summary sentence](URL)"""),
                    ("user", "Here are the news articles:\n\n{articles}")
            ])

        formatted_prompt = prompt_template.format(articles=articles_str)

        response = self.llm.invoke(formatted_prompt)

        state['summary'] = response.content.strip()
        self.state['summary'] = state['summary']
        return self.state

    

    def save_result(self, state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        folder_path = "./AINews"
        
        # Ensure the folder exists
        os.makedirs(folder_path, exist_ok=True)
        
        filename = os.path.join(folder_path, f"{frequency}_summary.md")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        
        self.state['filename'] = filename
        return self.state
