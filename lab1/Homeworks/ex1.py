from gmail import GMail,Message
from datetime import *
gmail= GMail("hohainam7@gmail.com","codethechange")
while True:
    if datetime.now().hour == 7 :
        message= Message("hello, ",to="qhuydtvt@gmail.com",text="em xin nghi a")
        gmail.send(message)
        break
print("sent")