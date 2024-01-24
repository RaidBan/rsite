import mammoth
from flask import Flask, Response, render_template
from flask_restful import Api, Resource, request, reqparse

style_map = """
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
"""


def tohtml(name):
    print(name)
    print("asd")
    name = name.split(".")
    try:
        named = name[0] + ".docx"
        f = open(named, 'rb')
    except:
        named = name[0] + ".doc"
        f = open(named, 'rb')
    nameh = name[0] + ".html"
    b = open(f'templates/{nameh}', 'wb')
    document = mammoth.convert_to_html(f, style_map=style_map, include_default_style_map=False)
    b.write(document.value.encode('utf8'))
    f.close()
    b.close()
    return nameh


app = Flask(__name__)
api = Api()


@app.route("/rasp/<n>")
def index(n):
    asd = tohtml(n)
    return render_template(asd)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="192.168.0.21")