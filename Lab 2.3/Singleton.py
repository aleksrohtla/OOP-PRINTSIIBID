def is_singleton(factory):
    objekt1 = factory()
    objekt2 = factory()
    return objekt1 is objekt2

class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def loo_andmebaas():
    return Database()

print(is_singleton(loo_andmebaas))