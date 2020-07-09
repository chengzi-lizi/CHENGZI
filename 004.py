# coding=utf-8

sentence = "I love  code."
print(sentence)

word = sentence.split(" ")
print(word)

new_word = [part for part in word if part!=""]    #将空格检出
print(new_word)

new_sentence = " ".join(new_word)
print(new_sentence)
