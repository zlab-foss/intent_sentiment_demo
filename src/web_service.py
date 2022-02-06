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

intents = {
    "bg":   'عملکرد برند خوب'  ,
    "bb":   'عملکرد برند بد' ,
    "cem":   'رضایت مشتری' ,
    "ceu":   'نارضایتی مشتری' ,
    "csu":   'پشتیبانی نامناسب',
    "csg":   'پشتیبانی مناسب',
    "dd":   'محصول آسیب دیده',
    "dl":   'تاخیر در ارسال',
    "do":   'ارسال به موقع',
    "pc":   'قیمت ارزان' ,
    "pe":   'قیمت به صرفه و اقتصادی' ,
    "px":   'قیمت گران' ,
    "prc":   'ذکر قیمت' ,
    "pag":   'ظاهر خوب و زیبا' ,
    "pab":   'ظاهر نامناسب' ,
    "pfb":   'خراب بودن محصول از ابتدا' ,
    "pfa":   'خراب شدن محصول پس از مدتی' ,
    "pim":   'اطلاعات گمراه کننده محصول' ,
    "pin":   'اطلاعات ناکافی محصول' ,
    "pid":   'عدم تطابق جزییات محصول' ,
    "ppg":   'بسته بندی مناسب',
    "ppb":   'بسته بندی نامناسب',
    "ppqh":   'کیفیت بالای محصول',
    "ppqm":   'کیفیت متوسط محصول',
    "ppql":   'کیفیت پایین محصول',
    "psg":   'خوب بودن ویژگی (های) محصول' ,
    "psb":   'بد بودن ویژگی (های) محصول' ,
    "pup":   'ناموجود بودن محصول' ,
    "puc":   'ناموجود بودن مدل / رنگ و ...' ,
    "pry":   'پیشنهاد محصول' ,
    "prn":   'عدم پیشنهاد محصول' ,
    "g":   'راهنمایی و توضیحات' ,
    "q":   'سوال' ,
    "wor":   'پیشتهاد شگقت انگیز' ,
    "crt":   'انتقاد' ,
    "wis":   'ارسال کالای اشتباه' ,
    "so":   'پیشنهاد ویژه'
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
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Something's wrong!")



@app.post("/intent", status_code=status.HTTP_200_OK)
async def intent(phrase: str):
    try:
        return {
            "intent_1": {
                "label_1": intents[predict_intent(query=phrase)['intent_1']['label']],
                "confidence_1" : predict_intent(query=phrase)['intent_1']['confidence']
                },
            "intent_2": {
                "label_2": intents[predict_intent(query=phrase)['intent_2']['label']],
                "confidence_2" : predict_intent(query=phrase)['intent_2']['confidence']
                },
            "intent_3": {
                "label_3": intents[predict_intent(query=phrase)['intent_3']['label']],
                "confidence_3" : predict_intent(query=phrase)['intent_3']['confidence']
                }
        }
    except:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Something's wrong!")