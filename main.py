import mammoth
from flask import Flask, render_template, Response
from flask_restful import Api
from os import listdir
import re

style_map = """
<style>
table {
   border-collapse: collapse;
   border: 1px solid grey;
   margin-left: auto;
   margin-right: auto;
   width: 6em;
}
td {
   border: 1px solid grey;
}
p{
   text-align: center;
}
</style>
"""


def rasp():
    ls = listdir('C:/rasp')
    lw = []
    uri = ""
    for j in ls:
        a = re.search(r'docx$', j)
        if a != None:
            b = j.split('.')
            lw.append(b[0])
    for i in lw:
        url = f"<a href=\"/rasp/{i}\">{i}</a><br>"
        uri += url
    return uri


def tohtml(name):
    name = name.split(".")
    try:
        named = name[0] + ".docx"
        f = open(f"C:/rasp/{named}", 'rb')
    except:
        named = name[0] + ".doc"
        f = open(f"C:/rasp/{named}", 'rb')
    nameh = name[0] + ".html"
    b = open(f'templates/{nameh}', 'wb')
    document = mammoth.convert_to_html(f)
    b.write(style_map.encode('utf8'))
    b.write(document.value.encode('utf8'))
    f.close()
    b.close()
    # print(nameh)
    return nameh


app = Flask(__name__)
api = Api()


@app.route("/rasp")
def indexs():
    return rasp()


@app.route("/rasp/<n>")
def index(n):
    try:
       asd = tohtml(n)
       return render_template(asd)
    except:
       return Response("Данного файла не существует", status=400)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
