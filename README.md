🚀 Autonomous Market Intelligence & Content Agent
This project is an autonomous multi-agent system built with CrewAI, LangChain, and Mistral AI. It deploys a team of specialized AI agents to perform end-to-end market research, audience sentiment analysis, and full content creation based on a single topic.

The system is delivered through an interactive Streamlit dashboard where a user can input a topic, and the AI agents will research, analyze, and write a complete article, presenting the final content alongside data visualizations like sentiment charts and word clouds.

🌟 Core Features
Autonomous Multi-Agent System: Utilizes a 4-agent system (Market Analyst, Social Scout, Content Strategist, Copywriter) built with CrewAI to automate the complex workflow from raw idea to published article.

Custom Machine Learning Tools: The "Social Scout" agent is empowered with a custom Hugging Face Transformers tool to perform real-time sentiment analysis on social media data it gathers.

Interactive Web Dashboard: A Streamlit frontend provides a user-friendly interface to input topics, select tasks, and view the final results.

Dynamic Data Visualization: Automatically generates and displays data visualizations—including a Plotly pie chart for sentiment and a WordCloud for key topics—directly in the UI.

Sequential Task Orchestration: Uses LangChain and CrewAI's Process.sequential to ensure a robust, step-by-step workflow where the output of one agent becomes the input for the next.

🛠️ Tech Stack
Agentic AI: CrewAI, LangChain

LLM: Mistral AI (via API)

Web Framework: Streamlit

ML/NLP: Hugging Face Transformers, PyTorch, Tokenizers

Data Visualization: Plotly, WordCloud, Matplotlib

Core Tools: Python, Serper API
