from threading import Lock, Thread

class Singleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        # First check (No locking yet, for performance)
        if cls._instance is None:
            # Now we lock to ensure only one thread enters the creation block
            with cls._lock:
                # Because another thread might have finished while we waited for the lock
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    def create_singleton():
        s = Singleton()
        print(f"Instance ID: {id(s)}")
    
    # Simulating high-volume concurrent access
    threads = []
    for _ in range(10):
        t = Thread(target=create_singleton)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
