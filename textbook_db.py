from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://abhinavsai:3wm03uNaQCbijKZu@cluster0.7zpqnji.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Database and collection
collection_textbooks = client["Textbooks"]["content"]

def fetch_textbook_content(class_selected, subject_selected, topic):
    doc = collection_textbooks.find_one({
        "class": int(class_selected),
        "subject_name": subject_selected,
        "topic": topic
    })
    return doc["textbook"].strip() if doc and doc.get("textbook") else ""

print(fetch_textbook_content(7, "Social Studies", "k"))
