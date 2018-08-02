#!/home/tops/bin/python3
# -*- coding;utf-8 -*-
from flask import Flask, request, url_for, render_template, make_response, flash, redirect
import json
from werkzeug.utils import secure_filename
#from log_conf import setup_logging
import logging

app = Flask(__name__)        #实例化Flask类成为WSGI应用
app.config['SECRET_KEY'] = '123456'
# setup_logging()
# logger = logging.getLogger()
# my_module = logging.getLogger('my_module')

# logger.info('sdfjjf')
# my_module.error('111111111111111');                #为啥会打印两次

@app.route('/', methods = ['GET'])
def hello_world():
  #return 'hello,world!'
  resp = make_response(render_template('index.html', name = 'ff'))
  resp.set_cookie('username', 'wfj')
  return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    methods = request.method
    username = request.cookies.get('username')
    print(methods, username)
    #logger.debug(methods)
    return 'http methods:' + methods

@app.route('/upfile', methods=['POST'])
def upfile():
  ret = {'message': '', 'code': 200, 'data': ''}
  if 'file' in request.files:
    flash('file')                #消息闪现
    f = request.files['file']
    f.save('./uploads/' + secure_filename(f.filename))
  if 'img' in request.files:
    flash('img')
    img = request.files['img']
    img.save('./uploads/images/' + secure_filename(img.filename))  
  return redirect('/')  
  #return make_response(json.dumps(ret), 200)


with app.test_request_context('/?name=wfj'):
    print(url_for('hello_world', name = 'fj'))
    assert request.args.get('name') == 'wfj'

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = '5004', debug = True)

from flask import Flask, url_for, request, render_template
app = Flask(__name__)              #实例化Flask类，成为WSGI应用，第一个参数是应用模块或者包的名称

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    print(request.method)        #GET,POST 
    #return 'Hello, World!' 
    return render_template('index.html')

with app.test_request_context('/?name=wfj'):        #激活一个临时的请求上下文
    print(url_for('hello_world', name = 'wfj'))
    assert request.path == '/'                       #断言测试
    assert request.args['name'] == 'wfj'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5004', debug = True)
