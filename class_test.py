

class Monster:
    def __init__(self, name, attack_strength, attacks):
        self._name = name
        self._strength = attack_strength
        self._attacks = attacks
        self._hp = 1000

    def get_name(self):
        return self._name
    
    def hurt(self, damage):
        self._hp -= damage

    def get_hp(self):
        return self._hp


dragon = Monster("Dragon", 100, ["bite", "kill", "tail"])
dragon._name
    
