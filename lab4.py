def unique_letters(word1, word2):
    set1 = set(word1)
    set2 = set(word2)

    print(word1)
    print(set1)
    unique_in_word1 = set1 - set2
    unique_in_word2 = set2 - set1


    result = ''.join(sorted(unique_in_word1.union(unique_in_word2)))
    print("Літери, які є тільки в одному з двох слів:", " ".join(result))


def count_vowels_consonants(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    consonants = set('abcdefghijklmnopqrstuvwxyz') - vowels

    vowel_count = 0  #
    consonant_count = 0

    text_lower = text.lower()

    for char in text_lower:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1


    if vowel_count > consonant_count:
        print(f"Більше голосних ({vowel_count})")
    elif consonant_count > vowel_count:
        print(f"Більше приголосних ({consonant_count})")
    else:
        print("Кількість голосних і приголосних однакова")


def unique_vowels_in_text(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    found_vowels = set(char for char in text.lower() if char in vowels)

    result = sorted(found_vowels)

    print("Голосні літери в алфавітному порядку:", " ".join(result))


word1 = "процесор"
word2 = "інформація"
unique_letters(word1, word2)

text1 = "testword123"
count_vowels_consonants(text1)

text2 = "somenewtestword"
unique_vowels_in_text(text2)
