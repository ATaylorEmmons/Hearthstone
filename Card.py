class Card:
    id = None
    name = None
    cardType = None
    mana = None
    attack = None
    health = None
    effect = None

    def __init__(self, card):
        self.id = card["id"]
        self.name = card["name"]
        self.cardType = card["type"]
        self.mana = card["cost"]
        
        if("attack" in card):
            self.attack = card["attack"]
        if("health" in card):
            self.health = card["health"]
        if("text" in card):
            self.effect = card["text"]

    def Print(self):
        print(self.name)
        print("_____________")
        print(self.mana)
        print(self.attack)
        print(self.health)
        print(self.effect)
        print("-------------")