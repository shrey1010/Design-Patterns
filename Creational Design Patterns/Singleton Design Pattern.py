class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance  is None:
            print("Creating new instance")
            cls._instance = object.__new__(cls)
        else:
            print("Using existing instance")
        return cls._instance
    
# Example usage
singleton1 = Singleton()
singleton2 = Singleton()