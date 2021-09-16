import time

d = {"dsadad": 322323}
lol = f'start procce - {d}'

print(lol)

time1 = time.time()

time.sleep(1)

time2 = time.time()


def timing(f):
    def wrap(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (end - start) * 1000.0))

        return ret
    return wrap

@timing
def lol():
    time.sleep(1)

lol()