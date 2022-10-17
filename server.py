import os
from pyexpat import model
from flask import Flask, Response, request
import requests

from serverYoloCall import loadModel, predictForImage, predictForImageName

app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))


@app.before_first_request
def before_first_request():
    loadModel()

@app.route('/test',methods=['GET'])
def test():
    return Response('Test successfull', 200)    

@app.route('/image',methods=['GET'])
def getReceipts():
    name = request.args.get("name")
    if name == None:
        return Response('Please provide image name similar to this: /image?name=913_0_jpg.rf.2e6547f5d2bfe87104c6ef25f54ae86e.jpg', 501)
    result = predictForImageName(name)
    return Response(result[0], result[1] )    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)