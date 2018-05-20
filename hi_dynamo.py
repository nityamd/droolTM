from pynamodb.models import Model
from pynamodb.attributes import (
     UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
 )

from pynamodb.models import batch_get
from datetime import datetime
from flask import Flask, request, abort

app = Flask(__name__)

class UserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "user"
        aws_access_key_id = 'AKIAIQSHG7SIK36GDYJQ'
        aws_secret_access_key = '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'
    #first_name = UnicodeAttribute(hash_key=True)
    #last_name = UnicodeAttribute(range_key=True)
    username = UnicodeAttribute(hash_key=True)
    password =  UnicodeAttribute(range_key=True)

    email = UnicodeAttribute(null=True)
    #given_name = UnicodeAttribute(null=True)
    #family_name = UnicodeAttribute(null=True)
    #zip_code = NumberAttribute(null=True)
    #timestamp = UTCDateTimeAttribute(null=True)


#UserModel.create_table(read_capacity_units=1, write_capacity_units=1)

#user = UserModel("John", "Denver")
#user.email = "djohn@company.org"
#user.save()

for user in UserModel.query("John", filter_condition= (UserModel.email=="djohn@company.org")):
    print(user.first_name)
#for user in UserModel.query("Denver", first_name__begins_with="J"):
 #   print(user.first_name)

@app.route('/', methods=["GET"])
def landing():
    #What I'm calling here is the table related to the key-value pair of the username being called;
    foundPosts = UserModel("Data1","Data2")
    return foundPosts

#@app.route('/ ----', methods = ["GET"])
#def




