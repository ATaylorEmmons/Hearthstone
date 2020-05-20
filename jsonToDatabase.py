import sqlite3
import json


from Card import Card

cardDB = sqlite3.connect("HsCards.db")

entry = cardDB.cursor()

entry.execute('''
        CREATE TABLE CARDS
        (card_id VARCHAR PRIMARY KEY, 
        card_name VARCHAR(16), 
        card_type VARCHAR(32), 
        mana INTEGER,
        attack INTEGER,
        health INTEGER,
        effect VARCHAR(32))
''')

cardDB.commit()


with open("cards.json", encoding="utf8") as cards_json:
    cardSet = json.load(cards_json)
    for card in cardSet:
        if card["type"] != "HERO":
            dataCard = Card(card)
            entry.execute('INSERT INTO CARDS VALUES (?, ?, ?, ?, ?, ?, ?)',(dataCard.id, dataCard.name, dataCard.cardType, dataCard.mana, dataCard.attack, dataCard.health, dataCard.effect))

cardDB.commit()
