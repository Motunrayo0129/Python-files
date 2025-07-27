import re

text = "Motunrayo is a gentle and calm girl and the git address is http://onibudomotunrayo2901@gmail.com"

pattern = re.findall(r"\w+", text)
pattern2 = re.compile(r"\b\d+\b", text)
print(pattern)

word = "I love my 29grandpa and daddy0, They are my best1 gift God gave me2006"
new_word = re.findall(r"[^0-9]+", word)
new_word2 = re.compile(r'[0-9]+')
print(new_word)
match = new_word2.findall(word)
print(match)

