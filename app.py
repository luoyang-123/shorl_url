from flask import Flask, render_template, request, jsonify, redirect
from utils import base62_decode, base62_encode
from db import get_buohao_index, add_url, get_long_url

app = Flask(__name__)
index_1,toekn=0,0
@app.route('/', methods=['POST', 'GET'])
def index():
    global toekn,index_1
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if index_1 == toekn:
            print(1)
            index_1 = get_buohao_index()
            toekn=index_1-100
        url = request.form['url']
        toekn+=1
        token = base62_encode(toekn)
        add_url(url, token)
        short_url = 'http://127.0.0.1:8002/{token}'.format(token=token)
        return jsonify({'short_url': short_url})

@app.route('/<token>')
def long_url(token):
    long_url = get_long_url(token)
    return redirect(long_url)


if __name__ == '__main__':
    app.run(port=8002, threaded=False)
