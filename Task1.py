def GetVowelsCount(text):
    count = 0
    for letter in text:
        if letter in vowels:
            count = count + 1
    return count


vowels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
verse = input("text = ").lower()
phrases = verse.split(' ')

vowelsCount = GetVowelsCount(phrases[0])
isVerseOk = True
for phrase in phrases:
    isVerseOk &= GetVowelsCount(phrase) == vowelsCount

if isVerseOk:
    print("Парам пам-пам")
else:
    print("Пам парам")