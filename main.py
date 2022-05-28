# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    counter = [0] * 256
    for i in word:
        counter[ord(i)] += 1
    # print(counter)
    for i in anagram:
        counter[ord(i)] -= 1
    # print(counter)
    return counter.count(0) == 256
print(find_anagram("hello", "check"))
print(find_anagram("elbow", "below"))