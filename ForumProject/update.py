def updateforum(update,name,path,IP, num):
    #b=["<style> body {background: url('sports.jpg');background-size: 113%;background-repeat: no-repeat;}</style>","<style> body {background: url('news.jpg');background-size: 90%;background-repeat: no-repeat;background-position: 50px -45px; }</style>","<style> body {background: url('movies.jpg');background-size: 90%;background-repeat: no-repeat;}</style>","<style> body {background: url('gaming.jpg');background-size: 102%;background-repeat: no-repeat;}</style>","<style> body {background: url('music.jpg');background-size: 90%;background-repeat: no-repeat;}</style>","<style> body {background: url('multimedia.jpg');background-size: 90%;background-repeat: no-repeat;}</style>"]
    update=open(update,'wb')
    txt=("<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<title>"+name+"</title>\r\n<h1>"+name+" Forum</h1>\r\n</head>\r\n<body>\r\n")
    for file in os.listdir(path):
        if file.endswith(".html"):
            f=file
            f=f.split(".")
            f=f[0]
            f2=f.replace("%20"," ")
            txt=txt+"<p>\r\n<a href=http://"+IP+":8080/"+path+"/"+f+".html>"+f2+"</a>\r\n</p>"
    txt=txt+"</body>\r\n</html>\r\n\r\n<html>\r\n<body>\r\n<button onclick='myFunction()'"+">New Thread</button><br>\r\n</body>\r\n</html>\r\n\r\n<script>\r\nfunction myFunction() {\r\n	window.open('http://"+IP+":8080/Example/"+name+"newthread.html', '_self')\r\n}\r\n</script>"
    update.write(txt)
    update.close()
