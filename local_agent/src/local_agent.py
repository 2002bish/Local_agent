from crewai import Agent, Crew, Process, Task, LLM

# Point crewAI to my local llm 
llama_llm = LLM(model="ollama/llama3.1", base_url="http://localhost:11434")
mistral_llm = LLM(model="ollama/mistral", base_url="http://localhost:11434")

# Define Agent
researcher = Agent(
    role='Senior Research Analyst',
    goal='find and outline the key fact and market trend of given topic.',
    backstory='You are the best researcher of this industry with the high level of expertise and knowledge. You have a strong ability to analyze and synthesize information from various sources, and you are skilled at identifying key insights and trends.',
    verbose=True,
    llm=llama_llm
)

# Agent 2
writer = Agent(
    role='Senior Writer',
    goal='write a comprehensive report based on the research findings.',
    backstory='You are an experienced writer with a talent for crafting clear and engaging content. You have a deep understanding of the industry and can effectively communicate complex ideas to a broad audience.',
    verbose=True,
    llm=mistral_llm
)

# Define Task
research_task = Task(
    description="Research and outline key facts and market trends of the given topic.",
    expected_output="A detailed bulleted report of key facts and trends.",
    agent=researcher
)

writing_task = Task(
    description="Write a comprehensive report based on the research findings.",
    expected_output="A well-structured and informative report that presents the research findings in a clear and engaging manner.",
    agent=writer
)

# Local crew
local_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True
)

# Kickoff system
if __name__ == "__main__":
    topic = "Artificial Intelligence in Healthcare"
    print(f"Starting research and report writing on the topic: {topic}")
    result = local_crew.kickoff()
    print("\n\n######################")
    print("##Final Output of the Crew##")
    print("######\n")
    print(result)