import os
import socket
import time

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip
###new thread example
def copy(path):
    txt=open(path,'rb')
    txt2=txt.read()
    txt.close()
    return txt2
###replace threadname with the new file name
def replacethread(txt,threadname):
    txt=txt.replace("threadname",threadname)
    return txt
###find if name is in username
def isuser(name):
    username1=open("users.txt",'rb')
    username=username1.read()
    username1.close()
    if (username.find("U="+name)>0):
        print "trueeeeeeeeeeeeeee"
        return True
    print "falseeeeeeeeeeeeeeeeeeeeee"
    return False
###get the username from the cookies
def getuser(txt):
    if "username=" in txt:
        f=txt.find("username=")+9
        f2=txt.find("username=")+10
        txt=list(txt)
        txt=txt[f:]
        txt2=txt[f2:]
        txt="".join(txt)
        txt2="".join(txt2)
        f=txt.find("\r\n\r\n")
        f2=txt2.find('=="')
        txt=list(txt)
        txt4="NOTLOGGEDIN"
        if f>0:
            txt=txt[:f]
            txt4="".join(txt)
        if f2>0:
            txt2=txt2[:f2]
            txt4="".join(txt2)
        print txt4
        return txt4
    if "admin=" in txt:
        f=txt.find("admin=")+6
        f2=txt.find("admin=")+7
        txt=list(txt)
        txt=txt[f:]
        txt2=txt[f2:]
        txt="".join(txt)
        txt2="".join(txt2)
        f=txt.find("\r\n\r\n")
        f2=txt2.find('=="')
        txt=list(txt)
        txt4="NOTLOGGEDIN"
        if f>0:
            txt=txt[:f]
            txt4="".join(txt)
        if f2>0:
            txt2=txt2[:f2]
            txt4="".join(txt2)
        print txt4
        return txt4
###is logged in ? if username in cookies he is logged in
def islogged(txt):
    if "username=" in txt:
        return True
    if "admin=" in txt:
        return True
    else:
       return False
def isadmin(username):
    print "didddddddddddddddddddddddddddddddddddddddddddddddddddd"
    admin1=open("admins.txt","rb")
    admin=admin1.read()
    admin1.close()
    u=username.replace('"',"")
    if(admin.find(u))>0:
        print "trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        return True
    return False

def updateforum(update,name,path,IP,num):
    b=["<style> body {background: url('sports.jpg');background-size: 113%;background-repeat: no-repeat;}</style>","<style> body {background: url('news.jpg');background-size: 90%;background-repeat: no-repeat;background-position: 50px -45px; }</style>","<style> body {background: url('movies.jpg');background-size: 90%;background-repeat: no-repeat;}</style>","<style> body {background: url('gaming.jpg');background-size: 102%;background-repeat: no-repeat;}</style>","<style> body {background: url('music.jpg');background-size: 90%;background-repeat: no-repeat;}</style>","<style> body {background: url('multimedia.jpg');background-size: 90%;background-repeat: no-repeat;}</style>"]
    update=open(update,'wb')
    txt=("<!DOCTYPE html>\r\n<html>\r\n<head>\r\n"+b[num]+"<title>"+name+"</title>\r\n<h1>"+name+" Forum</h1>\r\n</head>\r\n<body>\r\n")
    for file in os.listdir(path):
        if file.endswith(".txt"):
            f=file
            f=f.split(".")
            f=f[0]
            f2=f.replace("%20"," ")
            f2=f2.replace("QUSMRK","?")
            txt=txt+"<h2>\r\n<a href=http://"+IP+":8080/"+path+"/"+f+".html>"+f2+"</a>\r\n</h2>"
    txt=txt+"</body>\r\n</html>\r\n\r\n<html>\r\n<body>\r\n<button onclick='myFunction()'"+">New Thread</button><br>\r\n</body>\r\n</html>\r\n\r\n<script>\r\nfunction myFunction() {\r\n	window.open('http://"+IP+":8080/Example/"+name+"newthread.html', '_self')\r\n}\r\n</script>"
    txt=txt+'</script><div id="home" style="position: absolute; top: 50px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IP+':8080/playplay.html" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="7">Home &#8962 </font></span></div></a></div>'
    update.write(txt)
    update.close()

