from __future__ import print_function
import os
ROOT=(".\Forum\Sports\Threads",".\Forum\News\Threads",".\Forum\Music\Threads",".\Forum\Multimedia\Threads",".\Forum\Movies\Threads",".\Forum\Gaming\Threads",".\Example","./")
def replace(txt,oldip,threadname):
    txt=txt.replace(oldip,threadname)
    return txt
def temp(f,i):
    (root,ext)=os.path.splitext(f)
    os.rename(ROOT[i]+"/"+f+".txt",ROOT[i]+"/"+f+"1.txt")
def temp2(f,i):
    (root,ext)=os.path.splitext(f)
    os.rename(ROOT[i]+"/"+f+"1.txt",ROOT[i]+"/"+f+".txt")
def changeIP(oldip,newip):
    for i in range (len(ROOT)):
        for file in os.listdir(ROOT[i]):
            if file.endswith(".html"):
                x=file.split(".")
                x=x[0]
                print (x+".html- changed")
                #os.rename(ROOT[i]+"/"+x+".html",ROOT[i]+"/"+x+".txt")
                Html_file=open(ROOT[i]+"/"+x+".html","rb")
                txt=Html_file.read()
                Html_file.close()
                Html_file=open(ROOT[i]+"/"+x+".html","wb")
                txt=replace(txt,oldip,newip)
                Html_file.write(txt)
                Html_file.close()
    for file in os.listdir("./Users"):
        f1=open("Users/"+file+"/profile.html",'rb')
        txt1=f1.read()
        f1.close()
        f2=open("Users/"+file+"/message.html",'rb')
        txt2=f2.read()
        f2.close
        txt1=txt1.replace(oldip,newip)
        txt2=txt2.replace(oldip,newip)
        f1=open("Users/"+file+"/profile.html",'wb')
        f1.write(txt1)
        f1.close()
        f2=open("Users/"+file+"/message.html",'wb')
        f2.write(txt2)
        f2.close()


            
 
