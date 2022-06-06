from threading import Lock
from collections import namedtuple
from os import getenv
from flask import Flask

app = Flask(__name__)
lock = Lock()
counter = 0
ApplicationStatus
app_status = ApplicationStatus(healthy=bool(getenv()))
with lock:
    counter +=1
if not app_status.healthy and counter > 5:
    raise Exception
\
    app.run(host)


