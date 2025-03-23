import easyocr
from spellchecker import SpellChecker
from speak import say

reader = easyocr.Reader(['en'])
spell = SpellChecker()


def spell_correct(text: str):
    temp = text.split(" ")
    out = ""
    for i in range(len(temp)):
        corrected = spell.correction(temp[i])
        valid_text = (corrected if corrected is not None else temp[i])
        if i == len(temp) - 1:
            out += valid_text
        else:
            out += valid_text + " "
    return out

def ocr(image_path: str):
    print("Reading Text")
    data = reader.readtext(image_path)

    string = ""
    for (bbox, text, prob) in data:
        print(text, prob)
        if prob >= 0.5:
            temp = spell_correct(text)
            string += (temp if temp is not None else text) + " "

    print(string)
    say(string)

if __name__ == '__main__':
    # data = ocr("data/frame3.jpg")
    # string = ""
    # for (bbox, text, prob) in data:
    #     print(text, prob)
    #     if prob >= 0.5:
    #         temp = spell_correct(text)
    #         string += (temp if temp is not None else text) + " "

    # print(string)
    # say(string)
    pass