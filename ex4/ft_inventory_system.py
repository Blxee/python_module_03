def print_inventory(inventory: dict) -> None:
    """Show the contenct of the gived inventory"""
    value = 0
    count = 0
    categories = {}
    for key, item in inventory.items():
        if key == "username":
            continue

        print(
            f"{key} ({item['type']}, {item['rarity']}): "
            "{item['amount']}x @ {item['price']} gold each"
            " = {item['amount'] * item['price']} gold"
        )

        value += item["price"] * item["amount"]
        count += item["amount"]
        if item["type"] in categories:
            categories[item["type"]] += item["amount"]
        else:
            categories[item["type"]] = item["amount"]

    print(f"\nInventory value: {value} gold")
    print(f"Item count: {count} items")
    print("Categories: ", end="")

    categories = (f"{type}({count})" for type, count in categories.items())
    print(", ".join(categories))


def trade_items(inv1: dict, inv2: dict, item: str, amount: int) -> None:
    """Give arbitrary amount of items from inventory to another"""
    print(
        f"=== Transaction: {inv1['username']} "
        "gives {inv2['username']} {amount} {item}s ==="
    )

    if item in inv1 and inv1[item]["amount"] >= amount:
        if item in inv2:
            inv2[item]["amount"] += amount
        else:
            inv2[item] = inv1[item].copy()
            inv2[item]["amount"] = amount

        inv1[item]["amount"] -= amount
        if inv1[item]["amount"] == 0:
            del inv1[item]

        print("Transaction successful!\n")
        print("=== Updated Inventories ===")
        print(f"{inv1['username']} {item}s: {inv1[item]['amount']}")
        print(f"{inv2['username']} {item}s: {inv2[item]['amount']}")

    else:
        print("Transaction failed!")


def print_inventory_analytics(inventories: list[dict]) -> None:
    """Show inventory stats"""
    print("=== Inventory Analytics ===")

    max_value: tuple = ()
    max_items: tuple = ()
    rarest_items: list = []

    for inventory in inventories:
        value = 0
        items = 0

        for key, item in inventory.items():
            if key == "username":
                continue
            value += item["price"] * item["amount"]
            items += item["amount"]
            if item["rarity"] == "rare":
                rarest_items.append(key)

        if not max_value or value > max_value[1]:
            max_value = (inventory["username"], value)
        if not max_items or items > max_items[1]:
            max_items = (inventory["username"], items)

    print(f"Most valuable player: {max_value[0]} ({max_value[1]} gold)")
    print(f"Most items: {max_items[0]} ({max_items[1]} items)")
    print("Rarest items:", ", ".join(rarest_items))


def main():
    """Main function"""
    alice = {
        "username": "Alice",
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

    bob = {
        "username": "Bob",
        "magic_ring": {
            "amount": 1,
            "price": 400,
            "type": "accessory",
            "rarity": "rare",
        },
    }

    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")
    print_inventory(alice)
    print()
    trade_items(alice, bob, "potion", 2)
    print()
    print_inventory_analytics([alice, bob])


if __name__ == "__main__":
    main()
