# crew_logic.py
import os
from crewai import Crew, Process
from langchain_mistralai.chat_models import ChatMistralAI
from src.agents import ResearchAgents
from src.tasks import ResearchTasks

def run_crew(topic: str, enabled_tasks: dict, callbacks=None):
    """
    Initializes and runs the CrewAI crew based on the selected tasks.
    """
    # ... (all the agent and task creation logic remains the same) ...
    # ...
    agents = ResearchAgents()
    tasks = ResearchTasks()
    llm = ChatMistralAI(
        model="mistral-small-latest", # Changed from "mistral-large-latest"
        api_key=os.getenv("MISTRAL_API_KEY"),
        timeout=120
    )
    market_analyst = agents.market_analyst()
    social_scout = agents.social_scout()
    content_strategist = agents.content_strategist()
    copywriter = agents.copywriter()
    for agent in [market_analyst, social_scout, content_strategist, copywriter]:
        agent.llm = llm
    active_tasks = []
    if enabled_tasks.get("market_analysis") or enabled_tasks.get("social_media_analysis"):
        market_task = tasks.market_analysis_task(market_analyst, topic)
        social_task = tasks.social_scout_task(social_scout, topic)
        active_tasks.extend([market_task, social_task])
    if enabled_tasks.get("generate_strategy"):
        strategy_task = tasks.strategy_task(content_strategist)
        active_tasks.append(strategy_task)
    if enabled_tasks.get("write_blog_post"):
        writing_task = tasks.writing_task(copywriter)
        active_tasks.append(writing_task)
    if not active_tasks:
        return "Error: Please select at least one task to perform."
    # ...

    # --- THE FIX IS HERE ---

    # Assemble and run the crew with the selected tasks
    crew = Crew(
        agents=[market_analyst, social_scout, content_strategist, copywriter],
        tasks=active_tasks,
        process=Process.sequential,
        verbose=False, 
        # Pass the callbacks to the Crew constructor
        callbacks=callbacks
    )
    
    # The kickoff method no longer needs the callbacks argument
    result = crew.kickoff(inputs={'topic': topic})
    return result