def makeadmin(name):
    temp=open("users.txt",'rb')
    users=temp.read()
    temp.close()
    users=users.split("[")
    print users
    right=0
    for i in range (len(users)):
        f=users[i].find("U="+name)
        if f>=0:
            right=i
        else:
            pass
    if right>0:
        f=users[right-1].find("F=")
        temp=list(users[right-1])
        temp=temp[f:]
        users[right-1]="".join(temp)
        users[right-1]=users[right-1]+"["
        f=users[right].find("]")
        temp=list(users[right])
        temp=temp[:f]
        users[right]="".join(temp)
        admin=users[right-1]+users[right]+"]"
        users=open("admins.txt",'ab')
        users=users.write(admin+"\r\n")
    else:
        pass

def findoldip():
    f=open('login.html','rb')
    txt=f.read()
    f.close()
    f1=txt.find('http://')
    f2=txt.find(':8080')
    ip=list(txt)
    ip=ip[f1+7:f2]
    ip="".join(ip)
    return ip
###editing comments or threads
###styling
###live scores and such as features
###second pages in sports.html....
###administrator
###https


def createprofile(name,IPADDRESS):
    os.makedirs("Users/"+name)
    f1=open("Users/"+name+"/profile.html",'wb')
    f2=open("Users/"+name+"/message.html",'wb')
    f3=open("Users/"+name+"/counter.html",'wb')
    f4=open("Users/"+name+"/background.jpg",'wb')
    f5=open("landscape.jpg",'rb')
    tmp=f5.read()
    f5.close()
    f4.write(tmp)
    f4.close()
    txt1='<!DOCTYPE html><html><style> body {background: url("background.jpg");background-size: 102%;background-repeat: no-repeat;}</style><title>NAME</title><head><link rel="icon" href="favicon.ico" type="image/gif" sizes="16x16"></head><body><h1 style="color:black">NAME</h1><br><br><br><h2 style="color:black">joined on:'+time.asctime( time.localtime(time.time()) )+'</h2><br><br><br><h4 style="color:black">number of messages:0</h4><br><br><br><br><br><textarea rows="4" cols="50" id="textarea"></textarea><button onclick="myFunction()">send private message</button></body></html><script>function myFunction() {data=document.getElementById("textarea").value\r\nwindow.open("http://'+IPADDRESS+':8080/Users/NAME/message="+data, "_self")}</script><div id="home" style="position: absolute; top: 50px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IPADDRESS+':8080/playplay.html" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="7">Home &#8962 </font></span></div></a></div>'
    txt1=txt1.replace("NAME",name)
    f1.write(txt1)
    f1.close()
    f3.write("0")
    txt2='<!DOCTYPE html><html><style> body {background: url("background.jpg");background-size: 102%;background-repeat: no-repeat;}</style><title>Messages</title><body><html><p style="color:black; position: absolute; top: 510px; right: 100px;">instructions for uploading image for new background:</p><p style="color:black;position: absolute; top: 525px; right: 70px;">paste an image url in the text box above and click "upload"</p><textarea style="position: absolute; top: 500px; height: 20px; width: 200px; right: 200px;" rows="1" cols="50" id="textarea"></textarea><button style="position: absolute; top: 500px; height: 20px; width: 80px; right: 100px;" onclick="myFunction()">upload</button><br><select id="select" style="position: absolute; top: 450px; height: 20px; width: 70px; right: 335px;"> <option value="black">Black</option><option value="white">White</option><option value="red">Red</option><option value="green">Green</option><option value="yellow">Yellow</option></select><button style="position: absolute; top: 450px; height: 20px; width: 120px; right: 200px;" onclick="myFunction1()">Change Color</button><br><p style="color:black; position: absolute; top: 400px; right: 170px;">Change your profile font color to:</p><button style="position: absolute; top: 350px; height: 40px; width: 120px; right: 200px;" onclick="myFunction2()">Check your profile</button><button style="position: absolute; top: 300px; height: 20px; width: 120px; right: 200px;" onclick="myFunction3()">Clear messages</button><br><br></body></html><script>function myFunction() {data=document.getElementById("textarea").value\r\nwindow.open("http://'+IPADDRESS+':8080/link?"+data, "_self")}</script><script>function myFunction1() {data=document.getElementById("select").value\r\nwindow.open("http://'+IPADDRESS+':8080/color?"+data, "_self")}</script><script>function myFunction2() {window.open("http://'+IPADDRESS+':8080/Users/'+name+'/profile.html", "_self")}</script><script>function myFunction3() {window.open("http://'+IPADDRESS+':8080/Users/'+name+'/msgclear","_self")}</script><div id="home" style="position: absolute; top: 50px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IPADDRESS+':8080/playplay.html" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="7">Home &#8962 </font></span></div></a></div>'
    f2.write(txt2)
    f2.close()

