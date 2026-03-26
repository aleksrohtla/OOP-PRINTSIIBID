class Specification:
    """Baasklass, mis defineerib reeglite struktuuri."""
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        # Võimaldab kasutada & operaatorit: spec1 & spec2
        return AndSpecification(self, other)

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class NameSpecification(Specification):
    """Lisaülesandena pakutud nime kontroll."""
    def __init__(self, name):
        self.name = name

    def is_satisfied(self, item):
        return item.name == self.name

class AndSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        # Kontrollib, kas kõik listis olevad spetsifikatsioonid on tõesed
        return all(spec.is_satisfied(item) for spec in self.specs)