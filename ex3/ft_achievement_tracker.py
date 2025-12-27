def main():
    """Main function"""
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    unique = alice | bob | charlie
    print("All unique achievements:", unique)
    print("Total unique achievements:", len(unique))

    common = alice & bob & charlie
    print("\nCommon to all players:", common)
    rare = unique - (alice & bob) - (alice & charlie) - (bob & charlie)
    print("Rare achievements (1 player):", rare)

    common = alice & bob
    print("\nAlice vs Bob common:", common)
    alice_unique = alice - bob
    print("Alice unique:", alice_unique)
    bob_unique = bob - alice
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    main()
