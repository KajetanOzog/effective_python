from threading import Thread, Lock
import time

lock_a = Lock()
lock_b = Lock()

def thread_a():
    while True:
        time.sleep(1)
        if lock_a.acquire(timeout=10):
            time.sleep(1)
            print("Thread A: Acquired Lock A")
            if lock_b.acquire(timeout=10):
                print("Thread A: Acquired Lock B")
                # Sekcja krytyczna
                lock_b.release()
            lock_a.release()
        else:
            print("Thread A: Ustępuję zasobu")

def thread_b():
    while True:
        time.sleep(1)
        if lock_b.acquire(timeout=10):
            time.sleep(1)
            print("Thread B: Acquired Lock B")
            if lock_a.acquire(timeout=10):
                print("Thread B: Acquired Lock A")
                # Sekcja krytyczna
                lock_a.release()
            lock_b.release()
        else:
            print("Thread B: Ustępuję zasobu")

# Startujemy dwa wątki
Thread(target=thread_a, daemon=True).start()
Thread(target=thread_b, daemon=True).start()

time.sleep(500)