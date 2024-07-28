from fastapi import FastAPI 

app=FastAPI()

@app.get("/")
def index():
    return {"name":"First"}

@app.get('/blogs/unpublished')
def show():
    return {"all unpublished blogs"}

@app.get('/blogs/{id}')
def show(id:int):
    return {"blog":{id}}