from src.llm import generate_response
from src.context_manager import retrieve_relevant_context
from src.feedback import save_feedback

def get_recommendation(user_query):
    # Retrieve relevant context from vector store
    context = retrieve_relevant_context(user_query)
    
    # Generate response using the LLM with the context
    recommendation = generate_response(user_query, context)
    
    # Grade the quality of the recommendation (simple heuristic for now)
    quality = grade_recommendation(recommendation)
    
    if quality < 0.7:
        # Handle low quality by generating a new recommendation
        recommendation = retry_recommendation(user_query, context)
    
    return recommendation

def grade_recommendation(recommendation):
    # Simple grading logic (e.g., based on length or certain keywords)
    if len(recommendation.split()) > 30:
        return 0.8
    return 0.5

def retry_recommendation(user_query, context):
    print("Retrying with updated context...")
    return generate_response(user_query, context)
