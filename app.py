from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
import uvicorn

app = FastAPI()

# Load model
loaded_model = joblib.load("california1.joblib")
model = loaded_model["model"]
columns = loaded_model["columns"]

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html") as f:
        return f.read()


@app.post("/predict", response_class=HTMLResponse)
def predict(
    MedInc: float = Form(...),
    HouseAge: float = Form(...),
    AveRooms: float = Form(...),
    AveBedrms: float = Form(...),
    Population: float = Form(...),
    AveOccup: float = Form(...)
):

    inputs = [
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup
    ]

    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)

    result = round(float(prediction[0]), 3)

    return f"""
    <html>
    <head>
        <title>Prediction Result</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:50px;">
        <h2>🏠 Predicted California House Price</h2>
        <h1>{result}</h1>
        <br>
        <a href="/">Go Back</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)