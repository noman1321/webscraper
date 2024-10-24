import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime  # Import datetime for timestamps

# Load environment variables (if using .env file for MongoDB credentials)
load_dotenv()

# MongoDB connection settings (replace with your own MongoDB URI and database/collection names)
MONGO_URI = os.getenv('MONGO_URI') or "mongodb://localhost:27017"
DATABASE_NAME = os.getenv('MONGO_DB_NAME') or "web_scraping_db"
COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME') or "scraped_data"

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['noman']
collection = db['ansari']

def store_in_mongodb(parsed_data, metadata=None):
    """
    Store parsed data in MongoDB as a document.
    
    Args:
    - parsed_data (str): The cleaned and parsed content to store.
    - metadata (dict, optional): Additional metadata about the document (e.g., source URL).
    
    Returns:
    - result (InsertOneResult): The result of the insert operation.
    """
    document = {
        "parsed_content": parsed_data,
        "metadata": metadata or {},
        "created_at": datetime.now()  # Add a timestamp
    }
    
    # Insert the document into MongoDB
    result = collection.insert_one(document)
    
    return result
