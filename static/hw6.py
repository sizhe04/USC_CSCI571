from flask import Flask, redirect, url_for
from flask import Flask, abort, request, jsonify
from flask_cors import CORS

# app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Welcome to my Youtube channel"


# @app.route('/success/<int:score>')
# def success(score):
#     return "The person has passed and the mark is " + str(score)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The person has failed and the mark is " + str(score)    


# @app.route('/results/<int:marks>')
# def result(marks):
#     result=""
#     if (marks < 50):
#         result = 'fail'
#     else:
#         result = "success"
#     return redirect(url_for(result, score=marks))


# if __name__=='__main__':
#     app.run(debug = True)








# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # by vellhe 2017/7/9



# app = Flask(__name__)
 
 
# @app.route('/HelloWorld')
# def hello_world():
#     return "Hello World!"
 
 
# if __name__ == "__main__":
#     # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
#     app.run(debug=True)
 
# # app = Flask(__name__)
 
# # 测试数据暂时存放
# tasks = []
 
# @app.route('/add_task/', methods=['POST'])
# def add_task():
#     if not request.json or 'id' not in request.json or 'info' not in request.json:
#         abort(400)
#     task = {
#         'id': request.json['id'],
#         'info': request.json['info']
#     }
#     tasks.append(task)
#     return jsonify({'result': 'success'})
 
 
# @app.route('/get_task/', methods=['GET'])
# def get_task():
#     if not request.args or 'id' not in request.args:
#         # 没有指定id则返回全部
#         return jsonify(tasks)
#     else:
#         task_id = request.args['id']
#         task = filter(lambda t: t['id'] == int(task_id), tasks)
#         return jsonify(task) if task else jsonify({'result': 'not found'})
 
 
# if __name__ == "__main__":
#     # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
#     app.run(host="0.0.0.0", port=8383, debug=True)




from flask import Flask
from flask_cors import CORS

import requests
# r = requests.get('/discovery/v2/events.json?unit=miles&segmentId=KZFzniwnSyZfZ7v7nE&geoPoint=9q5cs&radius=10&keyword=University+of+Southern+California')
# print(r.status_code)




# payload = {'key1':'value1', 'key2': 'value2'}
# r = requests.get('https://api.github.com/events',params=payload)
# print(r.json())
# res = r.json()

ticketMatsterApi = "qNHGBwrCsREw50tqWDbzj99LyRfEJlc3"

app = Flask(__name__)
CORS(app)

 
@app.route('/')
def hello():
    return 'Hello World!'

# @app.route("/eventSearch")
# def eventSearch():
#     res = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?apikey=qNHGBwrCsREw50tqWDbzj99LyRfEJlc3")
    
#     return jsonify(res.json())


@app.route("/eventSearchNoSeg/<geoPoint>/<radius>/<keyword>")
def eventSearch_non_seg(keyword, geoPoint, radius):
    res = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?keyword="
                        + keyword + 
                        "&geoPoint=" + geoPoint + 
                        "&radius=" + radius +
                        "&unit=miles" +
                        "&apikey=" + ticketMatsterApi)
    
    return jsonify(res.json())


@app.route("/eventSearch/<geoPoint>/<radius>/<keyword>/<segmentId>")
def eventSearch_seg(keyword, geoPoint, radius, segmentId):
    res = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?keyword="
                        + keyword + 
                        "&segmentId=" + segmentId + 
                        "&geoPoint=" + geoPoint + 
                        "&radius=" + radius +
                        "&unit=miles" +
                        "&apikey=" + ticketMatsterApi)
    
    return jsonify(res.json())

@app.route("/eventDetails/<id>")
def eventDetails(id):
    res = requests.get("https://app.ticketmaster.com/discovery/v2/events/"
                        + id + "?apikey=" + ticketMatsterApi)
    
    return jsonify(res.json())


if __name__=='__main__':
    app.run(host = '0.0.0.0', port = '8888', debug = True)


