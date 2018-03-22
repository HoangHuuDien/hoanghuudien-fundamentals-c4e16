from gmail import Gmail, Message
from random import choice
import datetime
gmail = GMail('hoangdmdien@gmail.com','Dien12345')

html_content = """<p>Ch&agrave;o anh Tuấn Anh</p>
<p>H&ocirc;m qua trời mưa gi&ocirc;ng b&atilde;o, em bị {{sickness}}</p>
<p>Em nghỉ nh&eacute;</p>
<p>Thanks anh</p>"""

reason = ['headache', 'stomache', 'h5n1', 'h5n2']

reasons = choice(reason)

msg = Message('Haha',to='techkidsc4e16@gmail.com',html=html_content.replace("{{sickness}}", reasons))
now = datetime.now().time().hour

While True :
    if now == 7:
        gmail.send(msg)
    break
