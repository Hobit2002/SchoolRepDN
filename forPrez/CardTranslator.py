#Import modules
import os,openpyxl,logging, json
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#Open Excel spredsheet and extract data about cards
#Open Sheet with good cards
wb=openpyxl.load_workbook('StudenaValka.xlsx')
sheet = wb['List1']
#Go through rows - different subjects. For each subject do following:
Cards = {"West":[],"East":[]}
GoodCards = Cards["West"]

for row in range(2, sheet.max_row + 1):
    GoodCards.append({})
    CardParameters = GoodCards[len(GoodCards)-1]
    CardParameters["Name"] = sheet.cell(row=row, column=1).value
    CardParameters["Abilities"] = sheet.cell(row=row, column=2).value + ";"
    CardParameters["Occupation"] = sheet.cell(row=row, column=3).value
    CardParameters["Sociom"] = sheet.cell(row=row, column=4).value
    CardParameters["Resiliance"] = sheet.cell(row=row, column=5).value
    CardParameters["Assertivity"] = sheet.cell(row=row, column=6).value
    CardParameters["Money"] = sheet.cell(row=row, column=7).value
    CardParameters["Glory"] = sheet.cell(row=row, column=8).value
    CardParameters["Discipline"] = sheet.cell(row=row, column=9).value
    CardParameters["Legend"] = sheet.cell(row=row, column=10).value

Redsheet = wb['List2']
RedCards = Cards["East"]
for row in range(2, Redsheet.max_row + 1):
    RedCards.append({})
    CardParameters = RedCards[len(RedCards)-1]
    CardParameters["Name"] = Redsheet.cell(row=row, column=1).value
    CardParameters["Abilities"] = Redsheet.cell(row=row, column=2).value + ";"
    CardParameters["Occupation"] = Redsheet.cell(row=row, column=3).value
    CardParameters["Sociom"] = Redsheet.cell(row=row, column=4).value
    CardParameters["Resiliance"] = Redsheet.cell(row=row, column=5).value
    CardParameters["Assertivity"] = Redsheet.cell(row=row, column=6).value
    CardParameters["Legend"] = Redsheet.cell(row=row, column=7).value


ToSave = json.dumps(Cards)
JSONFile = open('JSONCards.json','w')
JSONFile.write(ToSave)
JSONFile.close()




