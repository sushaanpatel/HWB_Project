import easyocr
from speak import say

def ocr(image_path):
    reader = easyocr.Reader(['en'])
    print("Reading Text")
    result = reader.readtext(image_path)
    return result

if __name__ == '__main__':
    data = ocr("data/frame1.jpg")
    string = ""
    for (bbox, text, prob) in data:
        string += text + " "

    # print(string)
    say(string)



