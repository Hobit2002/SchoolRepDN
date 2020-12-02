from django.core.cache import cache
import random,time

class Player:
    def __init__(self):
        self.lifes = 100
        self.Lived = False
        self.Discipline = 20
        self.Money = 20
        self.Glory = 20
        self.Hand = []
        self.Terrain = {}
        self.Vouchers = 0
        self.Attackers = []
        self.Buttons = ""
        self.SDIs = 0


class Game:

    def __init__(self,GameToken):
        self.players = {}
        self.Code = str(GameToken)
        self.Deck = []
        self.Pension = []
        self.EastDeck = []
        self.EasternBlock ={}
        self.Started = False
        self.Phase = "Unstarted"
        self.Phases = [["Elections","Politics"],["Elections","Politics"],["Elections","Politics"],["Contrarevolution","Reformation"]]
        self.PlayerNames = ["Player 1","Player 2","Player 3", "Communists"]
        self.Buttons = {"Politics":"<button id='EndTurn'>EndTurn</button>",
                        "Elections":"<button id='GoSerious'>Step into Politics</button>",
                        "Contrarevolution":"<button class='FightEnd' data-backid=\"%s\">Done</button>",
                        "Reformation":"<button class='NothingMore' data-backid=\"%s\">Nothing more</button>"}
        self.PhaseCoordinates = 0
        self.LastFigureId = 0
        self.CommunistCount = 0
        self.WorkCamp = []
        self.Reforming = []
        for i in range(1,4):
            NewPlayerToken = str(self.Code)+str(i)
            NewPlayer = Player()
            self.players[NewPlayerToken] = NewPlayer
        self.Triggers = {
            "NewFigure":[],
            "EastDeath":[],
            "WestDeath":[],
            "EndTurn":[],
            "RedTriumph":[],
            "Conflict":[],
            "GainedSDI":[],
            "DrawnCard":[]
            }
        self.EventRegisters = {
            "Conflict":{},
            "NewFigure":{},
            "EastDeath":{},
            "RedTriumph":{},
            "GainedSDI":{},
            "DrawnCard":{}
            }

    
    def AlterComs(self,Player,Count,Opperation,Commodity,GameDelta):
        PlayerIdent = self.players[Player]
        Count *= 10
        if Commodity == "Money":
            PlayerIdent.Money = eval("PlayerIdent."+Commodity + Opperation)
        elif Commodity == "Glory":
            PlayerIdent.Glory = eval("PlayerIdent."+Commodity + Opperation)
        elif Commodity == "Discipline":
            PlayerIdent.Discipline = eval("PlayerIdent."+Commodity + Opperation)
        elif Commodity == "Lives":
            PlayerIdent.lifes = eval("PlayerIdent.lifes" + Opperation)
        if Player not in GameDelta.keys():
            GameDelta[Player] = {Commodity:0}
        try:
            GameDelta[Player][Commodity] = eval("PlayerIdent."+Commodity)
        except AttributeError:
            GameDelta[Player][Commodity] = eval("PlayerIdent.lifes")
        return GameDelta

    def GetSDI(self,Player,Count,GameDelta):
        PlayerIdent = self.players[Player]
        PlayerIdent.SDIs += Count
        GameDelta = self.FireEvent(GameDelta,"GainedSDI",PlayerIdent)
        if PlayerIdent.SDIs >= 3:
            GameDelta["Alert"] = "You won"
        if Player not in GameDelta.keys():
            GameDelta[Player] = {}
        GameDelta[Player]["SDI"] = PlayerIdent.SDIs
        return GameDelta

    def RegisterPlayer(self):
        Players = self.players.items()
        for Token,player in Players:
            if player.Lived == False:
                player.Lived = True
                return Token

    def PlayerList(self):
        ReturnPack = {}
        Players = self.players.items()
        for playerToken, player in Players:
            if player.Lived == False:
                BioForm = "Daemon"
            else:
                BioForm = "Real"
            Key = "Player" + str(playerToken)
            ReturnPack[Key] = {"BioForm":BioForm}
            ReturnPack[Key].update({"ID":playerToken})
        return ReturnPack

    def GetPlayer(self,PlayerToken):
        PlayerList = self.players
        return PlayerList[PlayerToken]

    def DeletePlayer(self,PlayerNum):
        self.players[PlayerNum].Lived = False

    def save(self,GameDelta={}):
        cache.set(self.Code,self,7200)
        try: 
            if "Alert" in GameDelta.keys():
                if GameDelta["Alert"] == "You won":
                    cache.delete(self.Code)
                elif GameDelta["Alert"] == "Communism won":
                    cache.delete(self.Code)
        except AttributeError:
            pass
        
    def RenderAll(self,PlayerNum):
        GameDelta = {}
        GameDelta["GamePhase"] = self.Phases[self.PhaseCoordinates[0]][self.PhaseCoordinates[1]]
        GameDelta["TurningPlayer"] = self.PlayerNames[self.PhaseCoordinates[0]]
        try:
            GameDelta["TurningPlayerToken"] = list(self.players.keys())[self.PhaseCoordinates[0]]
        except IndexError:
            GameDelta["TurningPlayerToken"] = ""

        GameDelta["EasternBlock"] = {}
        for Key,Communist in self.EasternBlock.items():
            GameDelta["EasternBlock"][Key] = {}
            RedStats = GameDelta["EasternBlock"][Key]
            RedStats["RedName"] = Communist.Name
            RedStats["RedOccupation"] = Communist.Occupation
            RedStats["RedSociom"] = Communist.Sociom
            RedStats["RedResiliance"] = Communist.Resiliance
            RedStats["RedPower"] = Communist.Assertivity
        Players = self.players.items()
        for playerToken, player in Players:
            GameDelta[playerToken] = {}
            PlayerDict = GameDelta[playerToken]
            PlayerDict["Lifes"] = player.lifes
            PlayerDict["Discipline"] = player.Discipline
            PlayerDict["Money"] = player.Money
            PlayerDict["Glory"] = player.Glory
            PlayerDict["SDI"] = player.SDIs
            PlayerDict["Hand"] = {}
            ClientHand = PlayerDict["Hand"]
            for CardNum,Card in enumerate(player.Hand):
                if Card != "Bubo":
                    ClientHand[CardNum] = {}
                    CardStats = ClientHand[CardNum]
                    CardStats["CardName"] = Card.Name
                    CardStats["CardOccupation"] = Card.Occupation
                    CardStats["CardSociom"] = Card.Sociom
                    CardStats["CardResiliance"] = Card.Resiliance
                    CardStats["CardPower"] = Card.Assertivity
                    CardStats["CardMoney"] = Card.Money
                    CardStats["CardGlory"] = Card.Glory
                    CardStats["CardDiscipline"] = Card.Discipline
            PlayerDict.update({"Terrain":{}})
            PlayerTerrain = PlayerDict["Terrain"]
            Terrain = player.Terrain
            for FigureId,Figure in Terrain.items():
                PlayerTerrain[FigureId] = {}
                FigureStats = PlayerTerrain[FigureId]
                FigureStats["FigureName"] = Figure.Name
                FigureStats["FigureOccupation"] = Figure.Occupation
                FigureStats["FigureSociom"] = Figure.Sociom
                FigureStats["FigureResiliance"] = Figure.Resiliance
                FigureStats["FigurePower"] = Figure.Assertivity
                FigureStats["FigureMoney"] = Figure.Money
                FigureStats["FigureGlory"] = Figure.Glory
                FigureStats["FigureDiscipline"] = Figure.Discipline
            Attackers = player.Attackers
            if Attackers != []:
                PlayerDict["Attackers"]=[]
                for AttackerId in Attackers:
                    PlayerDict["Attackers"].append(AttackerId)

            PlayerDict["ButtonDiv"] = player.Buttons
            PlayerDict["Vouchers"] = self.players[playerToken].Vouchers
        return GameDelta

    def FireEvent(self,GameDelta,Event,*args):

        Cards = self.EventRegisters[Event]
        for Card in Cards.values():
            ArgString = ""
            if args != ():
                j = 0 
                ArgDict = {}
                for ar in args:
                    ArgDict[j] = ar
                    ArgString+=",ArgDict["+str(j)+"]"
                    j+=1
            
            EventDelta = eval("Card."+Event+"(self"+str(ArgString)+",GameDelta)")
            if EventDelta != None:
                GameDelta = EventDelta
        return GameDelta

    def StartGame(self,PlayerNum):
        from DeckClasses import DefaultSDI
        Deck = DefaultSDI.CreateDeck()
        random.shuffle(Deck)
        GameDelta = {}
        Players = self.players.items()
        self.Started = True
        self.PhaseCoordinates=[0,0]
        list(self.players.values())[0].Vouchers = 2
        self.Phase = self.Phases[self.PhaseCoordinates[0]][self.PhaseCoordinates[1]]
        list(self.players.values())[0].Buttons = self.Buttons[self.Phase]
        for playerToken, player in Players:
            player.Hand = Deck[:5]
            Deck = Deck[5:]
        self.Deck = Deck
        EastDeck = DefaultSDI.CreateEasternDeck()
        random.shuffle(EastDeck)
        self.EastDeck = EastDeck
        GameDelta = self.RenderAll(PlayerNum)
        return GameDelta

    def BuyCard(self,CardNum,PlayerNum):
        TurningPlayerToken =list(self.players.keys())[self.PhaseCoordinates[0]]
        PlayerOb = list(self.players.values())[self.PhaseCoordinates[0]]
        if PlayerNum == TurningPlayerToken or PlayerOb.Lived==False:
            Hand = PlayerOb.Hand
            Card = Hand[int(CardNum)]
            CardDiscipline = Card.Discipline
            CardMoney = Card.Money
            CardGlory = Card.Glory
            
            if PlayerOb.Glory - Card.Glory >= 0 and PlayerOb.Money - Card.Money  >= 0 and PlayerOb.Discipline - Card.Discipline >= 0:
                GameDelta = {TurningPlayerToken:{"Hand":{CardNum:{}}}}
                CardStats = GameDelta[TurningPlayerToken]["Hand"][CardNum]
                CardStats["CardName"] = ""
                CardStats["CardOccupation"] = ""
                CardStats["CardSociom"] = ""
                CardStats["CardResiliance"] = ""
                CardStats["CardPower"] = ""
                CardStats["CardMoney"] = ""
                CardStats["CardGlory"] = ""
                CardStats["CardDiscipline"] = ""
                Hand[int(CardNum)] = "Bubo"
                PlayerOb.Glory = PlayerOb.Glory - Card.Glory
                GameDelta[TurningPlayerToken]["Glory"] = PlayerOb.Glory
                PlayerOb.Money = PlayerOb.Money - Card.Money
                GameDelta[TurningPlayerToken]["Money"] = PlayerOb.Money
                PlayerOb.Discipline = PlayerOb.Discipline - Card.Discipline
                GameDelta[TurningPlayerToken]["Discipline"] = PlayerOb.Discipline
                NewCardNum = str(self.LastFigureId + 1)
                self.LastFigureId += 1
                PlayerOb.Terrain.update({NewCardNum:Card})
                GameDelta = self.conCard(Card,TurningPlayerToken,GameDelta)
                GameDelta[TurningPlayerToken].update({"Terrain":{NewCardNum:{}}})
                CardStats = GameDelta[TurningPlayerToken]["Terrain"][NewCardNum]
                CardStats["FigureName"] = Card.Name
                CardStats["FigureOccupation"] = Card.Occupation
                CardStats["FigureSociom"] = Card.Sociom
                CardStats["FigureResiliance"] = Card.Resiliance
                CardStats["FigurePower"] = Card.Assertivity
                CardStats["FigureMoney"] = Card.Money
                CardStats["FigureGlory"] = Card.Glory
                CardStats["FigureDiscipline"] = Card.Discipline
                return GameDelta

    def conCard(self,Card,playerTok,GameDelta):
        for trig in Card.Register:
            self.EventRegisters[trig][Card.Name] = Card
        Card.Controller = playerTok
        GameDelta = self.FireEvent(GameDelta,"NewFigure",Card)
        return GameDelta

    def NextPhase(self,PlayerNum):
        GameDelta = {}
        try:
            TurningPlayerToken = list(self.players.keys())[self.PhaseCoordinates[0]]
            TurningPlayer = list(self.players.values())[self.PhaseCoordinates[0]]
            PlayerName = self.PlayerNames[self.PhaseCoordinates[0]]
            if PlayerNum == TurningPlayerToken or TurningPlayer.Lived == False or PlayerName == "Communists":
                PhaseCount = len(self.Phases[self.PhaseCoordinates[0]])-1
                PlayerCount = len(self.PlayerNames)-1
                if self.PhaseCoordinates[1] < PhaseCount:
                    self.PhaseCoordinates[1] += 1
                    self.Phase = self.Phases[self.PhaseCoordinates[0]][self.PhaseCoordinates[1]]
                    TurningPlayer.Buttons = self.Buttons[self.Phase]
                elif self.PhaseCoordinates[1] == PhaseCount and self.PhaseCoordinates[0]<PlayerCount:
                    self.PhaseCoordinates[0] += 1
                    self.PhaseCoordinates[1] = 0
                    TurningPlayer.Buttons = ""
                    try:
                        TurningPlayerToken = list(self.players.keys())[self.PhaseCoordinates[0]]
                        TurningPlayer = list(self.players.values())[self.PhaseCoordinates[0]]
                        GameDelta = self.StartTurn(GameDelta)
                    except IndexError:
                        GameDelta["Message"] = "Redphase"
                        GameDelta["GamePhase"] = self.Phases[self.PhaseCoordinates[0]][self.PhaseCoordinates[1]]
                        GameDelta["TurningPlayer"] = self.PlayerNames[self.PhaseCoordinates[0]]
                        return GameDelta

        except IndexError:
            self.PhaseCoordinates=[0,0]
            TurningPlayerToken = list(self.players.keys())[self.PhaseCoordinates[0]]
            TurningPlayer = list(self.players.values())[self.PhaseCoordinates[0]]
            GameDelta = self.StartTurn(GameDelta)
            
        GameDelta["GamePhase"] = self.Phases[self.PhaseCoordinates[0]][self.PhaseCoordinates[1]]
        GameDelta["TurningPlayer"] = self.PlayerNames[self.PhaseCoordinates[0]]
        GameDelta["TurningPlayerToken"] = TurningPlayerToken
        if GameDelta["TurningPlayerToken"] not in GameDelta.keys():
            GameDelta[GameDelta["TurningPlayerToken"]] = {}
        TurningPlayer.Buttons = self.Buttons[GameDelta["GamePhase"]]
        GameDelta[GameDelta["TurningPlayerToken"]]["ButtonDiv"] = self.Buttons[GameDelta["GamePhase"]]
        return GameDelta

    def EndTurn(self,PlayerNum):
        TurningPlayerToken = list(self.players.keys())[self.PhaseCoordinates[0]]
        TurningPlayer = list(self.players.values())[self.PhaseCoordinates[0]]
        GameDelta = self.NextPhase(PlayerNum)
        try:
            Message = GameDelta["Message"]
            del GameDelta["Message"]
            TurningPlayer.Vouchers = 0
            TurningPlayer.Buttons=""
            GameDelta[TurningPlayerToken] = {"Vouchers":0,"ButtonDiv":""}
            GameDelta = self.RedExpansion(GameDelta)
            return GameDelta
        except KeyError:
            TurningPlayer.Vouchers = 0
            TurningPlayer.Buttons=""
            GameDelta[TurningPlayerToken] = {"Vouchers":0,"ButtonDiv":""}
            return GameDelta

    def StartTurn(self,GameDelta):
        TurningPlayer = list(self.players.values())[self.PhaseCoordinates[0]]
        TurningPlayerToken = list(self.players.keys())[self.PhaseCoordinates[0]]
        TurningPlayer.Vouchers = 2

        if TurningPlayerToken not in GameDelta.keys():
            GameDelta[TurningPlayerToken]={}
        GameDelta = self.DrawCard(TurningPlayer,TurningPlayerToken,GameDelta)

        GameDelta[TurningPlayerToken]["Vouchers"] = TurningPlayer.Vouchers
        return GameDelta

    def DrawCard(self,Player,pTok,GameDelta):
        try:
            if pTok not in GameDelta.keys():
                GameDelta[pTok]={}
            GameDelta[pTok]["Hand"] = {}
            if len(Player.Hand)<5:
                Player.Hand.append(self.Deck[0])
                self.Deck =self.Deck[1:]
                Card = Player.Hand(len(Player.Hand)-1)
                CardID = len(Player.Hand)-1
                GameDelta = self.FireEvent(GameDelta,"DrawnCard",Player)
            elif "Bubo" in Player.Hand:
                CardID = Player.Hand.index("Bubo")
                Card = self.Deck[0]
                Player.Hand[CardID] = Card
                self.Deck =self.Deck[1:]
                GameDelta = self.FireEvent(GameDelta,"DrawnCard",Player)
            else:
                return GameDelta
            GameDelta[pTok]["Hand"][str(CardID)] = {}
            CardStats = GameDelta[pTok]["Hand"][str(CardID)]
            CardStats["CardName"] = Card.Name
            CardStats["CardOccupation"] = Card.Occupation
            CardStats["CardSociom"] = Card.Sociom
            CardStats["CardResiliance"] = Card.Resiliance
            CardStats["CardPower"] = Card.Assertivity
            CardStats["CardMoney"] = Card.Money
            CardStats["CardGlory"] = Card.Glory
            CardStats["CardDiscipline"] = Card.Discipline
        except IndexError:
            GameDelta["Alert"] = "All cards drawn"
            
        return GameDelta

    def UseVoucher(self,PlayerNum,Commodity,Owner):
        SellingPlayer = self.players[Owner]
        if SellingPlayer.Vouchers >0 and (SellingPlayer.Lived == False or Owner==PlayerNum ):
            SellingPlayer.Vouchers -= 1
            Wealth = eval("SellingPlayer."+Commodity)
            Wealth +=10
            exec("SellingPlayer."+Commodity +"="+str(Wealth))
            GameDelta = {Owner:{Commodity:Wealth, "Vouchers":SellingPlayer.Vouchers}}
            return GameDelta
    
    def RedExpansion(self,GameDelta):
        NewRedies = self.EastDeck[:2]
        self.EastDeck = self.EastDeck[2:]
        GameDelta["EasternBlock"] = {}
        for Communist in NewRedies:
            RedKey = self.CommunistCount + 1
            self.CommunistCount += 1
            self.EasternBlock[RedKey] = Communist
            GameDelta["EasternBlock"][RedKey] = {}
            RedStats = GameDelta["EasternBlock"][RedKey]
            RedStats["RedName"] = Communist.Name
            RedStats["RedOccupation"] = Communist.Occupation
            RedStats["RedSociom"] = Communist.Sociom
            RedStats["RedResiliance"] = Communist.Resiliance
            RedStats["RedPower"] = Communist.Assertivity
        return [GameDelta,"RedTimes"]

    def RedAttack(self):
        PlayerIDs = list(self.players.keys())
        PlayerValues = list(self.players.values())
        Communists = self.EasternBlock.keys()
        GameDelta = {}
        for Communist in Communists:
            Index = random.choice([0,1,2])
            PlayerValues[Index].Attackers.append(Communist)
            PlayerID = PlayerIDs[Index]
            if PlayerID not in GameDelta.keys():
                GameDelta[PlayerID] = {"Attackers":[]}
            GameDelta[PlayerID]["Attackers"].append(Communist)

        for playerTok,player in self.players.items():
            if playerTok not in GameDelta.keys():
                GameDelta[playerTok]={}
            player.Buttons = self.Buttons["Contrarevolution"]%(playerTok)
            GameDelta[playerTok]["ButtonDiv"] = player.Buttons
        return GameDelta

    def Fight(self,PlayerNum,CommunistToken,BlockerToken,OwnerToken):
        if OwnerToken == PlayerNum or self.players[OwnerToken].Lived == False:
            player = self.players[OwnerToken]
            if (CommunistToken in player.Attackers) and (BlockerToken in list(player.Terrain.keys())):
                GameDelta = {}
                
                Communist = self.EasternBlock[CommunistToken]
                Blocker = player.Terrain[BlockerToken]
                GameDelta = self.FireEvent(GameDelta,"Conflict",Blocker,Communist)
                Communist.Resiliance -= Blocker.Assertivity
                player.Attackers.remove(CommunistToken)
                GameDelta["Graveyard"] = []
                if Communist.Resiliance <= 0:
                    del self.EasternBlock[CommunistToken]
                    GameDelta = self.FireEvent(GameDelta,"EastDeath",Blocker,Communist)
                    self.WorkCamp.append(Communist)
                    GameDelta["Graveyard"].append("Communist"+str(CommunistToken))
                else:
                    GameDelta["EasternBlock"] = {}
                    GameDelta["EasternBlock"][CommunistToken] = {"RedResiliance":Communist.Resiliance}

                Blocker.Resiliance -= Communist.Assertivity
                if Blocker.Resiliance <= 0:
                    del player.Terrain[BlockerToken]
                    self.Pension.append(Blocker)
                    GameDelta["Graveyard"].append(OwnerToken +"Figure"+BlockerToken)
                    for Register in Blocker.Register:
                        del self.EventRegisters[Register][Blocker.Name]
                else:
                    GameDelta[OwnerToken] = {"Terrain":{}}
                    GameDelta[OwnerToken]["Terrain"][BlockerToken] = {"FigureResiliance":Blocker.Resiliance}
                    self.Reforming.append(OwnerToken)
                return GameDelta

    def FightEnd(self,PlayerNum,OwnerToken):
        GameDelta = {}
        GameDelta["EasternBlock"] ={}
        if OwnerToken == PlayerNum or self.players[OwnerToken].Lived == False:
            player = self.players[OwnerToken]
            GameDelta[OwnerToken] = {"ButtonDiv":""}
            for Attacker in player.Attackers:
                player.lifes -= self.EasternBlock[Attacker].Assertivity
                GameDelta = self.FireEvent(GameDelta,"RedTriumph",self.EasternBlock[Attacker])
                if player.lifes < 0:
                    GameDelta["Alert"] = "Communism won"
                GameDelta["EasternBlock"][Attacker] = {}
            player.Attackers = []
            GameDelta[OwnerToken] = {"Lifes":player.lifes}
           # raise ValueError(self.Reforming)
            if OwnerToken not in self.Reforming:
                self.Reforming.append(OwnerToken)
                player.Buttons =""
            if len(self.Reforming)==3:
                self.Reforming = []
                self.PhaseCoordinates[1]+=1
                self.Phase = self.Phases[self.PhaseCoordinates[0]][self.PhaseCoordinates[1]]
                GameDelta["GamePhase"] = self.Phase
                GameDelta["TurningPlayer"] = self.PlayerNames[self.PhaseCoordinates[0]]
                for playerTok,player in self.players.items():
                    if playerTok not in GameDelta.keys():
                        GameDelta[playerTok] = {}
                    player.Buttons = self.Buttons[self.Phase]%(playerTok)
                    GameDelta[playerTok]["ButtonDiv"] = player.Buttons
            return GameDelta

    def NothingMore(self,PlayerNum,OwnerToken):
        GameDelta = {}
        Owner = self.players[OwnerToken]
        if OwnerToken == PlayerNum or self.players[OwnerToken].Lived == False:
            if OwnerToken not in self.Reforming:
                self.Reforming.append(OwnerToken)
            if len(self.Reforming) < 3:
                Owner.Buttons = ""
                GameDelta[OwnerToken] = {"ButtonDiv":""}
                return GameDelta
            if len(self.Reforming) == 3:
                self.Reforming = []
                GameDelta = self.NextPhase(PlayerNum)
                return GameDelta

    def Disposition(self,PlayerNum,OwnerNum,CardID):
        GameDelta = {}
        if OwnerNum == PlayerNum or self.players[OwnerNum].Lived == False:
            player = self.players[OwnerNum]
            Card = player.Terrain[CardID]
            GameDelta = eval("Card."+self.Phase+"(self,GameDelta)")
        return GameDelta


