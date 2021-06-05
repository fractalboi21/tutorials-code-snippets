from flask import Flask
from pywebio.output import *
from pywebio.input import *
from pywebio.platform.flask import webio_view

names = []

def name():
    for i in range(3):
        #input for pywebio
        answer = input("what is namw?",type="text")
        names.append(answer)
    
    abc = ":".join(names)
    #display html using python3
    put_text(abc)


app = Flask(__name__)
app.add_url_rule('/hello', 'webio_view', webio_view(name),
             methods=['GET', 'POST', 'OPTIONS'])

app.run(host='localhost',port=5000)
