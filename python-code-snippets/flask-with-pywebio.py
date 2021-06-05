from flask import Flask, send_from_directory
from pywebio import STATIC_PATH
from pywebio.output import *
from pywebio.input import *
from pywebio.platform.flask import webio_view

names = []

def name():
    for i in range(3):
        answer = input("what is namw?",type="text")
        names.append(answer)
    
    abc = ":".join(names)
    put_text(abc)


app = Flask(__name__)
app.add_url_rule('/hello', 'webio_view', webio_view(name),
             methods=['GET', 'POST', 'OPTIONS'])

app.run(host='localhost',port=5000)
