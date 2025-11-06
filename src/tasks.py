# src/tasks.py
from crewai import Task

class ResearchTasks:
    def market_analysis_task(self, agent, topic) -> Task:
        # This task is fine, no changes needed.
        return Task(
            description=f"Analyze the current market for {topic} and identify the top 5 emerging trends.",
            expected_output="A bullet-point list detailing the 5 most significant emerging trends, each with a brief explanation.",
            agent=agent,
            cache=True
        )

    def social_scout_task(self, agent, topic) -> Task:
        # This task is fine, no changes needed.
        return Task(
            description=f"Search online forums and social media to find the main questions and pain points of people interested in {topic}.",
            expected_output="A bullet-point list of the top 5 questions and a separate bullet-point list of the top 5 pain points.",
            agent=agent,
            cache=True
        )

    # --- FIX 1: Simplify the strategy_task ---
    def strategy_task(self, agent) -> Task:
        return Task(
            description=(
                "Based on the provided market trends and audience pain points from the previous tasks, "
                "generate a list of 5 specific blog post ideas. For each idea, provide a "
                "catchy headline and a 1-2 sentence summary of the angle."
            ),
            expected_output="A numbered list of 5 content ideas with headlines and summaries.",
            agent=agent,
            cache=True,
            # The 'context' parameter is removed.
        )

    # --- FIX 2: Simplify the writing_task ---
    def writing_task(self, agent) -> Task:
        return Task(
            description=(
                "Based on the content strategy from the previous task, write a full, comprehensive blog post. "
                "The post should be engaging, well-structured with clear headings, "
                "and should be at least 500 words long. Make sure to use the research findings in the post."
            ),
            expected_output="A complete blog post with a title, introduction, body with headings, and a conclusion.",
            agent=agent,
            cache=True
            # The 'context' parameter is removed.
        )