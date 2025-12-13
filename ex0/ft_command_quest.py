if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("No arguments provided! ")
    else:
        print("Arguments received:", len(sys.argv) - 1)
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print("Program name:", sys.argv[0])

    print("Total arguments", len(sys.argv))