def addtocount(name,IPADDRESS):
    f=open("Users/"+name+"/counter.html",'rb')
    num=f.read()
    f.close()
    num=int(num)
    num=num+1
    f=open("Users/"+name+"/counter.html",'wb')
    f.write(str(num))
    f.close
    f=open("Users/"+name+"/profile.html",'rb')
    txt=f.read()
    f.close()
    txt=txt.replace("number of messages:"+str(num-1),"number of messages:"+str(num))
    f=open("Users/"+name+"/profile.html",'wb')
    f.write(txt)
    f.close()
def changecolor(name,color,IPADDRESS):
    f1=open("Users/"+name+"/profile.html",'rb')
    f2=open("Users/"+name+"/message.html",'rb')
    txt1=f1.read()
    txt2=f2.read()
    f1.close()
    f2.close()
    try:
        txt1=txt1.replace("color:white","color:"+color)
        txt1=txt1.replace("color:black","color:"+color)
        txt1=txt1.replace("color:green","color:"+color)
        txt1=txt1.replace("color:yellow","color:"+color)
        txt1=txt1.replace("color:red","color:"+color)
        txt1=txt1.replace('color="white"','color="'+color+'"')
        txt1=txt1.replace('color="red"','color="'+color+'"')
        txt1=txt1.replace('color="yellow"','color="'+color+'"')
        txt1=txt1.replace('color="green"','color="'+color+'"')
        txt1=txt1.replace('color="black"','color="'+color+'"')
        txt1=txt1.replace('color:"white"','color:"'+color+'"')
        txt1=txt1.replace('color:"red"','color:"'+color+'"')
        txt1=txt1.replace('color:"yellow"','color:"'+color+'"')
        txt1=txt1.replace('color:"green"','color:"'+color+'"')
        txt1=txt1.replace('color:"black"','color:"'+color+'"')
        txt2=txt2.replace("color:white","color:"+color)
        txt2=txt2.replace("color:black","color:"+color)
        txt2=txt2.replace("color:green","color:"+color)
        txt2=txt2.replace("color:yellow","color:"+color)
        txt2=txt2.replace("color:red","color:"+color)
        txt2=txt2.replace('color="white"','color="'+color+'"')
        txt2=txt2.replace('color="red"','color="'+color+'"')
        txt2=txt2.replace('color="yellow"','color="'+color+'"')
        txt2=txt2.replace('color="green"','color="'+color+'"')
        txt2=txt2.replace('color="black"','color="'+color+'"')
        txt2=txt2.replace('color:"white"','color:"'+color+'"')
        txt2=txt2.replace('color:"red"','color:"'+color+'"')
        txt2=txt2.replace('color:"yellow"','color:"'+color+'"')
        txt2=txt2.replace('color:"green"','color:"'+color+'"')
        txt2=txt2.replace('color:"black"','color:"'+color+'"')
    except:
        print "WTFFFFFFFFFFFFFFFFF"
    f1=open("Users/"+name+"/profile.html",'wb')
    f2=open("Users/"+name+"/message.html",'wb')
    f1.write(txt1)
    f2.write(txt2)
    f1.close()
    f2.close()
    
    
    






















    
