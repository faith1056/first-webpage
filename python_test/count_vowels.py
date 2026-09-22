def count_vowels(name):
    count = 0

    for letter in name:
        if letter in "aeiou":
            count += 1

    return count


print(count_vowels("python"))
print(count_vowels("hello"))