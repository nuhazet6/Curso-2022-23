song = """You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness"""


list = song.split("voices")
print(list[0], "sounds", list[1], sep="")
print()


song = """You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness"""

list = song.split("voices")
print(list[0], list[1], sep="sounds")
print()

old_word = "voices"
new_word = "sounds"
word_position = song.find(old_word)
word_final = word_position + len(old_word)
print(song[:word_position] + new_word + song[word_final:])