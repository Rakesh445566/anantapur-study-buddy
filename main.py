import requests

BOT_TOKEN = "8557258154:AAHNcziTdnx2IeM7IdRnZXRwS8kSoJkL8ZY"
CHANNEL = "@AnantapurStudyBuddy"

message = """📚 *Anantapur Study Buddy - Daily Current Affairs*
📅 26-09-2026

1️⃣ National: New Education Policy update
2️⃣ AP: Amaravati works approved  
3️⃣ Sports: India wins match
4️⃣ Economy: RBI guidelines
5️⃣ Science: ISRO new mission

💡 Quiz: AP Governor evaru?
Ans: S. Abdul Nazeer

Daily 7 AM ki vastundi! Share cheyandi!
#APPSC #CurrentAffairs"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {"chat_id": CHANNEL, "text": message, "parse_mode": "Markdown"}
r = requests.post(url, data=data)
print(r.text)
print("Sent!")
