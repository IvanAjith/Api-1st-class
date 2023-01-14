from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc1', methods = ['GET', 'POST'])
def test1():
    if (request.method == 'POST'):
        a = request.json['Number1']
        b = request.json['Number2']
        res = a+b
        return jsonify((str(res)))

@app.route('/abc2', methods = ['GET', 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['Number1']
        b = request.json['Number2']
        res = a*b
        return jsonify((str(res)))


@app.route('/abc3', methods = ['GET', 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['Number1']
        b = request.json['Number2']
        res = a/b
        return jsonify((str(res)))


@app.route('/abc4', methods = ['GET', 'POST'])
def test4():
    if (request.method == 'POST'):
        a = request.json['Number1']
        b = request.json['Number2']
        res = a/b
        return jsonify((str(res)))

if __name__ == '__main__':
    app.run()
