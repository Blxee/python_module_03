def test_list_comps(game_data: dict):
    """Test list comps usage"""
    print("\n=== List Comprehension Examples ===")

    high_scores = [player
                   for player, data in game_data.items()
                   if data["score"] > 2000]
    print("High scorers (>2000):", high_scores)

    scores_doubled = [player["score"] * 2 for player in game_data.values()]
    print("Scores doubled:", scores_doubled)

    active_player = [player
                     for player, data in game_data.items()
                     if data["active"]]
    print("Active players:", active_player)


def test_dict_comps(game_data: dict):
    """Test dict comps usage"""
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {player: data["score"]
                     for player, data in game_data.items()}
    print("Player scores:", player_scores)

    print("Score categories:")

    achievement_counts = {
        player: len(data["achievements"]) for player, data in game_data.items()
    }
    print("Achievement counts:", achievement_counts)


def test_set_comps(game_data: dict):
    """Test set comps usage"""
    print("\n=== Set Comprehension Examples ===")

    unique_players = {player for player in game_data}
    print("Unique players:", unique_players)

    unique_achievements = {
        achievement
        for data in game_data.values()
        for achievement in data["achievements"]
    }
    print("Unique achievements:", unique_achievements)

    active_regions = {data["region"] for data in game_data.values()}
    print("Active regions:", active_regions)


def test_combined_analysis(game_data: dict):
    """Test combined comps usage"""
    print("\n=== Combined Analysis ===")
    print("Total players:", len(game_data))
    unique_achievements = {
        achievement
        for data in game_data.values()
        for achievement in data["achievements"]
    }
    print("Total unique achievements:", len(unique_achievements))
    average_score = sum(
        (data["score"] for data in game_data.values())
    ) / len(game_data)
    print("Average score:", average_score)
    (top_player_name, top_player_data) = max(
        game_data.items(), key=lambda item: item[1]["score"]
    )
    print(
        f"Top performer: {top_player_name} ({top_player_data['score']} "
        f"points, {len(top_player_data['achievements'])} achievements)"
    )


def main():
    """Main function"""
    print("=== Game Analytics Dashboard ===")

    game_data = {
        "alice": {
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": ["first_kill", "boss_slayer"],
        },
        "bob": {
            "score": 1800,
            "active": True,
            "region": "central",
            "achievements": ["level_10"],
        },
        "charlie": {
            "score": 2150,
            "active": True,
            "region": "east",
            "achievements": ["first_kill"],
        },
        "diana": {
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": ["level_10"],
        },
    }

    test_list_comps(game_data)
    test_dict_comps(game_data)
    test_set_comps(game_data)
    test_combined_analysis(game_data)


if __name__ == "__main__":
    main()
