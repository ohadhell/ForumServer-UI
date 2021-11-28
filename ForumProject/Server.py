import socket
import re
import os
import sys
import Cookie
import urllib2
import shutil
forbidden=False
from threading import Thread
from Queue import Queue
from changing import changeIP,temp,temp2,replace
from deletethreads import delete
from functions import copy,replacethread,isuser,getuser,islogged,isadmin,updateforum,makeadmin,findoldip,get_lan_ip,addtocount,createprofile,changecolor
IPADDRESS=get_lan_ip()###the IP of the current pc
print "ippppppppppppppppppppppppppppp:"
print IPADDRESS
oldip=findoldip()###the ip of the previous pc
changeIP(oldip,IPADDRESS)###replace the ips on all the files on the server
changeIP("127.0.0.1",IPADDRESS)
delete(IPADDRESS)##update the main forums pages

###copying the content of the files for later usage
sportexample=copy("Example/sportsexample.html")
newsexample=copy("Example/newsexample.html")
moviesexample=copy("Example/moviesexample.html")
musicexample=copy("Example/musicexample.html")
multimediaexample=copy("Example/multimediaexample.html")
gamingexample=copy("Example/gamingexample.html")
def one_client_request(client_socket, client_address, a):
    i=0
    #Dealing with one client's request
    delete(IPADDRESS)
    k=a.split(" ")
    if k[0]=="GET" and "HTTP/1.1" in k[2]:
        print k
        ktxt="".join(k)
        url=list(k[1])
        url=url[1:len(url)]
        k[1]="".join(url)
        if "sports.jpg" in k[1]:
            k[1]="Example/sports.jpg"
        if "news.jpg" in k[1]:
            k[1]="Example/news.jpg"
        if "movies.jpg" in k[1]:
            k[1]="Example/movies.jpg"
        if "music.jpg" in k[1]:
            k[1]="Example/music.jpg"
        if "multimedia.jpg" in k[1]:
            k[1]="Example/multimedia.jpg"
        if "gaming.jpg" in k[1]:
            k[1]="Example/gaming.jpg"
        if "olandscape.png" in k[1]:
            k[1]="olandscape.png"
        if "login.html" in k[1]:
            k[1]="login.html"
        if "login2.html" in k[1]:
            k[1]="login2.html"
        if "clogin.html" in k[1]:
            k[1]="clogin.html"
        if "latin.css" in k[1]:
            k[1]="playplay_files/latin.css"
        if "landscape.png" in k[1]:
            k[1]="landscape.png"
        if k[1]=="":
            if islogged(ktxt):
                k[1]="playplay.html"
            else:
                k[1]="home.html"
        if "playplay.html" in k[1]:
            if islogged(ktxt):
                username=getuser(ktxt)
                if isadmin(username):
                    k[1]="adminplayplay.html"
            else:
                k[1]="home.html"
        if "favicon" in k[1]:
            k[1]="./favicon.ico"
        if k[1]=="logout" or k[1]=="/logout":
            if "admin=" in ktxt:
                c=Cookie.SimpleCookie()
                c["admin"]=""
                c["admin"]['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
                sendfile = open("home.html", 'rb')
                data=sendfile.read()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n"+str(c)+"\r\n\r\n")
                client_socket.send(data)
            if "username=" in ktxt:
                c=Cookie.SimpleCookie()
                c["username"]=""
                c["username"]['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
                sendfile = open("home.html", 'rb')
                data=sendfile.read()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n"+str(c)+"\r\n\r\n")
                client_socket.send(data)
            else:
                k[1]="home.html"
            
        if "?comment=" in k[1]:##dealing with a comment 
            f=k[1].find("/?comment=")
            comment=list(k[1])
            path=comment[:f]
            path="".join(path)
            l=len("/?comment=")
            comment=comment[f+l:]
            comment="".join(comment)
            comment=comment.replace("%20", " ")
            s=comment
            s=urllib2.unquote(urllib2.unquote(s.encode("utf8")))
            temp="".join(k)
            if ("username=" not in temp and "admin=" not in temp):##sending to the login page with a proper message if user is not logged in
                sendfile = open("redirect.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                client_socket.send(data)
            else:##publishing the comment on the thread
                temp=getuser(temp)
                writetotxt=open(path,'rb')
                comnum=writetotxt.read()
                comnum=int(comnum)
                comnum=comnum+1
                writetotxt=open(path,'wb')
                temp=temp.decode('base64','strict')
                writetotxt.write(str(comnum))
                writetotxt.close()
                if "Sports" in path:
                    k[1]="Example/sports.html"
                if "News" in path:
                    k[1]="Example/news.html"
                if "Movies" in path:
                    k[1]="Example/movies.html"
                if "Music" in path:
                    k[1]="Example/music.html"
                if "Gaming" in path:
                    k[1]="Example/gaming.html"
                if "Multimedia" in path:
                    k[1]="Example/multimedia.html"
                addtocount(temp,IPADDRESS)
                if (comnum/10.0)>1.0:
                    pg=(comnum/10)+1
                    path2=path.replace(".txt","PG"+str(pg)+".html")
                    originalpath=path
                    path=path.replace(".txt",".html")
                    try:
                        f=open(path2,"rb")
                        ftxt=f.read()
                        f.close()
                    except:
                        f=open(path2,"wb")
                        f.write("")
                        f.close()
                        ftxt=""
                    f=open(path2,"ab")
                    f2=open(path,"rb")
                    ftxt2=f2.read()
                    f2.close()
                    f2=open(path,"ab")
                    txt=""
                    if "!DOCTYPE html" not in ftxt:
                        f=open(path2,"ab")
                        txt='<!DOCTYPE html><html><style> body {background: url("clouds.jpg");background-size: 102%;background-repeat: no-repeat;}</style><title>Far cry 5 </title><head>'
                    buttons='<textarea rows="4" cols="50" id="textarea"></textarea><button onclick="myFunction()">Comment</button><br><button onclick="myFunction2()">Report to Admin</button><br><script>function myFunction() {data=document.getElementById("textarea").value\r\nwindow.open("http://'+IPADDRESS+':8080/'+originalpath+'/?comment="+data,"_self")}</script><script>function myFunction2() {window.open("http://'+IPADDRESS+':8080/Admin/Report/'+path+'","_self")}</script>'+'<a href="http://'+IPADDRESS+':8080/'+path+'">page '+str(1)+'</a>'
                    txt=txt+'<h3><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+s+'</h3>'
                    if "page "+str(pg) not in ftxt2:
                        txt2='<a href="http://'+IPADDRESS+':8080/'+path2+'">page '+str(pg)+'</a>'
                        f2.write(txt2)
                        f2.close()
                    if buttons in ftxt:
                        f.close()
                        f=open(path2,'wb')
                        ftxt=ftxt.replace(buttons,"")
                        f.write(ftxt)
                        f.close()
                        f=open(path2,"ab")
                    f.write(txt+buttons)
                    f.close()
                else:
                    path=path.replace(".txt",".html")
                    f=open(path,"rb")
                    txt=f.read()
                    f.close()
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h3><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+s+'</h3>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    f=open(path,"wb")
                    f.write(txt)
                    f.close()
        if "?tn=" in k[1]:###creating a new thread 
            if islogged(ktxt):
                k[1]=k[1].replace("%20"," ")
                f=k[1].find("?tn=")
                f2=k[1].find("&msg=")
                path=list(k[1])
                threadname=path[f+4:f2]
                threadname="".join(threadname)
                threadname=threadname.replace("?","QUSMRK")
                threadname2=threadname.replace(" ","%20")
                s=threadname2
                s=urllib2.unquote(urllib2.unquote(s.encode("utf8")))
                threadname2=s
                threadname2=threadname2.replace(" ","%20")
                thread=path[f2+5:]
                thread="".join(thread)
                s=thread
                s=urllib2.unquote(urllib2.unquote(s.encode("utf8")))
                thread=s
                path=path[:f]
                path="".join(path)
                temp="".join(k)
                temp=getuser(temp)
                temp=temp.decode('base64','strict')
                newthread2=open(path+"/"+threadname2+".txt","wb")
                newthread2.write(str(1))
                newthread2.close()
                newthread=open(path+"/"+threadname2+"2.txt","wb")
                addtocount(temp,IPADDRESS)
                threadname22=threadname2.replace("%20"," ")
                threadname22=threadname22.replace("QUSMRK","?")
                ############making the thread in the specific forum#####################
                if "Sports" in path:
                    txt=replacethread(sportexample,threadname22)
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h2><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+thread+'</h2>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    newthread.write(txt)
                    newthread.close()
                    (root,ext)=os.path.splitext(path+"/"+threadname2+"2.txt")
                    os.rename(path+"/"+threadname2+"2.txt",path+"/"+threadname2+".html")
                    updateforum("Example/sports.html","Sports","Forum/Sports/Threads",IPADDRESS,0)
                    k[1]="Example/sports.html"
                if "News" in path:
                    txt=replacethread(newsexample,threadname22)
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h2><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+thread+'</h2>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    newthread.write(txt)
                    newthread.close()
                    (root,ext)=os.path.splitext(path+"/"+threadname2+"2.txt")
                    os.rename(path+"/"+threadname2+"2.txt",path+"/"+threadname2+".html")
                    updateforum("Example/news.html","News","Forum/News/Threads",IPADDRESS,1)
                    k[1]="Forum/News/Threads/"+threadname2+".html"
                    k[1]="Example/news.html"
                if "Movies" in path:
                    txt=replacethread(moviesexample,threadname22)
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h2><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+thread+'</h2>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    newthread.write(txt)
                    newthread.close()
                    (root,ext)=os.path.splitext(path+"/"+threadname2+"2.txt")
                    os.rename(path+"/"+threadname2+"2.txt",path+"/"+threadname2+".html")
                    updateforum("Example/movies.html","Movies","Forum/Movies/Threads",IPADDRESS,2)
                    k[1]="Forum/Movies/Threads/"+threadname2+".html"
                    k[1]="Example/movies.html"
                if "Gaming" in path:
                    txt=replacethread(gamingexample,threadname22)
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h2><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+thread+'</h2>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    newthread.write(txt)
                    newthread.close()
                    (root,ext)=os.path.splitext(path+"/"+threadname2+"2.txt")
                    os.rename(path+"/"+threadname2+"2.txt",path+"/"+threadname2+".html")
                    updateforum("Example/gaming.html","Gaming","Forum/Gaming/Threads",IPADDRESS,3)
                    k[1]="Forum/Gaming/Threads/"+threadname2+".html"
                    k[1]="Example/gaming.html"
                if "Music" in path:
                    txt=replacethread(musicexample,threadname22)
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h2><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+thread+'</h2>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    newthread.write(txt)
                    newthread.close()
                    (root,ext)=os.path.splitext(path+"/"+threadname2+"2.txt")
                    os.rename(path+"/"+threadname2+"2.txt",path+"/"+threadname2+".html")
                    updateforum("Example/music.html","Music","Forum/Music/Threads",IPADDRESS,4)
                    k[1]="Forum/Music/Threads/"+threadname2+".html"
                    k[1]="Example/music.html"
                if "Multimedia" in path:
                    txt=replacethread(multimediaexample,threadname22)
                    script=txt.find("<script></script>")
                    txt=list(txt)
                    txt1=txt[0:script]
                    txt1="".join(txt1)
                    txt2='<h2><a href="http://'+IPADDRESS+':8080/Users/'+temp+'/profile.html">'+temp+"</a>: "+thread+'</h2>'
                    txt3=txt[script:]
                    txt3="".join(txt3)
                    txt=txt1+txt2+txt3
                    newthread.write(txt)
                    newthread.close()
                    (root,ext)=os.path.splitext(path+"/"+threadname2+"2.txt")
                    os.rename(path+"/"+threadname2+"2.txt",path+"/"+threadname2+".html")
                    updateforum("Example/multimedia.html","Multimedia","Forum/Multimedia/Threads",IPADDRESS,5)
                    k[1]="Forum/Multimedia/Threads/"+threadname2+".html"
                    k[1]="Example/multimedia.html"
            else:##sending to login page with a proper message
                sendfile = open("clogin.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                client_socket.send(data)
        if "color?" in k[1]:
            color=k[1].split("?")
            color=color[1]
            username=getuser(ktxt)
            username=username.decode('base64','strict')
            changecolor(username,color,IPADDRESS)
            sendfile = open("playplay.html", 'rb')
            data=sendfile.read()
            sendfile.close()
            data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
            data=data.replace("nameeee",username+"/message.html")
            client_socket.send("HTTP/1.1 200 OK\r\n")
            client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
            client_socket.send(data)
        if "link?" in k[1]:
            link=list(k[1])
            link=link[5:]
            link="".join(link)
            print link
            request=urllib2.Request(link)
            handle=urllib2.urlopen(request)
            content=handle.read()
            username=getuser(ktxt)
            username=username.decode('base64','strict')
            f=open("Users/"+username+"/background.jpg",'wb')
            f.write(content)
            f.close()
            sendfile = open("playplay.html", 'rb')
            data=sendfile.read()
            sendfile.close()
            data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
            data=data.replace("nameeee",username+"/message.html")
            client_socket.send("HTTP/1.1 200 OK\r\n")
            client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
            client_socket.send(data)
        if "msgclear" in k[1]:
            wantedclear=k[1].split("/")
            wantedclear=wantedclear[1]
            current=getuser(ktxt)
            current=current.decode('base64','strict')
            if wantedclear==current:
                name=current
                k[1]=k[1].split("/")
                k[1]=k[1][0]+"/"+k[1][1]
                f2=open(k[1]+"/message.html",'wb')
                txt2='<!DOCTYPE html><html><style> body {background: url("background.jpg");background-size: 102%;background-repeat: no-repeat;}</style><title>Messages</title><body><html><p style="color:black; position: absolute; top: 510px; right: 100px;">instructions for uploading image for new background:</p><p style="color:black;position: absolute; top: 525px; right: 70px;">paste an image url in the text box above and click "upload"</p><textarea style="position: absolute; top: 500px; height: 20px; width: 200px; right: 200px;" rows="1" cols="50" id="textarea"></textarea><button style="position: absolute; top: 500px; height: 20px; width: 80px; right: 100px;" onclick="myFunction()">upload</button><br><select id="select" style="position: absolute; top: 450px; height: 20px; width: 70px; right: 335px;"> <option value="black">Black</option><option value="white">White</option><option value="red">Red</option><option value="green">Green</option><option value="yellow">Yellow</option></select><button style="position: absolute; top: 450px; height: 20px; width: 120px; right: 200px;" onclick="myFunction1()">Change Color</button><br><p style="color:black; position: absolute; top: 400px; right: 170px;">Change your profile font color to:</p><button style="position: absolute; top: 350px; height: 40px; width: 120px; right: 200px;" onclick="myFunction2()">Check your profile</button><button style="position: absolute; top: 300px; height: 20px; width: 120px; right: 200px;" onclick="myFunction3()">Clear messages</button><br><br></body></html><script>function myFunction() {data=document.getElementById("textarea").value\r\nwindow.open("http://'+IPADDRESS+':8080/link?"+data, "_self")}</script><script>function myFunction1() {data=document.getElementById("select").value\r\nwindow.open("http://'+IPADDRESS+':8080/color?"+data, "_self")}</script><script>function myFunction2() {window.open("http://'+IPADDRESS+':8080/Users/'+name+'/profile.html", "_self")}</script><script>function myFunction3() {window.open("http://'+IPADDRESS+':8080/Users/'+name+'/msgclear","_self")}</script><div id="home" style="position: absolute; top: 50px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IPADDRESS+':8080/playplay.html" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="7">Home &#8962 </font></span></div></a></div>'
                f2.write(txt2)
                f2.close()
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+name)
                data=data.replace("nameeee",name+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data='<script>alert("You cannot use this")</script>'+data
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                data=data.replace("nameeee",username+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
        if "/message=" in k[1]:
            if islogged(ktxt):
                k[1]=k[1].replace("Users/","")
                name=k[1].split("/")
                msg=k[1].split("message=")
                s=msg[1]
                s=urllib2.unquote(urllib2.unquote(s.encode("utf8")))
                name=name[0]
                print ("name= "+name+" msg= "+s)
                f=open("Users/"+name+"/message.html",'ab')
                user=getuser(ktxt)
                user=user.decode('base64','strict')
                f.write('<h2><a href="http://'+IPADDRESS+':8080/Users/'+user+'/profile.html">'+user+"</a>: "+s+'</h2>')
                f.close()
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+user)
                data=data.replace("nameeee",user+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:
                sendfile = open("clogin.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                client_socket.send(data)        
        if "Admin/remove/" in k[1]:
            if "admin=" in ktxt:##remove the specified username
                k[1]=k[1].replace("Admin/remove/","")
                users=open("users.txt",'rb')
                users2=open("allusernames.txt",'rb')
                data=users.read()
                data2=users2.read()
                data=data.split("U="+k[1]+"P=")
                k[1]=k[1].decode('base64','strict')
                data2=data2.split("UserName= "+k[1])
                data=data[0]+data[1]
                data2=data2[0]+data2[1]
                users=open("users.txt",'wb')
                users2=open("allusernames.txt",'wb')
                users.write(data)
                users2.write(data2)
                users.close()
                users2.close()
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("adminplayplay.html", 'rb')
                data=sendfile.read()
                data=data.replace("nameeee",username+"/message.html")
                sendfile.close()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
                shutil.rmtree("Users/"+k[1])
            else:##sending the REGULAR user to main page with a proper message
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                data=data.replace("nameeee",username+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
        if "admin/clearmsg" in k[1]:
            if "admin=" in ktxt:##clears the admin messages page
                f=open("adminmessage.html",'wb')
                f.write('<!DOCTYPE html><div id="home" style="position: absolute; top: 50px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IPADDRESS+':8080/playplay.html" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="7">Home &#8962 </font></span></div></a></div><div id="home" style="position: absolute; top: 200px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IPADDRESS+':8080/admin/clearmsg" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="4">Clear All Messages </font></span></div></a></div>')
                f.close()
                sendfile = open("adminplayplay.html", 'rb')
                data=sendfile.read()
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                data=data.replace("nameeee",username+"/message.html")
                sendfile.close()
                username=getuser(ktxt)
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:##sending the REGULAR user to main page with a proper message
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                data=data.replace("nameeee",username+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
        if "Admin/newadmin/" in k[1]:
            if "admin=" in ktxt:##making a username as a new admin
                k[1]=k[1].replace("Admin/newadmin/","")
                makeadmin(k[1])
                sendfile = open("adminplayplay.html", 'rb')
                data=sendfile.read()
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                data=data.replace("nameeee",username+"/message.html")
                sendfile.close()
                username=getuser(ktxt)
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:##sending the REGULAR user to main page with a proper message
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                data=data.replace("nameeee",username+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            
        if "Admin/Report" in k[1]:##reports a problem to the admins and set a proper message on the messages page
            if islogged(ktxt):##reportin to admin
                k[1]=k[1].replace("Admin/Report","")
                k[1]=k[1].replace("?","QSMRK")
                txt=open("adminmessage.html",'ab')
                txt.write("\r\n<html><body><p><a href=http://"+IPADDRESS+":8080/Forum"+k[1]+">"+k[1]+"</a></p></body></html>"+"\r\n")
                txt.close()
                sendfile = open("playplay.html", 'rb')
                username=getuser(ktxt)
                data=sendfile.read()
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                data=data.replace("nameeee",username+"/message.html")
                sendfile.close()
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:##sending to login page
                sendfile = open("redirect.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                client_socket.send(data)
            
        if "Admin/delete" in k[1]:
            if "admin=" in ktxt:##delete all thread on certain forum
                k[1]=k[1].replace("Admin/delete/","")
                for file in os.listdir(k[1]):
                    if file.endswith(".html") or file.endswith(".txt"):
                        os.remove(k[1]+"/"+file)
                name=k[1].split("/")
                name=name[1]
                if "Sports" in k[1]:
                    num=0
                if "News" in k[1]:
                    num=1
                if "Movies" in k[1]:
                    num=2
                if "Music" in k[1]:
                    num=4
                if "Gaming" in k[1]:
                    num=3
                if "Multimedia" in k[1]:
                    num=5
                updateforum("Example/"+name+".html",name,"Forum/"+name+"/Threads",IPADDRESS,num)
                sendfile = open("adminplayplay.html", 'rb')
                data=sendfile.read()
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                data=data.replace("nameeee",username+"/message.html")
                sendfile.close()
                username=getuser(ktxt)
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:##sending the REGULAR user to main page with a proper message
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                data=data.replace("nameeee",username+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
        if "delete/Forum" in k[1]:##deleting a specific thread
            if "admin=" in ktxt:
                k[1]=k[1].replace("delete/","")
                os.remove(k[1]+".html")
                os.remove(k[1]+".txt")
                try:
                   num=2
                   while True:
                       os.remove(k[1]+"PG"+str(num)+".html")
                       num=num+1
                except:
                    pass
                name=k[1].split("/")
                name=name[1]
                if "Sports" in k[1]:
                    num=0
                if "News" in k[1]:
                    num=1
                if "Movies" in k[1]:
                    num=2
                if "Music" in k[1]:
                    num=4
                if "Gaming" in k[1]:
                    num=3
                if "Multimedia" in k[1]:
                    num=5
                updateforum("Example/"+name+".html",name,"Forum/"+name+"/Threads",IPADDRESS,num)
                delete(IPADDRESS)
                sendfile = open("adminplayplay.html", 'rb')
                data=sendfile.read()
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                data=data.replace("nameeee",username+"/message.html")
                sendfile.close()
                username=getuser(ktxt)
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
            else:##sending the REGULAR user to main page with a proper message
                username=getuser(ktxt)
                username=username.decode('base64','strict')
                sendfile = open("playplay.html", 'rb')
                data=sendfile.read()
                sendfile.close()
                data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                data=data.replace("nameeee",username+"/message.html")
                client_socket.send("HTTP/1.1 200 OK\r\n")
                client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                client_socket.send(data)
        try:
            if (os.path.isfile(k[1])) and forbidden==False:###sending files to the user
                if ("playplay.html" in k[1]):
                    if k[1]=="playplay.html":##sending to home page with the username on the front
                        username=getuser(ktxt)
                        sendfile = open("playplay.html", 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        username=username.decode('base64','strict')
                        data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                        data=data.replace("nameeee",username+"/message.html")
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                        client_socket.send(data)
                    if k[1]=="adminplayplay.html":##sending admins to admins main page, and regular users to main page with a message
                        if "admin=" in ktxt:
                            print "blblblblbllblblblblbllblblbl"
                            username=getuser(ktxt)
                            username=username.decode('base64','strict')
                            sendfile = open("adminplayplay.html", 'rb')
                            print "blkblblblblbllajsdflkhskdsamlkfdm"
                            data=sendfile.read()
                            username=getuser(ktxt)
                            username=username.decode('base64','strict')
                            data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                            data=data.replace("nameeee",username+"/message.html")
                            sendfile.close()
                            client_socket.send("HTTP/1.1 200 OK\r\n")
                            client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                            client_socket.send(data)
                        if "username=" in ktxt:##sending the REGULAR user to main page with a proper message
                            username=getuser(ktxt)
                            username=username.decode('base64','strict')
                            sendfile = open("playplay.html", 'rb')
                            data=sendfile.read()
                            sendfile.close()
                            data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                            data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                            data=data.replace("nameeee",username+"/message.html")
                            client_socket.send("HTTP/1.1 200 OK\r\n")
                            client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                            client_socket.send(data)
                if ("message.html" in k[1]):
                    if getuser(ktxt).decode('base64','strict') in k[1]:
                        sendfile = open(k[1], 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                        client_socket.send(data)
                    if isadmin(getuser(ktxt)):
                        sendfile = open(k[1], 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                        client_socket.send(data)
                    else:
                        username=getuser(ktxt).decode('base64','strict')
                        sendfile = open("playplay.html", 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        data='<script>alert("You cant access this file")</script>'+data
                        data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                        data=data.replace("nameeee",username+"/message.html")
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                        client_socket.send(data)
                else:
                    if "admin" in k[1]:
                        if "admin=" in ktxt:##sending the proper page to admins only
                            sendfile = open(k[1], 'rb')
                            data=sendfile.read()
                            sendfile.close()
                            client_socket.send("HTTP/1.1 200 OK\r\n")
                            client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                            client_socket.send(data)
                        else:##sending the REGULAR user to main page with a proper message
                            username=getuser(ktxt)
                            username=username.decode('base64','strict')
                            sendfile = open("playplay.html", 'rb')
                            data=sendfile.read()
                            sendfile.close()
                            data='<script>alert("You wish! Access ONLY for Admins")</script>'+data
                            data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                            data=data.replace("nameeee",username+"/message.html")
                            client_socket.send("HTTP/1.1 200 OK\r\n")
                            client_socket.send("Content-length: "+str(len(data))+"\r\n\r\n")
                            client_socket.send(data)
                    else:##sending the proper page to regular users only
                        sendfile = open(k[1], 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                        client_socket.send(data)
            ##############################login and register###################
            if "P=" in k[1] and "U=" in k[1]:
                #dealing with a user that trys to login
                if "F=" not in k[1]:
                    p=k[1].find("P=")
                    username=list(k[1])[2:p]
                    username="".join(username)
                    password=list(k[1])
                    password=password[p+2:]
                    password="".join(password)
                    admin1=open("admins.txt","rb")
                    admin=admin1.read()
                    if(admin.find(username))>0:##finding out if the user is an admin
                        txt=admin
                        txt1=txt.find("U="+username)
                        admin1.close()
                        admin=True
                    else:##finding out if the user is a regular user
                        txt2=open("users.txt",'rb')
                        txt=txt2.read()
                        txt1=txt.find("U="+username)
                        txt2.close()
                        admin=False
                        admin1.close()
                    if txt1>0:##if username was found in the username pool
                        print (username+"3")
                        txt=list(txt)
                        txt=txt[txt1+2:]
                        txt="".join(txt)
                        tmp=txt.find("]")
                        txt=list(txt)
                        txt=txt[:tmp]
                        txt="".join(txt)
                        p=txt.find("P=")
                        txt=list(txt)
                        txt=txt[p+2:]
                        txt="".join(txt)
                        if txt==password:
                            c=Cookie.SimpleCookie()
                            if admin:##sending the admin to the admin home page
                                c["admin"]=username
                                username=username.decode('base64','strict')
                                sendfile = open("adminplayplay.html", 'rb')
                                data=sendfile.read()
                                data=data.replace("Welcome Admin","Welcome Admin "+username)
                                data=data.replace("nameeee",username+"/message.html")
                                sendfile.close()
                                client_socket.send("HTTP/1.1 200 OK\r\n")
                                client_socket.send("Content-length: "+str(len(data))+"\r\n"+str(c)+"\r\n\r\n")
                                client_socket.send(data)
                                
                            else:##sending to home page with the username on the front
                                c["username"]=username
                                sendfile = open("playplay.html", 'rb')
                                data=sendfile.read()
                                sendfile.close()
                                username=username.decode('base64','strict')
                                data=data.replace("Welcome To PlayPlay","Welcome To PlayPlay "+username)
                                data=data.replace("nameeee",username+"/message.html")
                                client_socket.send("HTTP/1.1 200 OK\r\n")
                                client_socket.send("Content-length: "+str(len(data))+"\r\n"+str(c)+"\r\n\r\n")
                                client_socket.send(data)
                                
                        else:##redirecting to the login page with a proper message
                            sendfile = open("clogin.html", 'rb')
                            data=sendfile.read()
                            sendfile.close()
                            data=data.replace("Login Or register","The Username or Password DOES NOT match")
                            client_socket.send("HTTP/1.1 200 OK\r\n")
                            client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                            client_socket.send(data)
                    else:##redirecting to the login page with a proper message
                        sendfile = open("clogin.html", 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        data=data.replace("Login Or register","The Username Does Not exist")
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                        client_socket.send(data)
                            
                else:#register a new user
                    p=k[1].find("U=")
                    k[1]=list(k[1])
                    k[1]=k[1][p:]
                    k[1]="".join(k[1])
                    p=k[1].find("P=")
                    username=list(k[1])[2:p]
                    username="".join(username)
                    if (isuser(username)==False):
                        writetotxt=open("users.txt",'ab')
                        u=k[1].find("U=")
                        p=k[1].find("P=")
                        tmp=k[1][u+2:p]
                        tmp=tmp.decode('base64','strict')
                        username="UserName= "+tmp
                        allusers=open("allusernames.txt",'ab')
                        allusers.write(username+"\r\n")
                        allusers.close()
                        k[1]=k[1][:u]+"["+k[1][u:]+"]"
                        writetotxt.write(k[1]+"\r\n")
                        writetotxt.close()
                        sendfile = open("home.html", 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                        client_socket.send(data)
                        createprofile(tmp,IPADDRESS)
                    else:##username is already taken
                        sendfile = open("login2.html", 'rb')
                        data=sendfile.read()
                        sendfile.close()
                        client_socket.send("HTTP/1.1 200 OK\r\n")
                        client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                        client_socket.send(data)
            else:#dealing with errors or files not found problems
                sendfile=open("404.html",'rb')
                data=sendfile.read()
                sendfile.close()
                client_socket.send("HTTP/1.1 404 Not Found\r\n")
                client_socket.send("Content-length: "+str(len(data))+'\r\n\r\n')
                client_socket.send(data)
        except IOError:##forbidden files
            client_socket.send("HTTP/1.1 403 Forbidden\r\n")
            client_socket.send("Content-length: "+str(len('403 Forbidden'))+'\r\n\r\n')
            client_socket.send("403 Forbidden")
        else:##just in case...
            client_socket.send("HTTP/1.1 500 Internal Server Error\r\n")
            client_socket.send("Content-length: "+str(len("500 Internal Server Error"))+'\r\n\r\n')
            client_socket.send("500 Internal Server Error")
    client_socket.close()


HOST = ''
PORT = 8080
#Number of threads in the pool
THREADPOOL = 50
#Queue size
QUEUESIZE= THREADPOOL * 2

#Start a new Queue object
q=Queue(QUEUESIZE)

#Each thread does this work
def doWork(name):
    print "{} started\n".format(name)
    while True:
        #pool next conncetion from the queue
        conn, addr, a=q.get()
        #Take care of clients requests
        try:
            one_client_request(conn, addr, a)
        except:
            pass
        print "Server log: Thread {} completed to serve request from: {}:{}".format(name,addr[0],str(addr[1]))
        q.task_done()
        conn.close()

#Start a pool of workers
for i in xrange(THREADPOOL):
    name="T-"+str(i)
    t=Thread(target=doWork, args=(name,))
    t.daemon=True
    t.start()


#Establish server
#The server expects that files reside in teh same direcotry it run from. There should be a file index.html in this directory and a sub directory ./pics to store and serve images
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Find a free port
while True:
    try:
        s.bind((HOST, PORT))
        break
    except Exception:
        PORT=PORT

#Start main server
s.listen(1)
print "Server log: Listening on address: {}:{}".format(HOST, PORT)
#Server's main loop
while True:
    conn, addr = s.accept()
    a=conn.recv(1024)
    print "Server log: New connection: {}:{}\n".format(addr[0],str(addr[1]))
    #Put info in queue and return to serve another client
    q.put((conn, addr, a))     
    

s.close()

