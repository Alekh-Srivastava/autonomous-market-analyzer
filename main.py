# main.py
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_mistralai.chat_models import ChatMistralAI
from src.agents import ResearchAgents
from src.tasks import ResearchTasks
import logging

# Suppress verbose warnings from underlying libraries
logging.basicConfig(level=logging.ERROR)
logging.getLogger('langchain_core.language_models.chat_models').setLevel(logging.ERROR)

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    print("## Welcome to the Full Content Creation Crew ##")
    print("---------------------------------")

    # --- CHECKPOINT: Loading API Keys & User Input ---
    print("\n--- CHECKPOINT: Loading API Keys & User Input ---")
    mistral_api_key = os.getenv("MISTRAL_API_KEY")
    if not mistral_api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env file.")
    topic = input("Please enter the topic you want to research: ")
    print("  - Topic Received.")

    # --- CHECKPOINT: Initializing LLM ---
    print("\n--- CHECKPOINT: Initializing LLM ---")
    llm = ChatMistralAI(
        model="mistral-large-latest",
        api_key=mistral_api_key,
        timeout=120
    )
    print("  - LLM Initialized Successfully.")

    # --- CHECKPOINT: Initializing Agent & Task Classes ---
    print("\n--- CHECKPOINT: Initializing Agent & Task Classes ---")
    agents = ResearchAgents()
    tasks = ResearchTasks()
    print("  - Agent and Task classes Initialized.")

    # --- CHECKPOINT: Creating Agents ---
    print("\n--- CHECKPOINT: Creating Agents ---")
    market_analyst = agents.market_analyst()
    social_scout = agents.social_scout()
    content_strategist = agents.content_strategist()
    copywriter = agents.copywriter()
    print("  - All four agents created.")

    # --- CHECKPOINT: Assigning LLM to Agents ---
    print("\n--- CHECKPOINT: Assigning LLM to all Agents ---")
    market_analyst.llm = llm
    social_scout.llm = llm
    content_strategist.llm = llm
    copywriter.llm = llm
    print("  - LLM assigned successfully.")

    # --- CHECKPOINT: Creating Tasks ---
    print("\n--- CHECKPOINT: Creating Tasks ---")
    market_task = tasks.market_analysis_task(market_analyst, topic)
    social_task = tasks.social_scout_task(social_scout, topic)
    strategy_task = tasks.strategy_task(content_strategist)
    writing_task = tasks.writing_task(copywriter)
    print("  - All four tasks created.")
    
    # --- CHECKPOINT: Assembling the Crew ---
    print("\n--- CHECKPOINT: Assembling the Crew ---")
    crew = Crew(
        agents=[market_analyst, social_scout, content_strategist, copywriter],
        tasks=[market_task, social_task, strategy_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )
    print("  - Crew assembled successfully.")

    # --- CHECKPOINT: Kicking off the Crew Execution ---
    print("\n\n--- CHECKPOINT: Starting Crew Execution ---")
    print("   (The detailed logs that follow are from CrewAI's verbose mode)")
    result = crew.kickoff()

    # --- CHECKPOINT: Final Output ---
    print("\n\n################################")
    print("## Content Creation Complete! ##")
    print("################################")
    print("Final blog post:")
    print(result)