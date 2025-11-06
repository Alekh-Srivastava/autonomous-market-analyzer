# main.py
import os
from dotenv import load_dotenv
from crewai import Crew

# Import the Mistral Chat Model
from langchain_mistralai.chat_models import ChatMistralAI

# Import your custom agent and task classes
from src.agents import ResearchAgents
from src.tasks import ResearchTasks

# Load environment variables
load_dotenv()

# Main execution block
if __name__ == "__main__":
    print("## Starting Diagnostic Test for a Single Agent ##")
    print("---------------------------------")
    
    mistral_api_key = os.getenv("MISTRAL_API_KEY")
    if not mistral_api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env file.")

    topic = input("Please enter the topic you want to research: ")

    # Initialize the Mistral LLM
    llm = ChatMistralAI(
        model="mistral-large-latest",
        api_key=mistral_api_key
    )

    # Initialize your agent and task classes
    agents = ResearchAgents()
    tasks = ResearchTasks()

    # --- DIAGNOSTIC CHANGE 1: Create ONLY ONE AGENT ---
    market_analyst = agents.market_analyst()
    market_analyst.llm = llm

    # --- DIAGNOSTIC CHANGE 2: Create ONLY ONE TASK and set it to run SEQUENTIALLY ---
    # We are modifying the original task definition for this test.
    market_task = tasks.market_analysis_task(market_analyst, topic)
    market_task.async_execution = False # Force it to run in the foreground

    # --- DIAGNOSTIC CHANGE 3: Assemble a crew with only ONE agent and ONE task ---
    crew = Crew(
        agents=[market_analyst],
        tasks=[market_task],
        verbose=True,
    )

    # Kick off the simplified workflow
    print("\n--- Running simplified crew... ---\n")
    result = crew.kickoff()

    # Print the final results
    print("\n\n################################")
    print("## Diagnostic Test Complete! ##")
    print("################################")
    print("Final results:")
    print(result)