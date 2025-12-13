if __name__ = "__main__":
    alice = {
        "sword": {
            "amount": 1,
            "price": 500,
            "type": "weapon",
            "rarity": "rare",
        },
        "potion": {
            "amount": 5,
            "price": 50,
            "type": "consumable",
            "rarity": "common",
        },
        "shield": {
            "amount": 1,
            "price": 200,
            "type": "armor",
            "rarity": "uncommon",
        },
    }

"""
$> python3 ft_inventory_system.py
=== Player Inventory System ===

=== Alice's Inventory ===
sword (weapon, rare): 1x @ 500 gold each = 500 gold
potion (consumable, common): 5x @ 50 gold each = 250 gold
shield (armor, uncommon): 1x @ 200 gold each = 200 gold

Inventory value: 950 gold
Item count: 7 items
Categories: weapon(1), consumable(5), armor(1)

=== Transaction: Alice gives Bob 2 potions ===
Transaction successful!

=== Updated Inventories ===
Alice potions: 3
Bob potions: 2

=== Inventory Analytics ===
Most valuable player: Alice (850 gold)
Most items: Alice (5 items)
Rarest items: sword, magic_ring
"""
