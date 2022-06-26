import string
from typing import List


def reverseWords(sentence: string) -> string:
    temp = sentence.split()
    temp.reverse()
    new_sentence = " ".join(temp)
    return new_sentence


test_speech = input("Please input a very long string:\n")
print(reverseWords(test_speech))