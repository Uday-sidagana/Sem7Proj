from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from litellm import completion
import litellm

import os

# Initialize the LLM
llm = (
    litellm.set_verbose=True,
    model="gemini-1.5-pro",
    verbose=True,
    temperature=1.0,
    
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="Explore groundbreaking advancements in personalized learning systems, uncovering insights on adaptive learning, engagement strategies, and AI-driven educational tools.",
    verbose=True,
    memory=True,
    backstory=(
        "Fueled by a drive to advance education, you're focused on discovering "
        "innovations that personalize and improve learning experiences for all."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# writer agent 
writer = Agent(
    role="Writer",
    goal="Craft comprehensive, engaging materials on personalized learning systems, focusing on adaptive technology and user-specific learning strategies.",
    verbose=True,
    memory=True,
    backstory=(
        "You bring clarity to educational innovations, writing accessible and "
        "engaging content that highlights the potential of personalized learning "
        "to transform education."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
