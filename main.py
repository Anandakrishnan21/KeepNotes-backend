from database import (
    fetch_one_note,
    fetch_all_notes,
    create_note,
    update_note,
    remove_note,
)
from fastapi import FastAPI,HTTPException
from model import test
from fastapi.middleware.cors import CORSMiddleware
# cors - cross origin resource sharing

# app object
app = FastAPI()


origin = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {"Hello": "world!"}

# uvicorn main:app --reload


@app.get('/api/keepNotes')
async def get_notes():
    response = await fetch_all_notes()
    return response


@app.get('/api/keepNotes/{title}', response_model=test)
async def get_notes_by_title(title):
    response = await fetch_one_note(title)
    if response:
        return response
    raise HTTPException(400, "something went wrong")


@app.post('/api/keepNotes', response_model=test)
async def post_notes(note: test):
    response = await create_note(note)
    if response:
        return response
    raise HTTPException(400, "something went wrong")


@app.put('/api/keepNotes/{title}', response_model=test)
async def put_notes(title: str, desc: str):
    response = await update_note(title, desc)
    if response:
        return response
    raise HTTPException(400, "something went wrong")


@app.delete('/api/keepNotes/{title}')
async def delete_notes(title):
    response = await remove_note(title)
    if response:
        return "Successfully deleted Note"
    raise HTTPException(404, f"There is no paper with title {title}")


# first - pip install pipenv
# second - pipenv shell
# third - pipenv install -r requirements.txt or python -m pipenv install -r requirements.txt
# run - uvicorn main:app --reload or python -m uvicorn main:app --reload
#  env - environment variable mainly for storing secret keys, API's and all.