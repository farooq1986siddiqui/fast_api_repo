from fastapi import FastAPI


app: FastAPI = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
