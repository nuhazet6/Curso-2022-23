text1 = "0001010011101"
text2 = "0000110010001"
hamming_distance = 0
for i in range(len(text1)):
    if text1[i] != text2[i]:
        hamming_distance += 1
print(hamming_distance)
