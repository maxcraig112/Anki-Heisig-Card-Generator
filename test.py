f = open("hiragana.txt","r", encoding="utf-8")

data = f.read().replace("\n"," ").split(" ")
pass