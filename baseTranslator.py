morse_code = ("e", "."),("i", ".."),("s", "..."),("h", "...."),("a", ".-"),("u", "..-"),("v", "...-"),("w", ".--"),("j", ".---"),("r", ".-."),("l", ".-.."),("f", "..-."),("p", ".--."),("t", "-"),("m", "--"),("o", "---"),("n", "-."),("g", "--."),("z", "--.."),("q" ,"--.-"),("d", "-.."),("b", "-..."),("k", "-.-"),("c", "-.-."),("y", "-.--"),("x", "-..-"),(" ","/")


def search(x):
    if x<"a":
        for row in morse_code:
            if row[1]==x:
                return row[0]
    else:
        for row in morse_code:
            if row[0]==x:
                return row[1]



def translate(y):
    y = y.lower()
    words = y.split()
    translated = ""
    for word in words:
        if y >="a":

            for letter in word:
                translated = translated + search(letter) + " "
            translated = translated + "/ "
        else:
            translated = translated + search(word) 
    return translated




print(translate("... --- ... / "))
print(type(morse_code))

