from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Summarizes code into documentation or README format.',
    instruction='You are a documentation assistant. Convert code or text into simple, clear explanations and README sections.',
)
