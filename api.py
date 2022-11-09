from fastapi import FastAPI, Request
from datetime import datetime






storage = FastAPI(title='My FastAPI')

# # flask way
# @app.route('/',methods=['GET','POST'])
# def index():
#     return "This is the index/first page of my server"



#  fast API way
@storage.get('/')
def index():
    return "This is the index/first page of my API!!!!"

@storage.get("/today")# route with GET Method
def today():
    return str(datetime.now())

@storage.get("/mynames")
def names(first_name:bool=False,last_name:bool=False, full_name=False):
    full_names =""
    if first_name:
        full_names+= "Arnaud"
    if last_name:
        full_names +=' KAYONGA'
    if full_name:
        full_names +=f'My names are {first_name} {last_name}'

    return full_names


# if __name__=='__main__':
#     app.run()

# pip install fastapi
# pip install uvicorn
# crl + C to stop the server and then run the following:
# uvicorn main:app --reload

# Rename the file from main.py to api.py

# Now to run it again type: uvcorn api:storage --reload
