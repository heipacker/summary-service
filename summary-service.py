# coding:utf-8
from flask import Flask, jsonify
from flask import request
from snownlp import SnowNLP

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/api/v1.0/summary', methods=['POST'])
def index():
    if not request.json or not 'text' in request.json:
        return jsonify({'code': 1}), 400
    text = request.json['text']

    s = SnowNLP(text)
    # 计算这段话的摘要（本质上是对这段话中的每个句子计算其重要程度，利用的是TextRank算法）
    return jsonify({'code': 0, 'data': s.summary(3)[0] + ',' + s.summary(3)[1] + ',' + s.summary(3)[2]}), 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=False)
