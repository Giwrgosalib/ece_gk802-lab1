import requests
x=input("Enter Desired URL:")
r=requests.get(x)
for i in r.headers:
    print(i)
