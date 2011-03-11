import web, os, sys
        
urls = (
    '/favicon.ico','favicon',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class favicon:
    def GET(self):
        return ''

class hello:
    def __init__(self):
        items = os.listdir('../')
        items = filter(lambda i: i.endswith('.txt'), items)
        items = [i[:-4] for i in items]
        self.textFiles = items
    
    def POST(self, name):
        if not name:
            return "Error!"
        else:
            return self.writeFile(name)
    
    def GET(self, name):
        if not name:
            return self.makeIndex()
        else:
            text = self.readFile(name)
            if not text: text = "Not Found"
            return text
    
    def writeFile(self, name):
        try:
            f = open("../%s.txt" % name, 'w')
        except OSError, e:
            return "Failed to open"
        content = web.input()['text']
        #return content
        try:
            f.write(content)
        except:
            return "Failed to save"
        return "Success"
    
    def readFile(self, name):
        try:
            f = open("../%s.txt" % name)
        except OSError, e:
            return False
        text = f.read()
        f.close()
        return render.page(name,text)
    
    def makeIndex(self):
        return render.index(self.textFiles)

if __name__ == "__main__":
    app.run()