import threading
import time
import logging


def trabajador():
    logging.debug("Starting\n")
    time.sleep(0.2)
    logging.debug("Exiting\n")


def mi_servicio():
    logging.debug("Starting\n")
    time.sleep(0.3)
    logging.debug("Exiting\n")

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s\n',
)

s = threading.Thread(name='mi_servicio', target=mi_servicio)
h = threading.Thread(name='trabajador', target=trabajador)
h2 = threading.Thread(target=trabajador)

h.start()
h2.start()
s.start()