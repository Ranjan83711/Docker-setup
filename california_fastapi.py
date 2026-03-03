from fastapi import FastAPI
import joblib
import numpy as np
import uvicorn

app = FastAPI()

# Load model
# file = r"E:\Downloads\california1.joblib"
loaded_model = joblib.load("california1.joblib")
model = loaded_model["model"]
columns = loaded_model["columns"]

@app.get("/")
def home():
    return {"message": "Welcome to California Housing Price Prediction API"}

@app.get("/predict")
def predict(
    MedInc: float = 0,
    HouseAge: float = 0,
    AveRooms: float = 0,
    AveBedrms: float = 0,
    Population: float = 0,
    AveOccup: float = 0,
    # Latitude: float = 0,
    # Longitude: float = 0
):
    inputs = [
        MedInc, HouseAge, AveRooms, AveBedrms,
        Population, AveOccup
    ]

    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)

    return {"Predicted House Price": prediction[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)