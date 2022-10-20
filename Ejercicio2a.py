import threading
import time

def trabajador():
    print(threading.current_thread().getName(), 'Starting\n')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting\n')

def mi_servicio():
    print(threading.current_thread().getName(), 'Starting\n')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Exiting\n')

s = threading.Thread(name='mi_servicio', target=mi_servicio)
h = threading.Thread(name='trabajador', target=trabajador)
h2 = threading.Thread(target=trabajador)

h.start()
h2.start()
s.start()