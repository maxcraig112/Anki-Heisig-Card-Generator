
allKanji = ""
with open('all kanji heisig.txt','r',encoding='utf-8') as file:
    allKanji = list(file.read().replace(' ',''))

print(len(allKanji))