from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_api():
    return {'status': 'UP'}


@app.get("/{name}")
def hello_name(name: str):
    return {'message': 'Hello ' + name}
