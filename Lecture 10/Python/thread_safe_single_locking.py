from threading import Lock

"""
Problem with this type of locking is you are acquiring lock everytime without even checking
if the lock is acquired. In distributed systems - this is contention and can cause bottleneck
in large scale appplications.
"""
class Singleton:
    _instance = None
    _lock = Lock()


    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"Are they same: {s1 == s2}")
