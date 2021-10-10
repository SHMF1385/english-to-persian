alphabet_fa = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی', 'آ', 'ئ', 'ء']
alphabet_en = ['h', 'f', '\\', 'j', 'e', '[', ']', 'p', 'o', 'n', 'b', 'v', 'c', 's', 'a', 'w', 'q', 'x', 'z', 'u', 'y', 't', 'r', ';', "'", 'g', 'l', 'k', ',', 'i', 'd', 'H', 'M', 'm']

characters = input("Enter: ")
for i in alphabet_en:
    if i in characters:
        characters = characters.replace(i, alphabet_fa[alphabet_en.index(i)])
print(characters)
