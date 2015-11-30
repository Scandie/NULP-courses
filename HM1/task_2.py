def most_frequent_letter(string):
    string = string.lower()
    string = filter(str.isalpha, string)
    string = sorted(string)
    most_frequent = string[0]
    for letter in string[1:]:
        if string.count(letter) > string.count(most_frequent):
            most_frequent = letter
    return most_frequent
