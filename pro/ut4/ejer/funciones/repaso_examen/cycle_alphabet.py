# *****************
# ALFABETO CIRCULAR
# *****************

def generate_alphabet(text, max_letters):
    letter_index = 0
    for i in range(n):
        current_position = i % len(text)
        yield text[letter_index]
        letter_index += 1

def run(max_letters: int) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    text = ''.join(generate_alphabet(ALPHABET,max_letters))

    return text


if __name__ == '__main__':
    run(0)