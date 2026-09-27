import requests, os, random
from datetime import datetime as dt

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@AnantapurStudyBuddy"

def get_news():
    today = dt.now().strftime("%d-%m-%Y")
    date_seed = int(dt.now().strftime("%d%m%Y"))
    random.seed(date_seed)
    
    national_list = [
        "ISRO announces Gaganyaan test date - Big boost to space",
        "PM Modi launches new Vande Bharat route",
        "Supreme Court new judgement on jobs reservation",
        "India GDP growth crosses 7 percent this quarter",
        "New Education Policy update from Centre"
    ]
    
    ap_list = [
        "AP Govt releases Mega DSC notification 2026",
        "Anantapur receives new industrial park approval",
        "AP Police recruitment 1000 posts announced",
        "Amaravati capital works resume - CM announcement",
        "APPSC Group 2 mains dates released"
    ]
    
    sports_list = [
        "Team India wins series - Kohli century",
        "Neeraj Chopra wins gold in Diamond League",
        "IPL 2026 schedule released today",
        "Anantapur youth selected for Ranji team"
    ]
    
    n = random.choice(national_list)
    a = random.choice(ap_list)
    s = random.choice(sports_list)
    
    msg = f"""Anantapur Study Buddy - Daily Current Affairs

Date: {today}

1. National: {n}

2. State AP: {a}

3. Sports: {s}

4. Science: ISRO NASA new discovery - Students must know!

Daily 6 AM ki Current Affairs vastayi - Share to friends!"""
    return msg

msg = get_news()
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
res = requests.post(url, json={"chat_id": CHANNEL, "text": msg})
print(res.text)
       
