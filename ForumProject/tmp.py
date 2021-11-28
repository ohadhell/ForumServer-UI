import os
f=open("Server.py",'rb')
txt=f.read()
f.close()
txt=txt.replace('data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)','data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)\r\ndata=data.replace("NAMEEE","username/message.html")')
