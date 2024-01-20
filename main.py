from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import training

from predictions import try_out
from preprocessing import get_clean_data


class UserInput(BaseModel):
    Pclass: int
    Age: int
    Sex: int
    Embarked: int


# load the model from disk
def get_model():
    try:
        loaded_model = joblib.load('model.pkl')
    except FileNotFoundError:
        data = get_clean_data()
        training.train_model(data)
        loaded_model = joblib.load('model.pkl')

    return loaded_model


app = FastAPI()


@app.post("/")
def get_prediction(input: UserInput):
    prediction = try_out(get_model(), input.model_dump().values())

    # return the prediction
    return {"prediction": prediction.item()}
