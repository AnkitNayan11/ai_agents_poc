# ai_review_agent.py

from phi.knowledge.text import TextKnowledgeBase
from phi.vectordb.pgvector import PgVector
from phi.agent import Agent

# Step 1: Define the knowledge base from your .txt file 
knowledge_base = TextKnowledgeBase(
    path="/Users/ankitnayan/Downloads/ai_agent/webscraper_result",  # Folder containing merged_reviews.txt
    vector_db=PgVector(
        table_name="text_documents",  # Table in your pgvector-backed PostgreSQL DB
        #db_url="postgresql+psycopg://ai:ai@localhost:5532/ai", 
        db_url = "postgresql+psycopg2://ai:ai@localhost:5532/ai"

    ),
)

#  Step 2: Load the knowledge base (Only once unless content changes) 
knowledge_base.load(recreate=False)
print(" Knowledge base loaded.")


#  Step 3: Create the RAG Agent 
agent = Agent(
    knowledge_base=knowledge_base,
    search_knowledge=True,
)

# === Step 4: Ask your question ===

# Sentiment & Opinion-Based
agent.print_response("What are the top complaints in the reviews?", stream=True) #used
# agent.print_response("What do users love the most about the product?", stream=True)
# agent.print_response("Are users generally satisfied with their purchase?", stream=True)
# agent.print_response("How is the overall customer sentiment in the reviews for apple products?", stream=True) #used

# Feature-Specific Feedback

# agent.print_response("What do customers say about the battery life?", stream=True)
# agent.print_response("How is the screen or display quality described in the reviews?", stream=True)
# agent.print_response("Are there any complaints about the performance or speed?", stream=True)
# agent.print_response("What feedback is there on the keyboard and trackpad?", stream=True)

# # General Summary & Insights
# agent.print_response("Summarize the overall feedback in 3 lines.", stream=True)
# agent.print_response("List the top 3 pros and top 3 cons from the reviews.", stream=True)
#agent.print_response("Based on the reviews, what should be improved in the next version?", stream=True) #used









# pip install pgvector

