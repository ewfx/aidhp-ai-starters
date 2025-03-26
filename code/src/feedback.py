from pymongo import MongoClient
from config.settings import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def save_feedback(user_id, recommendation_id, feedback):
    # Save user feedback for a particular recommendation
    feedback_data = {
        "user_id": user_id,
        "recommendation_id": recommendation_id,
        "feedback": feedback
    }
    try:
        db.feedback.insert_one(feedback_data)
        print("Feedback saved successfully!")
    except Exception as e:
        print(f"Error saving feedback: {e}")
