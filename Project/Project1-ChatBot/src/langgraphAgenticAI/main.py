import streamlit as st
from src.langgraphAgenticAI.ui.streamlitui.loadUI import LoadStreamlitUI
from src.langgraphAgenticAI.LLMs.groqllm import GroqLLM
from src.langgraphAgenticAI.graph.graph_builder import GraphBuilder
from src.langgraphAgenticAI.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI application using Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM models,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.

    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Please select an LLM and a use case to proceed.")
        return
    
    if st.session_state.get("IsFetchButtonClicked"):
        user_message = st.session_state.get("time_frame")
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("No model selected. Please select a model to proceed.")
                return
            
            # Initialize and set up the graph based on the use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error : No use case selected. Please select a use case to proceed.")
                return
            
            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

                # Reset fetch button state after processing AI News
                if usecase == "AI News":
                    st.session_state.IsFetchButtonClicked = False

            except Exception as e:
                st.error(f"Error setting up graph: {e}")
                return
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return

