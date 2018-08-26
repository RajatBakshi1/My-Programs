# Q1:-  What is an access token? Generate your access token for any API.

'''
Access Tokens:- An access token is an object that describes the security context of a process or thread.

API Key:- AIzaSyAz9kfWWe0-i8xmYQo0SPkzQPIwLVqWtrQ
'''

# Q2:- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
'''
import socket
print(socket.gethostbyname('google.com'))
'''

# Q3:-  Using google API.
'''
import urllib.request
import json
url='https://maps.googleapis.com/maps/api/directions/json?'
api='AIzaSyARaUqq0lZgvvD6W6lUH1l0HEwm8kd5DHo'
origin=input("Tell me your location:").replace(' ','+')
destination=input("Where you want to go ? :").replace(' ','+')
nav_request='origin={}&destination={}&key={}'.format(origin,destination,api)
request=url+nav_request
response=urllib.request.urlopen(request).read().decode('utf-8')
directions=json.loads(response)
print(directions)
'''

# Q4:- What is a difference between library and API . Figure it out with examples.
'''
::--  A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects.

::--  An API is an interface for other programs to interact with your program or library  without having direct access.

::--  Library: android.app.Activity library (Class with all code)

::--  API: Android API to interact with hardware, like the front camera of an Android-based device.
           If your app needs to vibrate the phone, you must use the Android API method like vibratePhone()
'''

# Q5:- Try to access Spotify API . Find out some library for it and play some music.
'''
import sendgrid
import os
from sendgrid.helpers.mail import *
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
from_email = Email("My Email: ")
to_email = Email("Reciever's email: ")
subject = "Assignment for AcadView."
content = Content("Completed my assignment.", "You will get it on github link. ")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
'''
