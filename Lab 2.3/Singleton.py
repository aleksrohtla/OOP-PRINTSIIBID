def is_singleton(factory):
    esimene = factory()
    teine = factory()
    return esimene is teine

class Kasutaja:
    pass

def loo_kasutaja():
    return Kasutaja()

print(is_singleton(loo_kasutaja))