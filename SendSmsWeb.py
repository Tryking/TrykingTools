import os

from flask import Flask
from flask import request

from SmsSend import TwilioSmsSend
from libs.common import init_log
import logging

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/sendsms', methods=['GET'])
def send_sms():
    pwd = request.args.get('pwd')
    content = request.args.get('content')
    if pwd and content:
        sms_send = TwilioSmsSend()
        return sms_send.send_sms(content)
    else:
        return 'Params Error'


def write_file_log(msg, __module='', level='error'):
    filename = os.path.split(__file__)[1]
    if level == 'debug':
        logging.getLogger().debug('File:' + filename + ', ' + __module + ': ' + msg)
    elif level == 'warning':
        logging.getLogger().warning('File:' + filename + ', ' + __module + ': ' + msg)
    else:
        logging.getLogger().error('File:' + filename + ', ' + __module + ': ' + msg)


# debug log
def debug(self, msg, func_name=''):
    __module = "%s.%s" % (self.__module, func_name)
    self.write_file_log(msg, __module, 'debug')


# error log
def error(self, msg, func_name=''):
    __module = "%s.%s" % (self.__module, func_name)
    self.write_file_log(msg, __module, 'error')


if __name__ == '__main__':
    init_log(console_level=logging.DEBUG, file_level=logging.DEBUG,
             logfile="logs/" + os.path.split(__file__)[1].split(".")[0] + ".log")
    init_log(console_level=logging.ERROR, file_level=logging.ERROR,
             logfile="logs/" + os.path.split(__file__)[1].split(".")[0] + "_error.log")
    app.run(host='0.0.0.0', port=99999)
