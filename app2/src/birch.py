import requests
import utils
from bs4 import BeautifulSoup

def check_text(website_txt, closed_text):
    updated = False
    closed_msgs = []

    # case where page has been removed
    if len(website_txt) == 0:
        msg.append("""Alert: there are currently no announcements on the
        Birch Aquarium website""")
        updated = True
 
    for para in website_txt:
        par = para.text
        if closed_text in par:
            closed_msgs.append(par)
    if len(closed_msgs) == 0:
        msg = "Still Closed"
    else:
        updated = True
        msg = "Check the Birch Aquarium website."

    return msg, updated

link = 'https://aquarium.ucsd.edu/birch-aquarium-update-covid-19'
req = requests.get(link)
page = BeautifulSoup(req.text, 'html.parser')
website_txt = page.select('p')
closed_text = "open"
subject = "Birch Aquarium Closed" 
body, updated = check_text(website_txt, closed_text)
body += f'\n{link}'
if updated:
    subject += " Update"
    utils.send_email(subject, body, receiver='dfunni@gmail.com')
else:
    utils.send_email(subject, body)
