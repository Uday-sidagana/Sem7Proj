from crewai import Crew,Process
from tasks import research_task,write_task
from agents import researcher,writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[researcher,writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)