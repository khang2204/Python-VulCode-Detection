"""
workflow worker daemon
"""
import json
import traceback
from pprint import pformat
import signal
from time import sleep, time
import pika
from tornado.escape import json_decode
from pyoko.conf import settings
from pyoko.lib.utils import get_object_from_path
from zengine.client_queue import ClientQueue, BLOCKING_MQ_PARAMS
from zengine.engine import ZEngine
from zengine.current import Current
from zengine.lib.cache import Session, KeepAlive
from zengine.lib.exceptions import HTTPError
from zengine.log import log
import sys
from zengine.receivers import *
sys._zops_wf_state_log = ''
wf_engine = ZEngine()
LOGIN_REQUIRED_MESSAGE = {'error': 'Login required', 'code': 401}
"""
    Workflow runner worker object
    """
INPUT_QUEUE_NAME = 'in_queue'
INPUT_EXCHANGE = 'input_exc'
def __init__(self):...
self.connect()
signal.signal(signal.SIGTERM, self.exit)
log.info('Worker starting')
def exit(self, signal=None, frame=None):...
"""docstring"""
self.input_channel.close()
self.client_queue.close()
self.connection.close()
log.info('Worker exiting')
sys.exit(0)
def connect(self):...
"""docstring"""
self.connection = pika.BlockingConnection(BLOCKING_MQ_PARAMS)
self.client_queue = ClientQueue()
self.input_channel = self.connection.channel()
self.input_channel.exchange_declare(exchange=self.INPUT_EXCHANGE, type=
    'topic', durable=True)
self.input_channel.queue_declare(queue=self.INPUT_QUEUE_NAME)
self.input_channel.queue_bind(exchange=self.INPUT_EXCHANGE, queue=self.
    INPUT_QUEUE_NAME)
log.info("Bind to queue named '%s' queue with exchange '%s'" % (self.
    INPUT_QUEUE_NAME, self.INPUT_EXCHANGE))
def run(self):...
"""docstring"""
self.input_channel.basic_consume(self.handle_message, queue=self.
    INPUT_QUEUE_NAME, no_ack=True)
self.input_channel.start_consuming()
log.info(' Exiting')
def _prepare_error_msg(self, msg):...
self.exit()
return msg + '\n\n' + 'INPUT DATA: %s\n\n' % pformat(self.current.input
    ) + 'OUTPUT DATA: %s\n\n' % pformat(self.current.output
    ) + sys._zops_wf_state_log
return msg
def _handle_ping_pong(self, data, session):...
still_alive = KeepAlive(sess_id=session.sess_id).update_or_expire_session()
msg = {'msg': 'pong'}
if not still_alive:
msg.update(LOGIN_REQUIRED_MESSAGE)
return msg
