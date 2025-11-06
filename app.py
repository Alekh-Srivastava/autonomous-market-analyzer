# app.py
import streamlit as st
from dotenv import load_dotenv

# Import our crew logic function and the new callback handler
from crew_logic import run_crew
from src.callbacks import StreamlitCallbackHandler # <-- Import the new handler

# Load environment variables
load_dotenv()

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Content Creation Crew", page_icon="🚀", layout="wide")

# --- App Title ---
st.title("🚀 AI-Powered Content Creation Crew")
st.markdown("This tool uses a team of AI agents to perform research, generate content ideas, and write a full blog post on any topic.")

# --- Sidebar for Inputs ---
with st.sidebar:
    st.header("Crew Configuration")
    topic = st.text_input("Enter the topic you want to research:", placeholder="e.g., 'AI in Healthcare'")
    
    st.subheader("Select Tasks to Perform:")
    task_market_analysis = st.checkbox("Market Trend Analysis", value=True)
    task_social_media = st.checkbox("Social Media Insights", value=True)
    task_generate_strategy = st.checkbox("Generate Content Strategy", value=True)
    task_write_post = st.checkbox("Write Full Blog Post", value=True)

    start_button = st.button("Start Content Creation")

# --- Main Content Area ---
if start_button:
    if not topic:
        st.warning("Please enter a topic before starting.")
    else:
        # Create a dictionary of enabled tasks
        enabled_tasks = {
            "market_analysis": task_market_analysis,
            "social_media_analysis": task_social_media,
            "generate_strategy": task_generate_strategy,
            "write_blog_post": task_write_post
        }
        
        # --- THIS IS THE NEW "GAMIFIED" WORKFLOW DISPLAY ---
        with st.status("🤖 **Agents at work...**", expanded=True) as status:
            # Pass the status container to our callback handler
            streamlit_callback = StreamlitCallbackHandler(status)
            callbacks = [streamlit_callback]
            
            try:
                # Run the crew with the callbacks
                result = run_crew(topic, enabled_tasks, callbacks)
                status.update(label="✅ Crew finished successfully!", state="complete")
                
                # Display the final result
                st.header("Final Result")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                status.update(label="❌ Error", state="error")