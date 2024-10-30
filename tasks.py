from crewai import Task
from tools import tool
from agents import researcher, writer

# Research 
research_task = Task(
  description=(
    "Investigate the latest advancements in personalized learning systems, "
    "highlighting key technologies, pros and cons, and overarching trends in adaptive learning. "
    "Provide a thorough assessment of its market potential, scalability, and risks."
  ),
  expected_output="A detailed 3-paragraph report on the latest trends in personalized learning technology.",
  tools=[tool],
  agent=researcher,
)

# Writing task on personalized learning systems w
write_task = Task(
  description=(
    "Create an engaging and informative article on the current state of personalized learning systems. "
    "Include recent trends, examples of technology adoption, and the positive impact on learners' engagement and outcomes. "
    "The article should be accessible, easy to read, and optimistic."
  ),
  expected_output="A 4-paragraph article on advancements in personalized learning systems, formatted as markdown.",
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file="new-blog-post.md"  
)
