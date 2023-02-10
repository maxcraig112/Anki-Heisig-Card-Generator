
import shutil
import json
import os


## Code to only grab kanji in heisig from https://github.com/KanjiVG/kanjivg

# kanjiList = json.load(open("heisig_data.json",encoding='utf-8'))
# for kanjiData in kanjiList:
#     shutil.move("C:/Users/maxcr/Desktop/kanjivg/kanji/" + kanjiList[kanjiData]["stroke_order"],"Heisig Kanji SVG/")

OLD_WIDTH_HEIGHT = 400
NEW_WIDTH_HEIGHT = 400
DIRECTORY = "Heisig Kanji SVG/"

for file in os.listdir(DIRECTORY):
    f = open(DIRECTORY + file,"r",encoding='utf-8')
    svgData = f.read()
    svgData = svgData.replace(f'width="{str(OLD_WIDTH_HEIGHT)}"',f'width="{str(NEW_WIDTH_HEIGHT)}"')
    svgData = svgData.replace(f'height="{str(OLD_WIDTH_HEIGHT)}"',f'height="{str(NEW_WIDTH_HEIGHT)}"')
    f.close()
    f = open(DIRECTORY + file,"w",encoding='utf-8')
    f.write(svgData)
    f.close()


