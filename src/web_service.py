from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from .predict import predict_intent, predict_sentiment

sentiments = {
    "1": "خیلی منفی",
    "2": "منفی",
    "3": "خنثی",
    "4": "مثبت",
    "5": "خیلی مثبت"
}

app = FastAPI()

@app.post("/sentiment", status_code=status.HTTP_200_OK)
async def sentiment(phrase: str):
    try:
        return {
            "sentiment": sentiments[predict_sentiment(query=phrase)['sentiment']['label']],
            "confidence": predict_sentiment(query=phrase)['sentiment']['confidence']
        }
    except:
        raise HTTPException(status.HTTP_409_CONFLICT)