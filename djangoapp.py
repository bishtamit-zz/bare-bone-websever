import sys
sys.path.insert(0, './dweb')

from dweb import wsgi

app = wsgi.application
