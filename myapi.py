from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def index():
    return {"name":"First"}
# query parameters
# /blogs?limit=20&published=true
# Not define query parameters in this path(route) but this is accepted inside this function ..path parameters are those which are defind inside path(route)
# limit , published are query parameter with their default values as 10 and true ..sort is the optional query parameter and sort default value is taken as None .......EG http://127.0.0.1:8000/blogs?limit=20&published=False

@app.get('/blogs')
def show(limit:int=10,published:bool=True,sort:Optional[int]=None):
    if published:
        return {f"{limit} published blogs"}
    else:
        return {f"{limit}blogs"}


@app.get('/blogs/unpublished')
def show():
    return {"all unpublished blogs"}

# As below path is blogs/id that is dynamic route ..if i had written this dynamic route above the route /blogs/unpublished  then whenever the user goes to blogs/unpublished then it would give error as Fast api reads routing line by ine ...it would take unpublished as {id} dynamic id thus this function of /blogs/{id} will execute and then give type error that id is not integer

@app.get('/blogs/{id}')
def show(id:int):
    return {"blog":{id}}

class Blog(BaseModel):
    title:str 
    body:str 
    published:Optional[bool]=None

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is created with title {blog.title}"}