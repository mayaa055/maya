import os, requests, datetime
TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
HASHTAGS = [
    "#السعودية #الرياض #جدة #مكة",
    "#الامارات #دبي #ابوظبي",
    "#قطر #الدوحة",
    "#الكويت #الكويت_العاصمة",
    "#البحرين #المنامة",
    "#عمان #مسقط #صلالة",
]
now = datetime.datetime.now()
index = (now.hour * 12 + now.minute // 5) % len(HASHTAGS)
text = HASHTAGS[index]
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, json={"chat_id": CHAT_ID, "text": text})
