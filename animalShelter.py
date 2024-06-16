# Mark Jumper
# CS 340 Client/Server Development
# 4/24/2023
#
# This project uses pymongo do connect to a MongoDB database
# In this, I create methods to connect to and perform CRUD operations to the MongoDB


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            print ("Username and Password are:", username, password)
            self.client = MongoClient('mongodb://%s:%s@localhost:29704/AAC' % (username, password))
            # where xxxx is your unique port number
            self.database = self.client['AAC']
            print ("Connection was successful")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        #return True
        if data is not None:
            if data:
                #replaced '_one' with '_many'
                result = self.database.animals.insert(data)  # data is a dictionary
                
                print(len(data), "inserted record(s)")
                return True if len(data) > 0 else False
        else:
            #data/exception handling
            return False
            raise Exception("Nothing to save, because data parameter is empty")
        

    ############################################
    # read method that only returns one record #
    ############################################
            
    def read(self, search):
        if search is not None:
            result = self.database.animals.find(search,{"_id":False}).limit(1000)
            numDocs = self.database.animals.count_documents(search)
            print(numDocs,"documents.")
            return result
        else:
            raise Exception("Could not find data")
        
    ############################################
    # update method that only returns one record #
    ############################################
            
    def update(self, search, updt):
        
        if search is not None: 
            if search:
                result = self.database.animals.update_many(search, updt)
                #print("Updating Record...")
                
                #find record again and return updated value. 
                print(result.modified_count, "record(s) Updated!")
                return True if result.modified_count > 0 else False
        else:
            #data/exception handling
            print("Check record to update, or record does not exist...")
            raise Exception("Exception: Record not found")
            return False
        
        

    def delete(self, data):
        if data is not None:
            if data:
                #create variable to store data and return record for deletions - this is for accidentals so we could re-create record if it was incorrectly entered
                                
                record = self.database.animals.delete_many(data)
                
                #try to return record, successful deletion returns "None" and statement.
                print(record.deleted_count, "record(s) deleted.")                
                return True if record.deleted_count > 0 else False
        else:
            #data/exception handling
            raise Exception("Record not found.")
            return False
            
        
        
        
        
        
        