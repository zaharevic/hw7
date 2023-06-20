def find_vowels_conut(word):
    count = 0
    for i in range(0,len(word)):
        if word[i] in vowels:
            count += 1
    return count

vowels = "уеыаоэяиюё"
words = input().lower().split()
vowels_count = set(map(find_vowels_conut, words))
print(vowels_count)
if(len(vowels_count) == 1) and (vowels_count != {0}):
    print('Парам пам-пам')
else:
    print("Пам парам")
