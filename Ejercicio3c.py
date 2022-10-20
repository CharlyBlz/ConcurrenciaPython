import threading
import time
import logging


def demonio():
    logging.debug('Starting\n')
    time.sleep(0.2)
    logging.debug('Exiting\n')


def no_demonio():
    logging.debug('Starting\n')
    logging.debug('Exiting\n')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s\n',
)

d = threading.Thread(name='daemon', target=demonio, daemon=True)
h = threading.Thread(name='non-daemon', target=no_demonio)
d.start()
h.start()

d.join(0.1)
print('d.isAlive()', d.is_alive())
h.join()