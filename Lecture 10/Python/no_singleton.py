class Singleton:
    def __init__(self):
        print("Object created")



if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"Are they same: {s1 == s2}")