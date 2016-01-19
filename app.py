from urllib.request import urlopen
import json
from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/feeds/<int:page>")
def feeds(page):
    data = json.loads(urlopen("https://qiita.com/api/v1/items?page="+str(page)).read().decode())
    filtered_data = [post for post in data if post['user']['url_name'] not in ['HirofumiYashima']]
    return Response(json.dumps(filtered_data), content_type="application/json")

if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000, debug=True)
