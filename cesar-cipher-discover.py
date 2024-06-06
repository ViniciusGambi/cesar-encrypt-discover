from langdetect import detect, DetectorFactory

text = "Hzn oerir erivfnb fboer pevcgbtensvn"

def cesar_encrypt(text, n):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        elif (char.isupper()):
            result += chr((ord(char) + n - 65) % 26 + 65)
        else:
            result += chr((ord(char) + n - 97) % 26 + 97)
    return result

def check_if_sentence_makes_sense_in_portuguese(sentence):
    DetectorFactory.seed = 0
    language = detect(sentence)
    return language == 'pt'

if __name__ == '__main__':
    for i in range(26):
        sentence = cesar_encrypt(text, i)
        if check_if_sentence_makes_sense_in_portuguese(sentence):
            print(i, sentence)