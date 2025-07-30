from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

# finance_agent = Agent(
#     name="Finance Agent",
#     model=OpenAIChat(id="gpt-4o"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
#     instructions=["Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
# )
# finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)

# pip install yfinance
from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
)
agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)
