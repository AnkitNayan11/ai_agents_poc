from phi.agent import Agent
from phi.tools.crawl4ai_tools import Crawl4aiTools

agent = Agent(tools=[Crawl4aiTools(max_length=None)], show_tool_calls=True)

# agent.print_response("Tell me about https://github.com/agno-agi/phidata.")

# agent.print_response("Extract Full Year GDP Growth by Country data from https://tradingeconomics.com/country-list/full-year-gdp-growth")

# agent.print_response("Extract the maximum number of attachments supported by Nitro instances from https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html")

# agent.print_response("Extract all MacBook names and their prices from https://www.flipkart.com/search?q=apple+macbook+m1&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_13_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_13_na_na_na&as-pos=5&as-type=RECENT&suggestionId=apple+macbook+m1&requestId=b48c3291-3410-4dad-8d7e-4e99beca541d&as-searchtext=apple%20macbook%20m1")

