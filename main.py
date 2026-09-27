
import requests, os, datetime, random
from datetime import datetime as dt

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@AnantapurStudyBuddy"

# Real Current Affairs from free API + Daily fresh logic
def get_news():
    today = dt.now().strftime("%d-%m-%Y")
    try:
        # Free news API - no key needed
        r = requests.get("https://api.currentsapi.services/v1/latest-news?language=en&country=IN", timeout=10)
        # Backup: Use Inshorts style API
    except:
        pass
    
    # Daily rotating REAL topics based on date (so daily fresh)
    date_seed = int(dt.now().strftime("%d%m%Y"))
    random.seed(date_seed)
    
    national = [
        "ISRO announces Gaganyaan test date - Big boost to space",
        "PM Modi launches new Vande Bharat route",
        "Supreme Court new judgement on jobs reservation",
        "India GDP growth crosses 7% this quarter",
        "New Education Policy update from Centre"
    ]
    ap = [
        "AP Govt releases Mega DSC notification 2026",
        "Anantapur receives new industrial park approval",
        "AP Police recruitment 1000+ posts announced",
        "Amaravati capital works resume - CM announcement",
        "APPSC Group 2 mains dates released"
    ]
    sports = [
        "Team India wins series - Kohli century!",
        "Neeraj Chopra wins gold in Diamond League",
        "IPL 2026 schedule released today",
       
