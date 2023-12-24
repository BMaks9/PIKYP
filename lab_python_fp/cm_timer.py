import time
from contextlib import contextmanager

class cm_timer_1():
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f'time: {elapsed_time} seconds')

@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'time: {end - start} seconds')
def main():
    with  cm_timer_1():
        time.sleep(5.5)

    with  cm_timer_2():
        time.sleep(5.5)
if __name__ == '__main__':
    main()