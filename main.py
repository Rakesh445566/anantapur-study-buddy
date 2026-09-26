import os
import requests
import datetime

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@AnantapurStudyBuddy"

def get_news():
    today = datetime.date.today().strftime("%d-%m-%Y")
    msg = f"""📚 *Anantapur Study Buddy - Daily Current Affairs*
📅 {today}

1️⃣ *National:* ISRO to launch new satellite today - Boost to India space mission

2️⃣ *State AP:* AP Govt announces new jobs notification - 1000+ posts

3️⃣ *Sports:* Indian cricket team wins - Anantapur youth inspired!

4️⃣ *Science:* New AI technology launched in India

🔥 *Daily 7 AM ki Current Affairs vastayi - Share to friends!*"""
    return msg

def send():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL, "text": get_news(), "parse_mode": "Markdown"}
    r = requests.post(url, data=data)
    print(r.text)

if __name__ == "__main__":
    send()
