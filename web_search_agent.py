from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

# Imports the Agent class to build AI agents using models and tools.
# Imports OpenAIChat to use OpenAI chat models like GPT-4o within the agent.
# Imports DuckDuckGo tool to enable web search capabilities for the agent.

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Tell me about OpenAI Sora?", stream=True)

# This block initializes an Agent named "Web Agent" with the following settings:

# model=OpenAIChat(id="gpt-4o") ➤ Uses GPT-4o from OpenAI as the language model.
# tools=[DuckDuckGo()] ➤ Adds DuckDuckGo search capability to the agent.
# instructions=["Always include sources"] ➤ Tells the agent to always return sources (useful when using search tools).
# show_tool_calls=True ➤ Makes the agent show when and how it's calling a tool like DuckDuckGo.
# markdown=True ➤ Formats the response using Markdown (e.g., for headings, links, bullet points).

# pip install -U phidata openai duckduckgo-search