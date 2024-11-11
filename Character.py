import xml.etree.ElementTree as ET
import os



class Character():
    def __init__(self):
        self.CharName = "Testify"
        self.health = 20




    def LoadCharacterAttr(self, Mode="Blitz", id=0, target="Name"):
        data = self.LoadXML(Mode)
        for character in data.findall("Character"):
            if character.tag.find("Id").text == str(id):
               #As there are only 3 values it could be after,
               match target:
                   case "Name":
                       return character.tag.find(target).text
                   case "Health":
                       return int(character.tag.find(target).text)
                   case _:
                       return bool(character.text)

    def LoadCharacterList(self, Mode="Blitz"):
        data = self.LoadXML(Mode)
        mylist = []

        for character in data:


    def LoadXML(self, Mode="Blitz"):
        file_name = Mode + ".xml"
        file_path = os.path.join(os.path.dirname(__file__), 'Data', file_name)
        return ET.parse(file_path).getroot()

        