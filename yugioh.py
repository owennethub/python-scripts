from array import array
from yugioh import guigame
import urllib2
import json
import os

monsterspath = "gamefiles/monsters.json"
spellspath = "gamefiles/spellcards.json"

def readFile(filepath, exists=false):
    if not exists:
        return open(filepath, "w+")
    return open(filepath, "r")

def loadMonsters(exists):
    
    monsterfile = Null
    
    if not exists:
        print "Monsters were not found. Downloading..."
        monsterfile = readfile(monsterpath, exists)
    
        
    headers= {'User-Agent' :'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    print "making request.."
    
    request = urllib2.Request("https://db.ygoprodeck.com/api/v5/cardinfo.php", headers=headers)
    response = urllib2.urlopen(request)
    webcards = json.load(response)
    cards = []
    
    print "copying data"
    
    for jsoncards in webcards:
        if jsoncards["type"] == "Normal Monster":
            card = { "id" : jsoncards["id"] , "name" : jsoncards["name"] , "attack" : jsoncards["atk"] , "defense" : jsoncards["def"] , "level" : jsoncards["level"] , "attribute" : jsoncards["attribute"] }
            cards.append(card)
            print card

    json.dump(cards , monsterfile)
    
    return cards


def loadSpells(exists):
    spellsfile = Null
    
    if not exists:
        print "Spells were not found. Using default spells..."
        spellsfile = readfile(spellpath, exists)
        
    spells = [{"name" : "Ambush","type" : "Trap Card","desc" : "When the opponent summon a monster face up with more than 1700 attack you can reduce his attack damage by 70%","effect" : {"typeeffect" : 1 , "action" : "target-(target*70/100)"}}]
    json.dump(spells , spellsfile)
    
    return spells


if not os.path.isdir("gamefiles"):
    os.mkdir("gamefiles")
    
loadMonsters(exists = os.path.exists(monsterspath))
loadSpells(exists = os.path.exists(spellspath)


main(emonsters = loadMonsters() , espells = loadSpells())
