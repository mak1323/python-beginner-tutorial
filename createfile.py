def Main():
    words = ["cat", "hay", "goat", "roast"]

    with open("words.txt", 'w') as f:
        for word in words:
            f.write(word + "\n")

if __name__ == "__main__":
    Main()
