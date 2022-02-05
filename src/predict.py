from .preprocess import preprocess
import fasttext


intent_model = fasttext.load_model("./statics/INTENT_model.bin")
sentiment_model = fasttext.load_model("./statics/SENTIMENT_model.bin")



def predict_intent(query: str):
    return {
        "intent_1": {
            "label":intent_model.predict(preprocess(query), k=3)[0][0][9:],
            "confidence": intent_model.predict(preprocess(query), k=3)[1][0]
        },
        "intent_2": {
            "label":intent_model.predict(preprocess(query), k=3)[0][1][9:],
            "confidence": intent_model.predict(preprocess(query), k=3)[1][1]
        },
        "intent_3": {
            "label": intent_model.predict(preprocess(query), k=3)[0][2][9:],
            "confidence": intent_model.predict(preprocess(query), k=3)[1][2]
        }
    }



def predict_sentiment(query: str):
    return {
        "sentiment": {
            "label": sentiment_model.predict(preprocess(query), k=1)[0][0][9:],
            "confidence": sentiment_model.predict(preprocess(query), k=1)[1][0]
        }
    }
