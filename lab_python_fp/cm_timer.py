from contextlib import contextmanager
import time

class cm_timer_1:
    def __init__(self):
        self.t = 0
        
    def __enter__(self):
        self.t = time.time()
        return 333
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time:', time.time() - self.t)

@contextmanager
def cm_timer_2():
    t = time.time()
    yield 333
    print('time:', time.time() - t)

try:
    with cm_timer_1() as cm_object:
        print(cm_object)
except:
    pass

with cm_timer_2() as cm_object:
    try:
        print(cm_object)
    except:
        pass
