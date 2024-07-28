from fastapi import FastAPI 

app=FastAPI()

@app.get("/")
def index():
    return {"name":"First"}

@app.get('/blogs/unpublished')
def show():
    return {"all unpublished blogs"}

# As below path is blogs/id that is dynamic route ..if i had written this dynamic route above the route /blogs/unpublished  then whenever the user goes to blogs/unpublished then it would give error as Fast api reads routing line by ine ...it would take unpublished as {id} dynamic id thus this function of /blogs/{id} will execute and then give type error that id is not integer

@app.get('/blogs/{id}')
def show(id:int):
    return {"blog":{id}}