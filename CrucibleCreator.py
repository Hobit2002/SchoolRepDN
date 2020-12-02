import json,re

def BuildRegisters(CardData):
    RegisterSet = {}
    RegisterSet["Player"] = {"Name":{"Register":{re.compile(r'((\w*(ni|eš) )| tv(é|á) | si )'):"self.Controller"},"Identificator":re.compile(r'.*')}}

    RegisterSet["Count"] = {"Number":{"Register":{re.compile(r'( bod | 1 | deset| 10(%| ))'):"1",
                                                  re.compile(r' dva| 2'):"2",
                                                  re.compile(r' tři| 3'):"3",
                                                  re.compile(r' čtyři| 4'):"4",
                                                  re.compile(r' pět|pades| 5'):"5",
                                                  re.compile(r' šest|šedes| 6'):"6",
                                                  re.compile(r' sedm| 7'):"7",
                                                  re.compile(r' osm| 8'):"8",
                                                  re.compile(r' dev(ět|adesát)| 9'):"9"
                                                  },"Identificator":re.compile(r'.*')}}
    RegisterSet["Commodity"] = {
                              "Type":{"Register":{re.compile(r' (peněz|peníz)'):"\"Money\"",
                                                  re.compile(r' morálk'):"\"Discipline\"",
                                                  re.compile(r' sláv'):"\"Glory\"",
                                                  re.compile(r' stabilit'):"\"Lives\""},"Identificator":re.compile(r'.*')},
                              }
    RegisterSet["Opperation"] = {
                              "Type":{"Register":{re.compile(r' zvýš(í|it) .* o '):"\"* (Count + 100)/100 \"",
                                                  re.compile(r' sníž(í|it) .* o '):"\"* (100-Count)/100 \"",
                                                  re.compile(r' přid(á|a)| dostaneš '):"\"+ Count\"",
                                                  re.compile(r' zaplatit '):"\"- Count\""},
                                                  "Identificator":re.compile(r'.*')}}

    RegisterSet["WestFig"] = {"Occupation":{"Register":{},"Identificator":re.compile(r'.*')},
                              "Sociom":{"Register":{},"Identificator":re.compile(r'postav. z ')},
                              "Name":{"Register":{re.compile(r'tato postava'):"self.Name"},"Identificator":re.compile(r'tato postava')},
                              "Controller":{"Register":{re.compile(r'tvá postava'):"self.Controller"},"Identificator":re.compile(r'postava')}
                              }

    RegisterSet["pId"] = {"Type":{"Register":{re.compile(r' ((\w*(ni|eš) )| tv(é|á) )'):"Game.players[self.Controller]"},
                                      "Identificator":re.compile(r'.*')}}

    for WestCard in CardData["West"]:
        WestOcc = WestCard["Occupation"]
        RegKey = WestOcc[:(len(WestOcc)-1)]  
        #RegKey = str(RegKey).replace("b'","").replace("'","")
        WestOcc = str(WestOcc.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        if "\'"+WestOcc+"\'" not in RegisterSet["WestFig"]["Occupation"]["Register"].values():
            RegisterSet["WestFig"]["Occupation"]["Register"][re.compile(RegKey)]= "\'"+WestOcc+"\'"
            

        WestSoc = WestCard["Sociom"]
        RegKey = WestSoc[:(len(WestSoc)-1)] 
        WestSoc = str(WestSoc.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        #RegKey = str(RegKey.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        WestOcc = str(WestSoc.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        if WestSoc not in RegisterSet["WestFig"]["Sociom"]["Register"]:
            RegisterSet["WestFig"]["Sociom"]["Register"][re.compile(RegKey)] = "\'"+WestSoc+"\'"
            

        RegisterSet["EastFig"] = {"Occupation":{"Register":{},"Identificator":re.compile(r'východní')},
                              "Sociom":{"Register":{},"Identificator":re.compile(r'východní.*  z ')},
                              "Name":{"Register":{re.compile(r'východní.* představitel'):""},"Identificator":re.compile(r'východní.* představitel')}
                              }
   
    for EastCard in CardData["East"]:
        EastOcc = EastCard["Occupation"]
        print("East Occupation:" + EastOcc)
        RegKey = EastOcc[:(len(EastOcc)-1)]  
        #RegKey = str(RegKey.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        EastOcc = str(EastOcc.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        if EastOcc not in RegisterSet["EastFig"]["Occupation"]["Register"]:
            RegisterSet["EastFig"]["Occupation"]["Register"][re.compile(r'východní.*' + RegKey.lower())]="\'"+EastOcc+"\'"
        EastSoc = EastCard["Sociom"]
        RegKey = EastSoc[:(len(EastSoc)-1)]
        EastSoc = str(EastSoc.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        #RegKey = str(RegKey.encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
        if EastSoc not in RegisterSet["EastFig"]["Sociom"]["Register"]:
            RegisterSet["EastFig"]["Sociom"]["Register"][re.compile(r'východní.* z ' + RegKey)] = "\'"+EastSoc+"\'"
    print("East occupations:" +str(RegisterSet["EastFig"]["Occupation"]["Register"]))
    print("East socioms:" +str(RegisterSet["EastFig"]["Sociom"]["Register"]))
    return RegisterSet

def KwargColl(Kwargargs,Ability):
    global RegisterSet
    Cascade = ""
    Space = "    "
    tok = 2
    
    for KwKey,KwAg in Kwargargs.items():
        Base = tok*(Space)+"if "
        argNum = 0
        for Aspect,Coords in RegisterSet[KwAg].items():
            if Coords["Identificator"].search(Ability) != None:
                for Possibility,Value in Coords["Register"].items():
                    #raise ValueError(Ability)
                    if Possibility.search(Ability) != None:
                        if Value != "":
                            if argNum>0:Base+=" and "
                            Base += KwKey + "." + Aspect + "==" + Value
                            argNum +=1
                            
                        else:
                            continue

        if Base !=tok*(Space)+"if ":
            tok += 1
            Cascade += Base +":\n"
    return Cascade,tok

def AcIdentifer(AcPart,tok,AddEnd = True):
    Space = "    "
    Declarations =""
    AcRegister = {"DrawCard":{"Identificator":re.compile(r'lízn.*kar(t|e)'),"Kwargargs":{"pId":"pId","Player":"Player"}},
                  "GetSDI":{"Identificator":re.compile(r'dostane.*body* SDI'),"Kwargargs":{"Player":"Player","Count":"Count"}},
                  "AlterComs":{"Identificator":re.compile(r'(přid|dostan|zvýš|zaplatit|sníž).* (peněz|peníz|morálk|sláv|stabilit)'),"Kwargargs":{"Player":"Player","Count":"Count","Opperation":"Opperation","Commodity":"Commodity"}},
                  }
    ArgStr = ""
    for Func,Aspects in AcRegister.items():
        if Aspects["Identificator"].search(AcPart)!=None:
            for VarName,VarType in Aspects["Kwargargs"].items():
                ArgStr += VarName + ","
                for Aspect,Coords in RegisterSet[VarType].items():
                    if Coords["Identificator"].search(Ability) != None:
                        for Possibility,Value in Coords["Register"].items():
                            if Possibility.search(AcPart) != None:
                                Declarations += tok*Space + VarName + "=" + Value +"\n"
                                
            
            Declarations += tok*Space + "GameDelta = Game."+Func +"("+ArgStr[:(len(ArgStr)-1)]+",GameDelta)\n"
            if AddEnd:
                Declarations += tok*Space + "return GameDelta\n"

    return Declarations

def TriggerSolver(Ability,Register,Methods):
    TrigPart = re.compile(r'.*,').search(Ability).group()
    ActPart = re.compile(r',.*').search(Ability).group()
    TriggerEvents = {
    "NewFigure":{"Identificator":re.compile(r'Kdy.+přijde .*do hry'),"KwargFunc":{"Figure":"WestFig"}},
    "EastDeath":{"Identificator":re.compile(r'triumfuje'),"KwargFunc":{"Figure":"WestFig","Communist":"EastFig"}},
    "WestDeath":{"Identificator":re.compile(r'hroch'),"KwargFunc":{}},
    "EndTurn":{"Identificator":re.compile(r'hroch'),"KwargFunc":{}},
    "RedTriumph":{"Identificator":re.compile(r'Kdykoliv .+ ovlivněn východním '),"KwargFunc":{"Communist":"EastFig"}},
    "Conflict":{"Identificator":re.compile(r'Kdykoliv se .* střetne s'),"KwargFunc":{"Figure":"WestFig","Communist":"EastFig"}},
    "GainedSDI":{"Identificator":re.compile(r'Kdykoliv dostaneš bod SDI'),"KwargFunc":{"Player":"pId"}},
    "DrawnCard":{"Identificator":re.compile(r'Kdykoliv si lízneš kartu'),"KwargFunc":{"Player":"pId"}}}

    for EvName,Event in TriggerEvents.items():
        if Event["Identificator"].search(TrigPart) != None:
            Register.append(EvName)
            Header = "    def " + EvName + "(self,Game,"
            for kwarg in Event["KwargFunc"].keys():
                Header += kwarg + ","
            Header = Header[:(len(Header)-1)] + ",GameDelta):\n"
            Cascade,tok = KwargColl(Event["KwargFunc"],Ability)
            Cascade += AcIdentifer(ActPart,tok)
            Methods += Header + Cascade
    return Register,Methods

def DisposSolver(Ability,Register,Methods):
    LocPart = re.compile(r'(Během |Na konci ).*? mů').search(Ability).group()
    OppPart = re.compile(r'.*? a').search(Ability.replace(LocPart,"")).group()
    ActPart = Ability.replace(LocPart,"").replace(OppPart,"")
    TriggerEvents = {
    "Politics":{"Identificator":re.compile(r'Během svého tahu')},
    "Reformation":{"Identificator":re.compile(r'Na konci rudé expanze')}
    }
    for DisName,Disposition in TriggerEvents.items():
        if Disposition["Identificator"].search(LocPart) != None:
            Space = "    "
            Header = Space + "def " + DisName + "(self,Game,GameDelta):"
            Header += "\n"+2*Space+"if Game.Phase=="+"\'"+DisName+"\':\n"
            Header+=3*Space+"GameDelta = {}\n"
            Header += AcIdentifer(OppPart,3,False)
            Header += AcIdentifer(ActPart,3)
            Methods += Header 
    return Register,Methods

AbiKeys = {
    "Trigger":[re.compile(r'Kdy.+,.+'),TriggerSolver],
    "Dispos":[re.compile(r'(Během |Na konci ).* můžeš'),DisposSolver],
    "Filter":[re.compile(r'roguu')]}
File1 = open('JSONCards.json',"r")
dataForm = json.load(File1,encoding = '')
RegisterSet = BuildRegisters(dataForm)
WestCards = dataForm["West"]
File1.close()
File2 = open('DeckClasses\DefaultSDI.py',"w")
Content =""
DeckFunc ="def CreateDeck():"
ReturnLine = "\n    return["
for ID, Card in enumerate(WestCards):
    Name = str(Card["Name"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    ClassName = str(Name).replace(" ","").replace(".","").replace("b'","").replace("'","").replace("\\","").replace("-","")
    ActiveText = Card["Abilities"]
    RulesToAdd = str(Card["Abilities"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    Occupation = str(Card["Occupation"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    Sociom = str(Card["Sociom"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    Resiliance = Card["Resiliance"]
    Assertivity = Card["Assertivity"]
    Money = Card["Money"]
    Glory = Card["Glory"]
    Discipline = Card["Discipline"]
    Legend = str(Card["Legend"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    NewString = """
class %s:

    def __init__(self):
        self.Name = '%s'
        self.Occupation = '%s'
        self.Sociom = '%s'
        self.Resiliance = %s
        self.Assertivity = %s
        self.Money = %s
        self.Glory = %s
        self.Discipline = %s
        self.RulesToShow = '%s'
        self.Controller = 0
        self.Legend = '%s'
"""%(ClassName,Name,Occupation,Sociom,Resiliance,Assertivity,Money,Glory,Discipline,RulesToAdd,Legend)
    ObjectName = "c" + str(ID)
    Content += NewString

    Register =[]
    Methods = "\n\n"
    AbilityForm = re.compile(r'.*?;')
    Abilities = AbilityForm.findall(ActiveText)
    for Ability in Abilities:
        for AbKey in AbiKeys.values():
            LookForThis = AbKey[0]
            if LookForThis.search(Ability) != None:
                Register,Methods = AbKey[1](Ability,Register,Methods)      

    Registring = "        self.Register =" + str(Register)
    Content += Registring + Methods
    FunctionLine = "\n    "+ObjectName+ "="+ClassName+"()"
    DeckFunc += FunctionLine
    ReturnLine += ObjectName+","

ReturnLine = ReturnLine[:(len(ReturnLine)-1)]+"]"
DeckFunc += ReturnLine 
Content += DeckFunc

EastCards = dataForm["East"]
EasternPart = ""
DeckFunc ="def CreateEasternDeck():"
ReturnLine = "\n    return["
for ID, Card in enumerate(EastCards):
    Name = str(Card["Name"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    RulesToAdd = str(Card["Abilities"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    ClassName = str(Name).replace(" ","").replace(".","").replace("b'","").replace("'","").replace("\\","").replace("-","")
    Occupation = str(Card["Occupation"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    Sociom = str(Card["Sociom"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    Resiliance = Card["Resiliance"]
    Assertivity = Card["Assertivity"]
    Legend = str(Card["Legend"].encode(encoding='UTF-8',errors='strict')).replace("b'","").replace("'","")
    NewString = """
class %s:

    def __init__(self):
        self.Name = '%s'
        self.Occupation = '%s'
        self.Sociom = '%s'
        self.Resiliance = %s
        self.Assertivity = %s
        self.RulesToShow = '%s'
        self.Legend = '%s'
"""%(ClassName,Name,Occupation,Sociom,Resiliance,Assertivity,RulesToAdd,Legend)
    ObjectName = "e" + str(ID)
    EasternPart += NewString
    FunctionLine = "\n    "+ObjectName+ "="+ClassName+"()"
    DeckFunc += FunctionLine
    ReturnLine += ObjectName+","

ReturnLine = ReturnLine[:(len(ReturnLine)-1)]+"]"
DeckFunc += ReturnLine 
EasternPart += DeckFunc
Content += EasternPart

Content = Content.replace(".Type","")
File2.write(Content)
File2.close()
    


