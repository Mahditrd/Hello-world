from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Hello():
    return f'Hello World'