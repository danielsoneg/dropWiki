#!/usr/bin/env python
# encoding: utf-8

import web
import os
import sys
import re
import json
        
urls = (
    '/favicon.ico','favicon',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class hello:
    def POST(self, name):
        if not name:
            return "Error!"
        action = web.input()['action']
        if action == 'write': return self.write(name)
        
    def write(self,name):
        content = web.input()['text']
        f = Files.getFile(name)
        status = f.write(content)
        return status
    
    def GET(self, name):
        if not name:
            return self.makeIndex()
        else:
            f = Files.getFile(name)
            content = f.read()
            return render.page(name,content)
    
    def makeIndex(self):
        return render.index(Files.items)
    
class FileModel(object):
    def __init__(self, path='../'):
        self.dir = path
        self.updateItems()
    
    def getFile(self, name):
        f = FileObject(name, self.dir, self.items)
        return f
    
    def updateItems(self):
        items = os.listdir(self.dir)
        items = filter(lambda i: i.endswith('.txt'), items)
        items = [i[:-4] for i in items]
        self.items = items

class FileObject(object):
    def __init__(self, name, sdir,items):
        """docstring for __init__"""
        self.name    = name
        self.items   = items
        self.dir     = sdir
        self.path    = "%s/%s.txt" % (self.dir, self.name)
        self.content = ""
        self.handle  = False
    
    def read(self):
        if self.name in self.items:
            self._existing()
        else:
            self._new()
        return self.content
    
    def write(self, content):
        if self.name not in self.items:
            Files.updateItems()
            self.items = Files.items
        if content == self.content:
            return self._success(self.content)
        else:
            self.content = content
            self._preSave()
            self.content = reUnlink.sub("`\\1`", self.content)
            self.handle = open(self.path,'w')
            try:
                self.handle.write(self.content)
            except OSError, e:
                return self._error("Could not write file")
            self.handle.close()
            self._addLinks()
            return self._success(self.content)
            
    def _existing(self):
        if os.path.isfile(self.path):
            self.handle = open(self.path)
            self.content = self.handle.read()
            self.handle.close()
            self._addLinks()
            self.handle.close()
        """docstring for existing"""

    def _new(self):
        self.content=""

    def _preSave(self):
        """docstring for _preSave"""
        content = self.content
        content = content.replace('<br/>', '\n')
        content = content.replace('<div><br>', '\n')
        content = content.replace('<br>', '\n')
        content = content.replace('</div><div>','\n')
        content = content.replace('<div>','\n')
        content = content.replace('</div>','')
        content = reUnspan.sub("\\1", content)
        self.content = content

    def _addLinks(self):
        self.content = reLink.sub("<a href='\\1'>\\1</a>", self.content,0)
    
    def _error(self,message):
        code = {}
        code['Code'] = 0
        code['Message'] = message
        return code
    
    def _success(self,message):
        code = {}
        code['Code'] = 1
        code['Message'] = message
        return json.dumps(code)
    

reLink   = re.compile(r'`(.*?)`', re.U)
reUnlink = re.compile(r'<a href=\".*?">(.*?)</a>', re.U)
reUnspan = re.compile(r'<span .*?>(.*?)</span>', re.MULTILINE)
Files = FileModel()

if __name__ == "__main__":
    app.run()