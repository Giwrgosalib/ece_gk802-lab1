import requests
from datetime import datetime;
x=input("Enter Desired URL:")
r=requests.get(x)
for i in r.headers:
    print(i)
print("Server:"+r.headers['Server'])
if('Set-Cookie' in r.headers):
    print("The URL has Cookies\n")
    for c in r.cookies:
        if c.expires==None:
            print(c.name)
            print("No expiration date")
        else:
            expdate=float(c.expires)
            nowdate=datetime.now().timestamp()
            print(c.name +" \nTime left Until Expiration:"+ str(expdate-nowdate)+" Seconds left")
else:
    print("The URL has no Cookies")

