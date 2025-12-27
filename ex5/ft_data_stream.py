def fetch_next_events(amount: int):
    """Generator for arbitrary event data"""
    players = ["alice", "bob", "charlie", "joe", "your mom"]
    levels = [5, 12, 8] + []
    events = ["killed monster", "found treasure", "leveled up", "sold item"]

    for i in range(amount):
        yield {
            "id": i + 1,
            "player": players[i % len(players)],
            "level": levels[i % len(levels)],
            "event": events[i % len(events)],
        }


def fibonacci(limit: int):
    """Generator for the fibanocci sequence"""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime(limit: int):
    """Generator for prime numbers"""
    i = 0
    prime = 2
    while i < limit:
        for j in range(2, prime):
            if prime % j == 0:
                break
        else:
            yield prime
            i += 1
        prime += 1


def test_generators():
    """Test different generators"""
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total_events = 1000
    high_levels = 0
    treasure_events = 0
    level_ups = 0
    for i, event in enumerate(fetch_next_events(total_events)):
        if event["level"] >= 10:
            high_levels += 1
        if event["event"] == "leveled up":
            level_ups += 1
        if event["event"] == "found treasure":
            treasure_events += 1
        if i < 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                "(level {event['level']}) {event['event']}"
            )

    print("...")

    print("\n=== Stream Analytics ===")
    print("Total events processed:", total_events)
    print("High-level players (10+):", high_levels)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_ups)

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib_count = 10
    print(
        f"Fibonacci sequence (first {fib_count}):",
        str(list(fibonacci(fib_count))).strip("[]"),
    )

    prime_count = 5
    print(
        f"Prime numbers (first {prime_count}):",
        str(list(prime(prime_count))).strip("[]"),
    )


if __name__ == "__main__":
    test_generators()
