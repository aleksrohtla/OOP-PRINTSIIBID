from abc import ABC, abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        """Meetod, mida kõik andmeallikad peavad realiseerima."""
        pass
-
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child)
        :self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

        def find_all_children_of(self, name):
        """Realiseerime abstraktsioonis nõutud meetodi."""
        for p, rel, child in self.relations:
            if p.name == name and rel == Relationship.PARENT:
                yield child.name

class Research:

    def __init__(self, browser: RelationshipBrowser):
        for child in browser.find_all_children_of("John"):
            print(f"Johnil on laps nimega {child}.")

if __name__ == "__main__":
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')     