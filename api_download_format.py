import json
import requests

#open index of every svg file
kvg_index = json.load(open("kvg-index.json",encoding='utf-8'))

#get list of all kanji
allKanjiRequest = requests.get("https://kanjiapi.dev/v1/kanji/all")
kanjiList = allKanjiRequest.json()

#define json file that contains all relevant heisig kanji
heisig_data = {}

#for all kanji
for i in range(len(kanjiList)):
    #print current percentage so i know how long
    if i%10 ==0:
        print(i)
    #get data about current kanji in json format
    kanjiData = requests.get("https://kanjiapi.dev/v1/kanji/" + kanjiList[i]).json()

    #if kanji has heisig id
    if kanjiData["heisig_en"] != None:
        #if heisig name already exists in json (used for testing)
        if kanjiData["heisig_en"] in heisig_data:
            print("DUPLICATE")
        else:
            #define new key-value for heisig
            heisig_data[kanjiData["heisig_en"]] = {
                "kanji": kanjiList[i],
                "alternate_meanings": kanjiData["meanings"][1:],
                "kun_reading":  kanjiData["kun_readings"][0] if len(kanjiData["kun_readings"]) != 0 
                                else kanjiData["name_readings"][0] if len(kanjiData["name_readings"]) != 0 
                                else kanjiData["on_readings"][0],
                "stroke_order": kvg_index[kanjiList[i]][-1]
            }

with open('heisig_data.json', 'wb') as fp:
    fp.write(json.dumps(heisig_data, ensure_ascii=False).encode("utf8"))