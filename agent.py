from google.adk.agents.llm_agent import Agent

# Just define the agent, no input() loop here
root_agent = Agent(
    name="DocumentationAgent",
    model="gemini-2.5-flash",  
    description="Summarizes code into documentation or README format.",
    instruction="You are a documentation assistant. Convert code or text into simple, clear explanations and README sections."
)
