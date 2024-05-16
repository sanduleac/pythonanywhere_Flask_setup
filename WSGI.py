import sys
#path to the source code files - change for your own location
path ='/home/sanduleac/sheet_talk'
if path not in sys.path:
    sys.path.append(path)
#change 'responder' to the name of your app
from responder import app as application
