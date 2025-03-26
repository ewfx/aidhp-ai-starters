import pinecone
from config.settings import PINECONE_API_KEY, PINECONE_INDEX

# Initialize Pinecone client
pinecone.init(api_key=PINECONE_API_KEY)
index = pinecone.Index(PINECONE_INDEX)

def retrieve_relevant_context(query):
    # Search the vector store for relevant context based on the user's query
    try:
        response = index.query(queries=[query], top_k=5)
        context = [match['metadata']['text'] for match in response['matches']]
        return " ".join(context)
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return ""
