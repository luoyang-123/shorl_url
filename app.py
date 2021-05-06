from flask import Flask, render_template, request, jsonify, redirect
from utils import base62_decode, base62_encode
from db import get_buohao_index, add_url, get_long_url

app = Flask(__name__)
toekn,index=0,0

@app.route('/', methods=['POST', 'GET'])
def index():
    global toekn,index
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form['url']
        if toekn==0:
            index = get_buohao_index()
            toekn=index-100
        if toekn==index:
            index = get_buohao_index()
            print(index)
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
