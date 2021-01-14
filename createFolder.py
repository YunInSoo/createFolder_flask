# -*- coding: utf-8 -*- 
from flask import Flask, request, jsonify
import random
import string
import os
import shutil

# UPLOAD_FOLDER를 이용해서 경로를 변경할수도있습니다.
UPLOAD_FOLDER = 'pre_data/'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

@app.route("/folder", methods=['GET'])
def createFolderTest():
    print(''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(8)))
    folderName = ''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(8))
    createFolder(app.config['UPLOAD_FOLDER'] + folderName)
    
    return "Create " + folderName + " File!!"
    
@app.route("/folder", methods=['DELETE'])
def delecteFolder():
    filename = request.form.get('filename') #json 데이터를 받아옴

    shutil.rmtree(app.config['UPLOAD_FOLDER'] + filename) #하위 파일까지 삭제
    return "Delecte " + filename + " File!!"

# flask 실행 
if __name__ == '__main__':
	
    app.run(host='0.0.0.0')