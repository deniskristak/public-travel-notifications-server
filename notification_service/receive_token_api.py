from fastapi import FastAPI, Request
from helpers.db_connection import db_connection
from user_requests import UserRequest, UserRequestHandler
app = FastAPI()


# method for listening to POST api calls
# test with
# curl -i -X POST -H 'Content-Type: application/json' -d '{"token": "something"}' https://thenis.co.uk/receive-token/
# todo: add error handling
@app.post("/receive-token/")
async def receive_message(request: Request):
    response = await request.json()
    store_token(response['token'])
    # TODO: once we are sending real requests (trains to follow etc.), we will call stuff from `user_requests.py` here
    return {"message": "Received token successfully"}


def store_token(token):
    cursor = db_connection.get_cursor()

    cursor.execute("""
            INSERT INTO `device_tokens`
                (`device_token`)
            VALUES
                (%(device_token)s)
        """, {
        'device_token': token['token']
    })

    db_connection.get_db().commit()


@app.get("/get-test/")
async def receive_message():
    print("Get successful")
    return "Get successful"
