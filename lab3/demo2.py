from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/info', methods=['GET','POST'])
def get_info():
    if request.method =='GET':
        return {'response': 200, 'method': 'GET'}, 200
    elif request.method == 'POST':
        data = json.loads(request.data)
        data['method']= 'POST'
        data['response']=201
        return data, 200

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=5000)
