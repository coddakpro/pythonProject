sentence = input('Sentence: ')
if not sentence[0].isupper() and sentence[-1] != '.':
    print(sentence.capitalize() + ".")
