# -*- coding: utf-8 -*-
# Download the helper library from https://www.twilio.com/docs/python/install
import logging
import os

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from libs.common import init_log, get_current_func_name


class TwilioSmsSend:
    def __init__(self):
        self.__module = self.__class__.__name__
        init_log(console_level=logging.DEBUG, file_level=logging.DEBUG,
                 logfile="logs/" + os.path.split(__file__)[1].split(".")[0] + ".log")
        init_log(console_level=logging.ERROR, file_level=logging.ERROR,
                 logfile="logs/" + os.path.split(__file__)[1].split(".")[0] + "_error.log")

    def send_sms(self, content):
        # tail 11 - 11  8808 - 5
        # Your Account Sid and Auth Token from twilio.com/console
        account_sid = 'AC175d21f084e6b3884a1cd64b1e36d41d'
        auth_token = '438014c532126d6b79688bd6df8fc111'
        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=content,
                from_='(938)888-8876 ',
                to='+8615705188808'
            )
            return message.status
        except Exception as e:
            self.error(str(e), get_current_func_name())
            return 'fail'

    @staticmethod
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
