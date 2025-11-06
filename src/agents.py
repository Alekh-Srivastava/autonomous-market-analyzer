# src/agents.py
from crewai import Agent
from crewai_tools import SerperDevTool

# --- REMOVE THE LINE "from main import llm" ---
# This line was causing the circular import and should be deleted.

class ResearchAgents:
    def __init__(self):
        self.search_tool = SerperDevTool(timeout=30)

    def market_analyst(self) -> Agent:
        return Agent(
            role='Market Trend Analyst',
            goal='Find and report on the top 5 emerging trends in the {topic} industry.',
            backstory=(
                'You are a sharp-eyed market analyst with a keen sense of what\'s next. '
                'Your job is to scour the web for data-driven insights and identify '
                'the most significant emerging trends that could shape the future of an industry.'
            ),
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False
        )

    def social_scout(self) -> Agent:
        return Agent(
            role='Audience Insights Specialist',
            goal='Uncover the primary pain points, desires, and frequently asked questions of the target audience for {topic}.',
            backstory=(
                'You are an expert in social listening and audience psychology. You can dive '
                'into online forums and social media to find out what people are truly '
                'struggling with and curious about regarding a specific topic.'
            ),
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False
        )

    def content_strategist(self) -> Agent:
        return Agent(
            role='Content Strategist',
            goal='Generate a list of 5 engaging and SEO-friendly blog post ideas based on a research report.',
            backstory=(
                'You are a master content strategist, known for your ability to turn '
                'dry research into viral content ideas. You excel at identifying the most '
                'compelling angles and crafting clickable headlines.'
            ),
            tools=[],
            verbose=True,
            allow_delegation=False
        )

    def copywriter(self) -> Agent:
        return Agent(
            role='Expert Tech and Economics Copywriter',
            goal='Write a compelling and informative blog post based on a given content idea.',
            backstory=(
                'You are a professional copywriter with a talent for making complex topics like economics '
                'and technology accessible and engaging. You write in a clear, concise, and authoritative tone.'
            ),
            tools=[],
            verbose=True,
            allow_delegation=False
        )