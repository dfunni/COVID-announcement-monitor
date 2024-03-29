import requests
import utils
from bs4 import BeautifulSoup


def check_announcements(announcements, text):
    updated = False
    msg = []

    # case where announcments are removed
    if len(announcements) == 0:
        msg.append("""Alert: there are currently no announcements on the
        Palomar Objevatory website""")
        updated = True

    # case where there are announcements 
    for announcement in announcements:
        ann = announcement.text

        if closed not in ann:
            msg.append(ann)
            updated = True
        else:
            msg.append("Still Closed")


    return '\n\n'.join(msg), updated

link = 'https://www.astro.caltech.edu/palomar/homepage.html'
req = requests.get(link)
page = BeautifulSoup(req.text, 'html.parser')
announcements = page.select('.announcement')
closed = "Palomar Observatory is closed to the public"
subject = ' '.join(str.split(closed)[:2])
body, updated = check_announcements(announcements, closed)
body += f'\n{link}'

if updated:
    subject += " Update"
    utils.send_email(subject, body, receiver='dfunni@gmail.com')
else:
    utils.send_email(subject, body)