def AddPlayer(GameToken):
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    PlayerToken = OpenGame.RegisterPlayer()
    OpenGame.save()
    return PlayerToken

def GoSerious(PlayerNum):
    GameToken = str(PlayerNum)[:(len(str(PlayerNum))-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.NextPhase(PlayerNum)
    OpenGame.save(GameDelta)
    return GameDelta

def PlayerList(GameToken):
    OpenGame = None
    Focuses = 0
    while OpenGame ==None and Focuses < 100:
        OpenGame = cache.get(GameToken)
        time.sleep(0.02)
        Focuses +=1
    if OpenGame != None:
        PlayerList = OpenGame.PlayerList()
        return PlayerList
    else:
        return "End"

def UnconnectPlayer(PlayerToken):
    GameToken = str(PlayerToken)[:(len(str(PlayerToken))-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    OpenGame.DeletePlayer(PlayerToken)
    OpenGame.save(GameDelta)
    
def StartGame(PlayerNum):
    if PlayerNum[len(PlayerNum)-1]=='1':
        GameToken = PlayerNum[:(len(PlayerNum)-1)]
        OpenGame = None
        while OpenGame ==None:
            OpenGame = cache.get(GameToken)
        if OpenGame.Started == False:
            GameDelta = OpenGame.StartGame(PlayerNum)
            OpenGame.save()
            return GameDelta
        else:
            return None

def CreateGame():
    GameToken = cache.get_or_set('GameCount',1, 86400)
    NewValue = GameToken + 1
    cache.set('GameCount',NewValue, 86400)
    NewGame = Game(GameToken)
    Token = NewGame.RegisterPlayer()
    NewGame.save()
    return Token

def RenderAll(PlayerNum):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    wago =0
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
        wago += 1 
    GameDelta = OpenGame.RenderAll(PlayerNum)
    if OpenGame == None and wago>4:
            raise ValueError(GameToken)
    OpenGame.save(GameDelta)
    return GameDelta

def GameStarted(GameToken):
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    Phase = OpenGame.Started
    return str(Phase)

def BuyCard(CardNum,PlayerNum):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.BuyCard(CardNum,PlayerNum)
    OpenGame.save(GameDelta)
    return GameDelta

def EndTurn(PlayerNum):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.EndTurn(PlayerNum)
    OpenGame.save(GameDelta)
    return GameDelta

def UseVoucher(PlayerNum,Commodity,Owner):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.UseVoucher(PlayerNum,Commodity,Owner)
    OpenGame.save(GameDelta)
    return GameDelta

def RedAttack(PlayerNum):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.RedAttack()
    OpenGame.save(GameDelta)
    return GameDelta

def Fight(PlayerNum,Communist,Blocker,Owner):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.Fight(PlayerNum,Communist,Blocker,Owner)
    OpenGame.save(GameDelta)
    return GameDelta

def FightEnd(PlayerNum,Owner):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
    GameDelta = OpenGame.FightEnd(PlayerNum,Owner)
    OpenGame.save(GameDelta)
    if "Alert" in GameDelta.keys():
        if GameDelta["Alert"] == "Communism won":
            cache.delete(GameToken)

    return GameDelta

def NothingMore(PlayerNum,Owner):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
        if OpenGame==None:
            time.sleep(0.05)
    GameDelta = OpenGame.NothingMore(PlayerNum,Owner)
    OpenGame.save(GameDelta)
    return GameDelta

def ShowDetails(PlayerNum,ConrNum,ElNum,CardType):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
        if OpenGame==None:
            time.sleep(0.05)
    if CardType =="/Red/g":
        Object = OpenGame.EasternBlock[int(ElNum)]
    if CardType =="/Figure/g":
        Object = OpenGame.players[ConrNum].Terrain[ElNum]
    if CardType =="/Card/g":
        Object = OpenGame.players[ConrNum].Hand[int(ElNum)]
    Details = Object.RulesToShow
    Legend = Object.Legend
    return {"Details":Details,"Legend":Legend}

def Disposition(PlayerNum,OwnerNum,CardID):
    GameToken = PlayerNum[:(len(PlayerNum)-1)]
    OpenGame = None
    while OpenGame ==None:
        OpenGame = cache.get(GameToken)
        if OpenGame==None:
            time.sleep(0.05)
    GameDelta = {}
    GameDelta = OpenGame.Disposition(PlayerNum,OwnerNum,CardID)
    OpenGame.save(GameDelta)
    return GameDelta