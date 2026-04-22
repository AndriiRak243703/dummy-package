from fastapi import FastAPI
from .smart_predict import predict_next

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"Hello": name}

@app.get("/predict")
def predict(numbers: str):
    number_list = [float(n) for n in numbers.split(",")]
    result = predict_next(number_list)
    return {"Next predicted value": result}