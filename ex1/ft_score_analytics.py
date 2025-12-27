import sys


def main():
    """Main function"""
    scores = sys.argv[1:]

    print("=== Player Score Analytics ===")

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        try:
            i = 0
            while i < len(scores):
                scores[i] = int(scores[i])
                i += 1
            print("Scores processed:", scores)
            print("Total players:", len(scores))
            print("Total score:", sum(scores))
            print("Average score:", sum(scores) / len(scores))
            print("High score:", max(scores))
            print("Low score:", min(scores))
            print("Score range:", max(scores) - min(scores))
        except ValueError:
            print("You are very naughty..")


if __name__ == "__main__":
    main()
