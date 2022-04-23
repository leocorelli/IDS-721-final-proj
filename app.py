from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from load_model import load_model
import pandas as pd
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory='html-directory')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/winequality")
async def predict_quality(request: Request):
    model = load_model("./models/winequality-randomforest.pkl")
    df = pd.DataFrame(columns=['free_sulfur_dioxide', "fixed_acidity", "alcohol", "density", "sulphates", "residual_sugar", "citric_acid", "total_sulfur_dioxide", "pH", "chlorides", "volatile_acidity"])
    df.loc[0] = [7.4, 0.70, 0.00, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]    
    pred = str(np.round(model.predict(df)[0],2))
    return templates.TemplateResponse("results.html", {"request": request, "prediction": pred})

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')