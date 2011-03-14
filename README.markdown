dropWiki: The DropBox Wiki
================
A web.py-based python server for editing, linking, and displaying plain-text files. Built to be self-sufficient - can be run on any system with at least Python 2.5 installed.
Designed as a light, easy, platform-agnostic way to create and link between notes. 
Use it with Dropbox for a text-based  document repository that can be synced and read anywhere by anything.

Requirements
------------
* Python 2.6 or better or Python 2.5 and simplejson
* A browser that supports ContentEditable (I've tested with Chrome Dev. Caveat User.)

Installation
------------
1. Drop the dbWiki folder inside a folder containing text files.
2. Run: `python dbWiki.py`
3. open [http://localhost:8080](http://localhost:8080)

Configuration
-------------
There is none. There probably will be later.

Usage
-----
Currently, the script is extremely limited: It hosts text files from the parent directory.

* To access a file named "Hello World.txt", go to [http://localhost:8080/Hello World](http://localhost:8080/Hello World)
* To edit a file, just go to its page, click on the page text, and edit. The content is saved whenever the text loses focus.
* To create a file, just go to a new page.
* To link to a file, use: ```Name of the page```.

Credits
-------
Uses web.py by Aaron Swartz