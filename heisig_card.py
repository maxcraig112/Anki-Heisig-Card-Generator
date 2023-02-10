import genanki
import random
import json
import os



def generateReadingDeck():
    file = open("heisig_data.json","r",encoding="utf-8")
    heisigData = json.load(file)

    readingModel = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        'Heisig Reading Model',
        fields=[
            {'name': 'Kanji Character'},
            {'name': 'Heisig Meaning'},
            {'name': 'Kun Reading'},
            {'name': 'Stroke Order'},
            {'name': 'Alternate Meanings'},
        ],
        templates=[
            {
                'name': 'Card test',
                'qfmt': '<div class="main title">Kanji</div><div class="main answer">{{Kanji Character}}</div>',
                'afmt': '{{FrontSide}}<hr> \
                    <div class="main title">Heisig Meaning</div> <div class="main answer">{{Heisig Meaning}}</div> <hr> \
                    <div class="main title">Kun Reading</div> <div class="main answer">{{Kun Reading}}</div> <hr> \
                    <div class="main title">Stroke Order</div> <div class="main answer">{{Stroke Order}}</div> <hr> \
                    <div class="main title">Alternate Meanings</div> <div class="main answer">{{Alternate Meanings}}</div> </div>'
            },
        ]
    )

    readingDeck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        'Heisig Reading Deck'
    )

    for kanji in heisigData:
        #get kanji data
        kanjiData = heisigData[kanji]

        #create new note
        newReadingNote = genanki.Note(
        readingModel,
        fields=[
            kanjiData["kanji"],
            kanji,
            kanjiData["kun_reading"],
            f'<img src="{kanjiData["stroke_order"]}">',
            str(kanjiData["alternate_meanings"])[1:-1].replace("'","")
        ]
        )

        #add node to deck
        readingDeck.add_note(newReadingNote)

    readingPackage = genanki.Package(readingDeck)

    readingModel.css = str(open("main.css",'r').read())

    #get directory where svg files are stored
    DIRECTORY = "Heisig Kanji SVG/"
    allFilePaths = [DIRECTORY + p for p in os.listdir(DIRECTORY)]
    #add all media files to package
    readingPackage.media_files = allFilePaths
    readingPackage.write_to_file('ReadingDeck.apkg')

def generateWritingDeck():
    file = open("heisig_data.json","r",encoding="utf-8")
    heisigData = json.load(file)

    readingModel = genanki.Model(
        120391087121,
        'Heisig Writing Model',
        fields=[
            {'name': 'Heisig Meaning'},
            {'name': 'Kanji Character'},
            {'name': 'Kun Reading'},
            {'name': 'Stroke Order'},
            {'name': 'Alternate Meanings'},
        ],
        templates=[
            {
                'name': 'Card test',
                'qfmt': '<div class="main title">Heisig Meaning</div><div class="main answer">{{Heisig Meaning}}</div>',
                'afmt': '{{FrontSide}}<hr> \
                    <div class="main title">Kanji</div> <div class="main answer">{{Kanji Character}}</div> <hr> \
                    <div class="main title">Kun Reading</div> <div class="main answer">{{Kun Reading}}</div> <hr> \
                    <div class="main title">Stroke Order</div> <div class="main answer">{{Stroke Order}}</div> <hr> \
                    <div class="main title">Alternate Meanings</div> <div class="main answer">{{Alternate Meanings}}</div> </div>'
            },
        ]
    )

    readingDeck = genanki.Deck(
        120392312321,
        'Heisig Writing Deck'
    )

    for kanji in heisigData:
        #get kanji data
        kanjiData = heisigData[kanji]

        #create new note
        newReadingNote = genanki.Note(
        readingModel,
        fields=[
            kanjiData["kanji"],
            kanji,
            kanjiData["kun_reading"],
            f'<img src="{kanjiData["stroke_order"]}">',
            str(kanjiData["alternate_meanings"])[1:-1].replace("'","")
        ]
        )

        #add node to deck
        readingDeck.add_note(newReadingNote)

    readingPackage = genanki.Package(readingDeck)

    readingModel.css = str(open("main.css",'r').read())

    #get directory where svg files are stored
    DIRECTORY = "Heisig Kanji SVG/"
    allFilePaths = [DIRECTORY + p for p in os.listdir(DIRECTORY)]
    #add all media files to package
    readingPackage.media_files = allFilePaths
    readingPackage.write_to_file('WritingDeck.apkg')

generateWritingDeck()