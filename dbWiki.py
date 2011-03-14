#!/usr/bin/env python
# encoding: utf-8

import web
try: import simplejson as json
except ImportError: import json
import files

urls = (
    '/(.*)', 'dropWiki'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class dropWiki:
    def __preflight(self, name):
        """docstring for __preflight"""
        name = name.replace('%20',' ')
        return name
    
    #POST actions - all return JSON
    def POST(self, name):
        if not name:
            raise web.internalerror('500 Invalid Request')
        name = self.__preflight(name)
        try: 
            action = web.input()['action']
        except:
            raise web.internalerror('500 No Action Specified')            
        if hasattr(self, action):
            return getattr(self, action)(name)
        raise web.internalerror('500 Invalid Action')

    def write(self,name):
        content = web.input()['text']
        f = Files.getFile(name)
        if name not in Files.items:
            Files.updateItems()
        status = f.write(content)
        return status
    
    def rename(self,name):
        newName = web.input()['name']
        f = Files.getFile(name)
        status = f.rename(newName)
        Files.updateItems()
        return status
    
    #GET actions
    def GET(self, name):
        if not name:
            return self.makeIndex()
        name = self.__preflight(name)
        f = Files.getFile(name)
        content = f.read()
        return render.page(name,content)
    
    def makeIndex(self):
        Files.updateItems()
        return render.index(Files.items)

Files = files.FileModel()

if __name__ == "__main__":
    app.run()