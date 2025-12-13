from sys import argv
from math import sqrt

def parse_coords(s: str) -> tuple:
    try:
        x, y, z = s.split(",")
        return (int(x), int(y), int(z))
    except Exception as e:
        e_type = e.__class__.__name__
        e_args = e.args
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {e_type}, Args: {e_args}")

def find_distance(pos1: tuple, pos2: tuple) -> None:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    dist: float = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    print(f"Distance between {pos1} and {pos2}: {dist:.2f} ");


if __name__ == "__main__":
    SPAWN_COORDS = (0, 0, 0)

    coords1 = (10, 20, 5)
    print("Position created:", coords1)
    find_distance(SPAWN_COORDS, coords1)

    coords2_str = "3,4,0"
    print(f"\nParsing coordinates: \"{coords2_str}\"")
    coords2 = parse_coords(coords2_str)
    print("Parsed position:", coords2)
    find_distance(SPAWN_COORDS, coords2)

    coords3_str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{coords3_str}\"")
    parse_coords(coords3_str)

    print("\nUnpacking demonstration:")
    x, y, z = coords2
    print(f"Player at {x=}, {y=}, {z=}")
    X, Y, Z = coords2
    print(f"Coordinates: {X=}, {Y=}, {Z=}")
