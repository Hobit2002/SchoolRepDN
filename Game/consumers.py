import json,re,time
from django.core.cache import cache
from asgiref.sync import async_to_sync
from Game import GameStats
from channels.generic.websocket import WebsocketConsumer
import traceback

class PrepareHerald(WebsocketConsumer):

    def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = 'GameGroup_%s' % self.game_name
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json = json.loads(text_data)
            phase = text_data_json['Act']
            headers = self.scope['headers']
            sendThis = str(headers)
            for head in headers:
                if head[0]==b'cookie':
                    BaseString = head[1].decode('UTF-8') +";"
                    DesiredCookie = re.compile(r'PlayerNum=\d+;?')
                    SearchObject = DesiredCookie.search(BaseString)
                    DesiredSection = SearchObject.group()
                    Numform = re.compile(r'\d+')
                    SearchObject = Numform.search(DesiredSection)
                    PlayerNum = SearchObject.group()
            if phase == "Disconnect":
                GameStats.UnconnectPlayer(PlayerNum)
                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {
                        'type': 'unconnectPlayer',
                        'PlayerNum': PlayerNum 
                    }
                )
            if phase == "GameStarted":
                GameDelta = GameStats.StartGame(PlayerNum)
                if GameDelta != None:
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {
                            'type': 'GameDelta',
                            'DataChanges': json.dumps(GameDelta) 
                        })
            if phase == "WhatsGoingOn":
                GameDelta = GameStats.RenderAll(PlayerNum)
                self.send(text_data=json.dumps([{'name': 'GameDelta','GameDelta':json.dumps(GameDelta)}]))

            if phase =="NewFigure":
                CardNum = text_data_json['Vote']
                GameDelta = GameStats.BuyCard(CardNum,PlayerNum)
                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {'type': 'GameDelta',
                      'DataChanges': json.dumps(GameDelta)})

            if phase =="GoSerious":
                GameDelta = GameStats.GoSerious(PlayerNum)
                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {'type': 'GameDelta',
                      'DataChanges': json.dumps(GameDelta)})

            if phase =="FightEnd":
                Owner = text_data_json['Owner']
                Sins= cache.get(PlayerNum)
                if Sins!=[Owner,"FightEnd"]:
                    cache.set(PlayerNum,[Owner,"FightEnd"],1)
                    GameDelta = GameStats.FightEnd(PlayerNum,Owner)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {'type': 'GameDelta',
                        'DataChanges': json.dumps(GameDelta)})

            if phase =="NothingMore":
                Owner = text_data_json['Owner']
                Sins= cache.get(PlayerNum)
                if Sins!=[Owner,"NothingMore"]:
                    cache.set(PlayerNum,[Owner,"NothingMore"],1)
                    GameDelta = GameStats.NothingMore(PlayerNum,Owner)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {'type': 'GameDelta',
                          'DataChanges': json.dumps(GameDelta)})

            if phase =="EndTurn":
                GameDelta = GameStats.EndTurn(PlayerNum)
                if type(GameDelta) == list:
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {'type': 'GameDelta',
                          'DataChanges': json.dumps(GameDelta[0])})
                    GameDelta = GameStats.RedAttack(PlayerNum)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {'type': 'WaitingDelta',
                          'DataChanges': json.dumps(GameDelta)})

                else:
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {'type': 'GameDelta',
                          'DataChanges': json.dumps(GameDelta)})
                    
            if phase =="UseVoucher":
                Commodity = text_data_json['Commodity']
                Owner = text_data_json['Owner']
                GameDelta = GameStats.UseVoucher(PlayerNum,Commodity,Owner)
                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {'type': 'GameDelta',
                      'DataChanges': json.dumps(GameDelta)})

            if phase =="Blocking":
                Communist = int(text_data_json['Communist'])
                Blocker = text_data_json['Blocker']
                Owner = text_data_json['Owner']
                GameDelta = GameStats.Fight(PlayerNum,Communist,Blocker,Owner)
                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {'type': 'GameDelta',
                      'DataChanges': json.dumps(GameDelta)})

            if phase =="Disposition":
                OwnerNum = text_data_json['PlayerNum']
                CardID = text_data_json['CardID']
                GameDelta = GameStats.Disposition(PlayerNum,OwnerNum,CardID)
                async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {'type': 'GameDelta',
                      'DataChanges': json.dumps(GameDelta)})

        except Exception as err:
            message = traceback.format_exc()
            self.send(text_data=json.dumps([{'name': 'Error','message':message}]))
        

    def unconnectPlayer(self,event):
        PlayerNum = event['PlayerNum']
        # Send message to WebSocket
        self.send(text_data=json.dumps([{'name': 'Trudeau','PlayerNum':PlayerNum}]))

    def NewPlayer(self,event):
         PlayerNum = event['PlayerNum']
        # Send message to WebSocket
         self.send(text_data=json.dumps([{'name': 'NewPlayer','PlayerNum':PlayerNum}]))
         
    def GameDelta(self,event):
         GameDelta = event['DataChanges']
        # Send message to WebSocket
         self.send(text_data=json.dumps([{'name': 'GameDelta','GameDelta':GameDelta}]))

    def WaitingDelta(self,event):
        time.sleep(5)
        GameDelta = event['DataChanges']
        # Send message to WebSocket
        self.send(text_data=json.dumps([{'name': 'GameDelta','GameDelta':GameDelta}]))

class NewPlayer(WebsocketConsumer):
    
    def connect(self):
        self.game_group_name = "pop"
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json = json.loads(text_data)
            GameToken = text_data_json['Game']
            PlayerToken = GameStats.AddPlayer(GameToken)
            self.game_group_name = 'GameGroup_%s' % GameToken
            async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name
            )
            async_to_sync(self.channel_layer.group_send)(
                    self.game_group_name,
                    {
                        'type': 'NewPlayer',
                        'PlayerNum': PlayerToken 
                    }
                )
            cache.set(str(PlayerToken),GameToken,4)
            self.send(text_data=json.dumps({'name': 'Access','accessCode':PlayerToken}))
        except Exception as err:
            self.send(text_data=json.dumps({'name': 'Error','message':str(err)}))