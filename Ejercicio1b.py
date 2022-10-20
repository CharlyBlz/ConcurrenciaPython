import threading


def trabajador(num):
    """funcion del hilo"""
    print('Trabajador: %s \n' % num)


hilos = []
for i in range(5):
    h = threading.Thread(target=trabajador, args=(i,))
    hilos.append(h)
    h.start()