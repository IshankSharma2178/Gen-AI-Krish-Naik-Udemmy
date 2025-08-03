from src.langgraphAgenticAI.state.state import State


class BasicChatbotNode:
    """
    A basic chatbot node that interacts with a language model to generate responses.
    """

    def __init__(self, model):
        self.model = model

    def process(self, state:State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """        
        return {"messages": self.model.invoke(state["messages"])}
