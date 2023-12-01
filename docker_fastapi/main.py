from fastapi import FastAPI

app = FastAPI(title="Dependency Injection")

@app.get("/ping")
def ping():
    return "pong"

