while True:
    enter = input("Please type a sentence: ")
    print("a e i o u")
    print(*map(enter.lower().count, "aeiou"))

