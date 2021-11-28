from __future__ import print_function
import os
def delete(IP):
    newtxt=""
    names=("Sports", "News", "Music", "Multimedia", "Movies", "Gaming")
    ROOT=(".\Forum\Sports\Threads",".\Forum\News\Threads",".\Forum\Music\Threads",".\Forum\Multimedia\Threads",".\Forum\Movies\Threads",".\Forum\Gaming\Threads")
    ROOT2=("Forum/Sports/Threads","Forum/News/Threads","Forum/Music/Threads","Forum/Multimedia/Threads","Forum/Movies/Threads","Forum/Gaming/Threads")
    newtxt=newtxt+"<!DOCTYPE html><title>All Threads</title><html><body><head>"
    for i in range (len(ROOT)):
        newtxt=newtxt+"<h3>"+names[i]+":</h3>"
        for file in os.listdir(ROOT[i]):
            if file.endswith(".txt"):
                tmp2=file.split(".")
                newtxt=newtxt+tmp2[0]+"<br>"
        newtxt=newtxt+"<textarea rows='1' cols='50' id='"+names[i]+"'></textarea><br><button type='button' onclick='myFunction"+str(i)+"()'>Delete Thread</button>"
    newtxt=newtxt+"</head></body></html>"
    for i in range(len(ROOT)):
        newtxt=newtxt+"<script>function myFunction"+str(i)+"() {window.open('http://"+IP+":8080/delete/"+ROOT2[i]+"/'+document.getElementById("+'"'+names[i]+'"'+").value,'_self')}</script>"
    newtxt=newtxt+'</script><div id="home" style="position: absolute; top: 50px; height: 100px; width: 250px; right: 100px;"><a href="http://'+IP+':8080/playplay.html" target="_self" id="home" class="s11link"><span id="home"><font color="black"; size="7">Home &#8962 </font></span></div></a></div>'
    Html_file=open("adminthreads.html","wb")
    Html_file.write(newtxt)
    Html_file.close()
