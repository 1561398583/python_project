from flask import Flask
from flask import render_template
import time
from flask import jsonify

import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wddlzh123 :wddlmm123@Mysql@rm-wz96qo32w042vtyf2bo.mysql.rds.aliyuncs.com:3306/video_info'
#db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/get_time')
def getTime():
    return time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())

@app.route('/get_total')
def getTotal():
    data = {
        "ensure" : 12345,
        "suspected" : 1000,
        "cure" : 5000,
        "death" : 1000
    }
    return jsonify(data)

@app.route('/get_left1')
def getLeft1():
    data = [0] * 6
    for i in range(0, 6):
        data[i] = random.randint(0, 40)

    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run()