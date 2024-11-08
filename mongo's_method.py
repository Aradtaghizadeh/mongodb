from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def insert_many(self, collection_name, documents):
        collection = self.db[collection_name]
        result = collection.insert_many(documents)
        return result.inserted_ids

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find_many(self, collection_name, query):
        collection = self.db[collection_name]
        return list(collection.find(query))

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_one(query, update)
        return result.modified_count

    def update_many(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_many(query, update)
        return result.modified_count

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

    def delete_many(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_many(query)
        return result.deleted_count

    def count_documents(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.count_documents(query)

    def close(self):
        self.client.close()

# Example usage:
if __name__ == "__main__":
    mongo_client = MongoDBClient('mongodb://localhost:27017/', 'my_database')

    # Insert a document
    doc_id = mongo_client.insert_one('my_collection', {'name': 'Alice', 'age': 30})
    print(f'Inserted document ID: {doc_id}')

    # Find a document
    document = mongo_client.find_one('my_collection', {'name': 'Alice'})
    print(f'Found document: {document}')

    # Update a document
    updated_count = mongo_client.update_one('my_collection', {'name': 'Alice'}, {'$set': {'age': 31}})
    print(f'Modified documents count: {updated_count}')

    # Delete a document
    deleted_count = mongo_client.delete_one('my_collection', {'name': 'Alice'})
    print(f'Deleted documents count: {deleted_count}')

    # Close the client
    mongo_client.close()