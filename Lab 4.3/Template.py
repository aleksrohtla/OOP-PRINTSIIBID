from abc import ABC, abstractmethod

class Creature:
    def __init__(self, attack, health):
        self.attack, self.health, self.max_health = attack, health, health

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_idx, c2_idx):
        c1, c2 = self.creatures[c1_idx], self.creatures[c2_idx]
        res2, res1 = self.hit(c1, c2), self.hit(c2, c1)
        return -1 if res1 == res2 else (c1_idx if res1 else c2_idx)

    @abstractmethod
    def hit(self, attacker, defender): pass

class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        if defender.health > 0: defender.health = defender.max_health
        return defender.health > 0

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        return defender.health > 0

if __name__ == "__main__":
    g1 = TemporaryDamageCardGame([Creature(1, 2), Creature(1, 3)])
    print(g1.combat(0, 1))

    g2 = PermanentDamageCardGame([Creature(1, 2), Creature(1, 3)])
    print(g2.combat(0, 1), g2.combat(0, 1))

    g3 = PermanentDamageCardGame([Creature(2, 2), Creature(2, 2)])
    print(g3.combat(0, 1))