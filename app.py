'''
This module is the application of blockable-qiita.
'''

from urllib.request import urlopen
import json
from flask import Flask, Response, render_template
from lib.feed import Feed
from lib.filter import UserNameBlackListFilter

APP = Flask(__name__)


@APP.route("/")
def index():
    '''This method is endpoint of this application.
    '''
    return render_template('index.html')


@APP.route("/feeds/<int:page>")
def feeds(page):
    '''This method get feed items from qiita api and return json to this application ajax.
    :type  page: int
    :param page: number of page
    :rtype:   Response
    :return:  WISG Response with json body
    '''
    data = json.loads(urlopen("https://qiita.com/api/v1/items?page="+str(page)).read().decode())
    feed = Feed(data)
    user_name_black_list_filter = UserNameBlackListFilter(feed)
    filtered_data = user_name_black_list_filter.filtering()
    return Response(json.dumps(filtered_data), content_type="application/json")


if __name__ == '__main__' :
    APP.run(host='0.0.0.0', port=5000)
