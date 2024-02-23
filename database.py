from model import test
from bson import ObjectId
import os
from dotenv import load_dotenv

# asynchronous mongodb driver
import motor.motor_asyncio
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
database = client.test
collection = database.keepNote


# Fetch By Title
async def fetch_one_note(title):
    document = await collection.find_one({"title" : title})
    return document


# Fetch All Notes
async def fetch_all_notes():
    notes = []
    async for document in collection.find({}):
        document['_id'] = str(document.get('_id'))
        notes.append(document)
    return notes

# Create Notes
async def create_note(KeepNote):
    document = KeepNote.dict()
    result = await collection.insert_one(document)
    return document


# Update Notes
async def update_note(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc }})
    document = await collection.find_one({"title": title})
    return document

# Delete Notes
async def remove_note(title):
    await collection.delete_one({"title": title})
    return True
