
class MargretTatcherovxc3xa1:

    def __init__(self):
        self.Name = 'Margret Tatcherov\xc3\xa1'
        self.Occupation = 'Politik'
        self.Sociom = 'VB'
        self.Resiliance = 50
        self.Assertivity = 90
        self.Money = 20
        self.Glory = 30
        self.Discipline = 20
        self.RulesToShow = 'Kdykoliv tato postava triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, zv\xc3\xbd\xc5\xa1\xc3\xad se tv\xc3\xa9 pen\xc3\xadze o 30%.;'
        self.Controller = 0
        self.Legend = 'Sedmdes\xc3\xa1t\xc3\xa1 l\xc3\xa9ta pro z\xc3\xa1padn\xc3\xad sv\xc4\x9bt nebyla kv\xc5\xafli n\xc4\x9bkolika ropn\xc3\xbdm kriz\xc3\xadm zrovna r\xc3\xa1jem a vl\xc3\xa1dy se sna\xc5\xbeily nespokojen\xc3\xa9 ob\xc4\x8dany udob\xc5\x99it v\xc5\xa1emo\xc5\xben\xc3\xbdmi populistick\xc3\xbdmi opat\xc5\x99en\xc3\xadmi. Pr\xc3\xa1v\xc4\x9b tomu u\xc4\x8dinila Margret Tatcherov\xc3\xa1 minim\xc3\xa1ln\xc4\x9b v Brit\xc3\xa1nii p\xc5\x99\xc3\xadtr\xc5\xbe, kdy\xc5\xbe osekala jak vl\xc3\xa1dn\xc3\xad v\xc3\xbddaje tak dan\xc4\x9b, oslabila d\xc4\x9blnick\xc3\xa9 odbory a privatizovala st\xc3\xa1tn\xc3\xad podniky. Jej\xc3\xad politika byla v\xc5\xbedy velmi kontroverzn\xc3\xad a p\xc5\x99iv\xc3\xa1d\xc4\x9bla k zlosti i jej\xc3\xad nejbli\xc5\xbe\xc5\xa1\xc3\xad kolegy.'
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=3
            Opperation="* (Count + 100)/100 "
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class RonaldReagan:

    def __init__(self):
        self.Name = 'Ronald Reagan'
        self.Occupation = 'Politik'
        self.Sociom = 'USA'
        self.Resiliance = 100
        self.Assertivity = 80
        self.Money = 40
        self.Glory = 20
        self.Discipline = 30
        self.RulesToShow = 'Kdykoliv n\xc4\x9bjak\xc3\xa1 tv\xc3\xa1 postava triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Controller==self.Controller:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class UsamabinLadin:

    def __init__(self):
        self.Name = 'Usama bin Ladin'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Muslimsk\xc3\xbd sv\xc4\x9bt'
        self.Resiliance = 40
        self.Assertivity = 100
        self.Money = 0
        self.Glory = 0
        self.Discipline = 30
        self.RulesToShow = 'Na konci rud\xc3\xa9 expanze m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit 20 mor\xc3\xa1lky a p\xc5\x99idat si 20 pen\xc4\x9bz.;'
        self.Controller = 0
        self.Legend = 'Je to skoro a\xc5\xbe absurdn\xc3\xad, ale pozd\xc4\x9bj\xc5\xa1\xc3\xad v\xc5\xafdce teroristick\xc3\xa9 organizace Al-K\xc3\xa1ida (zodpov\xc4\x9bdn\xc3\xa9 nap\xc5\x99\xc3\xadklad za teroristick\xc3\xbd \xc3\xbatok na \xe2\x80\x9eDvoj\xc4\x8data\xe2\x80\x9c) b\xc4\x9bhem studen\xc3\xa9 v\xc3\xa1lky Ameri\xc4\x8dan\xc5\xafm d\xc4\x9blal velkou radost, kdy\xc5\xbe se sob\xc4\x9b podobn\xc3\xbdmi \xe2\x80\x9ebojoval proti\xc2\xa0nev\xc4\x9b\xc5\x99\xc3\xadc\xc3\xadm, kte\xc5\x99\xc3\xad napadli jeho vlast\xe2\x80\x9c (Sov\xc4\x9bt\xc5\xafm, kte\xc5\x99\xc3\xad zkusili expandovat do Afgh\xc3\xa1nist\xc3\xa1nu).'
        self.Register =[]

    def Reformation(self,Game,GameDelta):
        if Game.Phase=='Reformation':
            GameDelta = {}
            Player=self.Controller
            Count=2
            Opperation="- Count"
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Player=self.Controller
            Count=2
            Opperation="+ Count"
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class Mudxc5xbeahedxc3xbdni:

    def __init__(self):
        self.Name = 'Mud\xc5\xbeahed\xc3\xbdni'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Muslimsk\xc3\xbd sv\xc4\x9bt'
        self.Resiliance = 60
        self.Assertivity = 30
        self.Money = 0
        self.Glory = 0
        self.Discipline = 20
        self.RulesToShow = 'Kdykoliv p\xc5\x99ijde V\xc3\xa1le\xc4\x8dn\xc3\xadk do hry, zv\xc3\xbd\xc5\xa1\xc3\xad se tv\xc3\xa1 mor\xc3\xa1lka o 25%.;'
        self.Controller = 0
        self.Legend = 'Zat\xc3\xadmco pro z\xc3\xa1pad sedmdes\xc3\xa1t\xc3\xa1 l\xc3\xa9ta nebyla \xc5\xbe\xc3\xa1dn\xc3\xbd med, v\xc3\xbdchod z nich vy\xc5\xa1el pos\xc3\xadlen\xc3\xbd a troufal\xc3\xbd k dal\xc5\xa1\xc3\xad expanzi. Objektem mocensk\xc3\xbdch choutek tehdej\xc5\xa1\xc3\xadho gener\xc3\xa1ln\xc3\xadho tajemn\xc3\xadka se stal zd\xc3\xa1nliv\xc4\x9b slab\xc3\xbd Afgh\xc3\xa1nist\xc3\xa1n. Ale ouha, m\xc3\xadstn\xc3\xad obyvatel\xc3\xa9 se postavili na odpor a zp\xc5\xafsobili Rus\xc5\xafm traumata srovnateln\xc3\xa1 s t\xc4\x9bmi, kter\xc3\xa1 utrp\xc4\x9bli Ameri\xc4\x8dan\xc3\xa9 ve Vietnamu. On\xc4\x9bm odv\xc3\xa1\xc5\xben\xc3\xbdm, \xc4\x8dasto n\xc3\xa1bo\xc5\xbeensky fanatick\xc3\xbdm bojovn\xc3\xadk\xc5\xafm vybaven\xc3\xbdm americkou technikou, se \xc5\x99\xc3\xadkalo mud\xc5\xbeahed\xc3\xbdni.'
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Occupation=='V\xc3\xa1le\xc4\x8dn\xc3\xadk':
            Player=self.Controller
            Count=2
            Opperation="* (Count + 100)/100 "
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class WillyBrandt:

    def __init__(self):
        self.Name = 'Willy Brandt'
        self.Occupation = 'Politik'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 50
        self.Assertivity = 50
        self.Money = 0
        self.Glory = 30
        self.Discipline = 0
        self.RulesToShow = 'Kdy\xc5\xbe tato postava p\xc5\x99ijde do hry, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class DEisenhower:

    def __init__(self):
        self.Name = 'D. Eisenhower'
        self.Occupation = 'Politik'
        self.Sociom = 'USA'
        self.Resiliance = 120
        self.Assertivity = 120
        self.Money = 0
        self.Glory = 35
        self.Discipline = 35
        self.RulesToShow = 'B\xc4\x9bhem sv\xc3\xa9ho tahu m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatiti 30 sl\xc3\xa1vy a dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =[]

    def Politics(self,Game,GameDelta):
        if Game.Phase=='Politics':
            GameDelta = {}
            Player=self.Controller
            Count=3
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class JFKennedy:

    def __init__(self):
        self.Name = 'J. F. Kennedy'
        self.Occupation = 'Politik'
        self.Sociom = 'USA'
        self.Resiliance = 70
        self.Assertivity = 70
        self.Money = 15
        self.Glory = 20
        self.Discipline = 15
        self.RulesToShow = 'B\xc4\x9bhem sv\xc3\xa9ho tahu m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit  20 sl\xc3\xa1vy a zv\xc3\xbd\xc5\xa1it svou mor\xc3\xa1lku o 90%.;'
        self.Controller = 0
        self.Legend = 'Legend\xc3\xa1rn\xc3\xad demokratick\xc3\xbd politik, kter\xc3\xbd v \xc5\xbeivot\xc4\x9b neprohr\xc3\xa1l jedin\xc3\xa9 volby. Do historie se zapsal dv\xc4\x9bma v\xc4\x9bcmi. Tou prvn\xc3\xad byla jeho \xc3\xba\xc4\x8dast p\xc5\x99i karibsk\xc3\xa9 krizi, kdy sv\xc4\x9bt po sov\xc4\x9btsk\xc3\xa9m um\xc3\xadst\xc4\x9bn\xc3\xad jadern\xc3\xbdch raket na Kubu balancoval na hran\xc4\x9b jadern\xc3\xa9 katastrofy. Kenedy jedn\xc3\xa1n\xc3\xad s Chru\xc5\xa1\xc4\x8dovem v\xc5\xa1ak hrozbu odvr\xc3\xa1tilo. Druh\xc3\xbdm v\xc3\xbdznamn\xc3\xbdm Kennedyho momentem byl atent\xc3\xa1t, kter\xc3\xbd na n\xc4\x9bj byl sp\xc3\xa1ch\xc3\xa1n v roce 1963. '
        self.Register =[]

    def Politics(self,Game,GameDelta):
        if Game.Phase=='Politics':
            GameDelta = {}
            Player=self.Controller
            Count=2
            Opperation="- Count"
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Count=9
            Opperation="* (Count + 100)/100 "
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class GeorgeMarshall:

    def __init__(self):
        self.Name = 'George Marshall'
        self.Occupation = 'Politik'
        self.Sociom = 'USA'
        self.Resiliance = 30
        self.Assertivity = 30
        self.Money = 20
        self.Glory = 20
        self.Discipline = 0
        self.RulesToShow = 'Na konci rud\xc3\xa9 expanze m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit 10 pen\xc4\x9bz a p\xc5\x99idat si 30 sl\xc3\xa1vy.;'
        self.Controller = 0
        self.Legend = 'Ministr zahrani\xc4\x8d\xc3\xad bez jeho\xc5\xbe n\xc3\xa1vrhu obnovit ekonomiky druhou sv\xc4\x9btovou v\xc3\xa1lku po\xc5\xa1kozen\xc3\xbdch evropsk\xc3\xbdch st\xc3\xa1t\xc5\xaf americk\xc3\xbdmi pen\xc4\x9bzi, aby tak Spojen\xc3\xa9 st\xc3\xa1ty z\xc3\xadskaly jednak odbyt pro sv\xc3\xa9 zbo\xc5\xbe\xc3\xad a druhak spojence, by asi Spojen\xc3\xa9 st\xc3\xa1ty byly b\xc4\x9bhem studen\xc3\xa9 v\xc3\xa1lky v\xc3\xbdrazn\xc4\x9b osam\xc4\x9blej\xc5\xa1\xc3\xad.'
        self.Register =[]

    def Reformation(self,Game,GameDelta):
        if Game.Phase=='Reformation':
            GameDelta = {}
            Player=self.Controller
            Count=1
            Opperation="- Count"
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Player=self.Controller
            Count=3
            Opperation="+ Count"
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class JanPavelII:

    def __init__(self):
        self.Name = 'Jan Pavel II.'
        self.Occupation = 'Duchovn\xc3\xad'
        self.Sociom = 'Vatik\xc3\xa1n'
        self.Resiliance = 90
        self.Assertivity = 40
        self.Money = 0
        self.Glory = 25
        self.Discipline = 25
        self.RulesToShow = 'Kdy\xc5\xbe tato postava p\xc5\x99ijde do hry, dostane\xc5\xa1 30 sl\xc3\xa1vy.;'
        self.Controller = 0
        self.Legend = 'Jan Pavel II. byl v\xc5\xafbec prvn\xc3\xadm (a dosud tak\xc3\xa9 posledn\xc3\xadm) slovansk\xc3\xbdm, konkr\xc3\xa9tn\xc4\x9b polsk\xc3\xbdm, pape\xc5\xbeem. Nutno podotknout, \xc5\xbee jeho pontifik\xc3\xa1t p\xc5\x99i\xc5\xa1el ve spr\xc3\xa1vn\xc3\xbd \xc4\x8das. SSSR osmdes\xc3\xa1t\xc3\xbdch let byl oslaben\xc3\xbd v\xc3\xa1lkou v Afgh\xc3\xa1nist\xc3\xa1nu i v\xc3\xbdbuchem \xc4\x8cernobylu, co\xc5\xbe sk\xc3\xbdtalo "ide\xc3\xa1ln\xc3\xad" podm\xc3\xadnky pro v\xc5\xa1echny st\xc3\xa1ty, kter\xc3\xa9 se cht\xc4\x9bly trochu vymanit z jeho podru\xc4\x8d\xc3\xad. Pro Pol\xc3\xa1ky byl "jejich" pape\xc5\xbe nad\xc4\x9bjnou p\xc5\x99ipom\xc3\xadnkou toho, \xc5\xbee pro n\xc4\x9b na z\xc3\xa1pad\xc4\x9b je m\xc3\xadsto.'
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=3
            Opperation="+ Count"
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class KonradAdenauer:

    def __init__(self):
        self.Name = 'Konrad Adenauer'
        self.Occupation = 'Politik'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 70
        self.Assertivity = 20
        self.Money = 20
        self.Glory = 0
        self.Discipline = 30
        self.RulesToShow = 'B\xc4\x9bhem sv\xc3\xa9ho tahu m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit deset sl\xc3\xa1vy a p\xc5\x99idat si  dvacet pen\xc4\x9bz.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =[]

    def Politics(self,Game,GameDelta):
        if Game.Phase=='Politics':
            GameDelta = {}
            Player=self.Controller
            Count=1
            Opperation="- Count"
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Player=self.Controller
            Count=2
            Opperation="+ Count"
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class HelmutKohl:

    def __init__(self):
        self.Name = 'Helmut Kohl'
        self.Occupation = 'Politik'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 80
        self.Assertivity = 50
        self.Money = 30
        self.Glory = 0
        self.Discipline = 30
        self.RulesToShow = 'Kdy\xc5\xbe tato postava triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, l\xc3\xadzni si kartu.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            pId=Game.players[self.Controller]
            Player=self.Controller
            GameDelta = Game.DrawCard(pId,Player,GameDelta)
            return GameDelta

class WLMKing:

    def __init__(self):
        self.Name = 'W. L. M. King'
        self.Occupation = 'Politik'
        self.Sociom = 'Kanada'
        self.Resiliance = 100
        self.Assertivity = 20
        self.Money = 20
        self.Glory = 0
        self.Discipline = 50
        self.RulesToShow = 'Kdykoliv n\xc4\x9bjak\xc3\xbd tv\xc5\xafj politik triumfuje rud\xc3\xa9ho p\xc5\x99edstavitele, l\xc3\xadzni si kartu.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        pId=Game.players[self.Controller]
        Player=self.Controller
        GameDelta = Game.DrawCard(pId,Player,GameDelta)
        return GameDelta

class Mosad:

    def __init__(self):
        self.Name = 'Mosad'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Izrael'
        self.Resiliance = 30
        self.Assertivity = 80
        self.Money = 30
        self.Glory = 20
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv se tato postava st\xc5\x99etne s v\xc3\xbdchodn\xc3\xadm politikem, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = 'Izraelsk\xc3\xa1 tajn\xc3\xa1 b\xc4\x9bhem t\xc4\x9bch \xc4\x8dty\xc4\x8diceti let, co trvala studen\xc3\xa1 v\xc3\xa1lka, stihla prov\xc3\xa9st spoustu mimo\xc5\x99\xc3\xa1dn\xc4\x9b poveden\xc3\xbdch kousk\xc5\xaf. Nejen, \xc5\xbee v Argentin\xc4\x9b na\xc5\xa1la nacistick\xc3\xa9ho zlo\xc4\x8dince Adolfa Eichmana a dopravila ho k soudu, pop\xc5\x99\xc3\xadpad\xc4\x9b dostala sv\xc3\xa9ho \xc5\xa1pi\xc3\xb3na Eliho Kohena do syrsk\xc3\xbdch vl\xc3\xa1dn\xc3\xadch kruh\xc5\xaf, ale tak\xc3\xa9 byla tou, p\xc5\x99es n\xc3\xad\xc5\xbe se na z\xc3\xa1pad dostal Chru\xc5\xa1\xc4\x8dov\xc5\xafv projev, ve kter\xc3\xa9m kritizoval Stalina (co\xc5\xbe vedlo k zna\xc4\x8dn\xc3\xa9 deziluzi z\xc3\xa1padn\xc3\xadch p\xc5\x99\xc3\xadznivc\xc5\xaf komunismu).'
        self.Register =['Conflict']

    def Conflict(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            if Communist.Occupation=='Politik':
                Player=self.Controller
                Count=1
                GameDelta = Game.GetSDI(Player,Count,GameDelta)
                return GameDelta

class DBGurion:

    def __init__(self):
        self.Name = 'D. B. Gurion'
        self.Occupation = 'Politik'
        self.Sociom = 'Izrael'
        self.Resiliance = 70
        self.Assertivity = 60
        self.Money = 0
        self.Glory = 0
        self.Discipline = 40
        self.RulesToShow = 'Kdykoliv jsi ovlivn\xc4\x9bn v\xc3\xbdchodn\xc3\xadm p\xc5\x99edstavitelem, dostane\xc5\xa1 20 mor\xc3\xa1lky.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['RedTriumph']

    def RedTriumph(self,Game,Communist,GameDelta):
        Player=self.Controller
        Count=2
        Opperation="+ Count"
        Commodity="Discipline"
        GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
        return GameDelta

class JicchakRabin:

    def __init__(self):
        self.Name = 'Jicchak Rabin'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Izrael'
        self.Resiliance = 50
        self.Assertivity = 40
        self.Money = 0
        self.Glory = 20
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv tv\xc3\xa1 postava z Izraele triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Sociom=='Izrael' and Figure.Controller==self.Controller:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class RichardNixon:

    def __init__(self):
        self.Name = 'Richard Nixon'
        self.Occupation = 'Politik'
        self.Sociom = 'USA'
        self.Resiliance = 20
        self.Assertivity = 60
        self.Money = 15
        self.Glory = 15
        self.Discipline = 0
        self.RulesToShow = 'Na konci rud\xc3\xa9 expanze m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit 20 mor\xc3\xa1lky a l\xc3\xadznout si kartu.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =[]

    def Reformation(self,Game,GameDelta):
        if Game.Phase=='Reformation':
            GameDelta = {}
            Player=self.Controller
            Count=2
            Opperation="- Count"
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Player=self.Controller
            GameDelta = Game.DrawCard(pId,Player,GameDelta)
            return GameDelta

class JanXXIII:

    def __init__(self):
        self.Name = 'Jan XXIII.'
        self.Occupation = 'Duchovn\xc3\xad'
        self.Sociom = 'Vatik\xc3\xa1n'
        self.Resiliance = 30
        self.Assertivity = 30
        self.Money = 0
        self.Glory = 0
        self.Discipline = 20
        self.RulesToShow = 'Kdykoliv p\xc5\x99ijde Duchovn\xc3\xad do hry, dostane\xc5\xa1 60 stabilit.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Occupation=='Duchovn\xc3\xad':
            Player=self.Controller
            Count=6
            Opperation="+ Count"
            Commodity="Lives"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class NeilArmstrong:

    def __init__(self):
        self.Name = 'Neil Armstrong'
        self.Occupation = 'Kosmanaut'
        self.Sociom = 'USA'
        self.Resiliance = 20
        self.Assertivity = 60
        self.Money = 10
        self.Glory = 10
        self.Discipline = 10
        self.RulesToShow = 'Kdykoliv tato postava triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class LudwigErdhart:

    def __init__(self):
        self.Name = 'Ludwig Erdhart'
        self.Occupation = 'Politik'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 40
        self.Assertivity = 20
        self.Money = 20
        self.Glory = 0
        self.Discipline = 0
        self.RulesToShow = 'Kdy\xc5\xbe tato postava p\xc5\x99ijde do hry, zv\xc3\xbd\xc5\xa1\xc3\xad se tv\xc3\xa9 pen\xc3\xadze o 90%.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=9
            Opperation="* (Count + 100)/100 "
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class HenryKissinger:

    def __init__(self):
        self.Name = 'Henry Kissinger'
        self.Occupation = 'Diplomat'
        self.Sociom = 'USA'
        self.Resiliance = 50
        self.Assertivity = 50
        self.Money = 0
        self.Glory = 20
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv se tato postava st\xc5\x99etne s v\xc3\xbdchodn\xc3\xadm politikem, l\xc3\xadzni si kartu.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['Conflict']

    def Conflict(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            if Communist.Occupation=='Politik':
                pId=Game.players[self.Controller]
                Player=self.Controller
                GameDelta = Game.DrawCard(pId,Player,GameDelta)
                return GameDelta

class HelmutSchmidt:

    def __init__(self):
        self.Name = 'Helmut Schmidt'
        self.Occupation = 'Politik'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 50
        self.Assertivity = 70
        self.Money = 20
        self.Glory = 20
        self.Discipline = 20
        self.RulesToShow = 'Kdykoliv p\xc5\x99ijde tv\xc3\xa1 postava z USA do hry, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = 'Koncem sedmdes\xc3\xa1t\xc3\xbdch letse soci\xc3\xa1ln\xc4\x9b-demokratick\xc3\xbd politik Helmut Schmidt stal kancl\xc3\xa9\xc5\x99em SRN a ud\xc4\x9blal \xc5\x99adu krok\xc5\xaf, kter\xc3\xa9 by \xc4\x8dlov\xc4\x9bk od levicov\xc3\xa9ho politika rozhodn\xc4\x9b ne\xc4\x8dekal. Nejnen, \xc5\xbee do vl\xc3\xa1dn\xc3\xad koalice p\xc5\x99ibral pom\xc4\x9brn\xc4\x9b pravicovou FDP, ale tak\xc3\xa9 velmi se\xc5\xa1krtal st\xc3\xa1tn\xc3\xad v\xc3\xbddaje (sedmdes\xc3\xa1t\xc3\xa1 l\xc3\xa9ta prov\xc3\xa1zela velk\xc3\xa1 celosv\xc4\x9btov\xc3\xa1 ekonomick\xc3\xa1 krize), podobn\xc4\x9b jako Tatcherov\xc3\xa1 v Brit\xc3\xa1nii nebo Reagan v USA. Tato ekonomick\xc3\xa1 opat\xc5\x99en\xc3\xad zafungovala a vynesla Schmidta na nejvy\xc5\xa1\xc5\xa1\xc3\xad p\xc5\x99\xc3\xad\xc4\x8dky \xc5\xbeeb\xc5\x99\xc3\xad\xc4\x8dk\xc5\xaf hodnot\xc3\xadchch n\xc4\x9bmeck\xc3\xa9 kancl\xc3\xa9\xc5\x99e. I p\xc5\x99esto v\xc5\xa1ak jeho vl\xc3\xa1da trvala pouze na n\xc4\x9bmeck\xc3\xa9 pom\xc4\x9bry kr\xc3\xa1tk\xc3\xbdch osm let. Ve\xc5\x99ejnost se proti n\xc4\x9bmu obr\xc3\xa1tila, kdy\xc5\xbe se rozhodl, \xc5\xbee nech\xc3\xa1 Ameri\xc4\x8dny um\xc3\xadstit jadern\xc3\xa9 rakety, aby tak vyv\xc3\xa1\xc5\xbeil p\xc5\x99evahu, kterou v nich do t\xc3\xa9 doby dr\xc5\xbeeli Sov\xc4\x9bti. Tento kontroverzn\xc3\xad krok nejen, \xc5\xbee vedl k jeho konci ve funkci kancl\xc3\xa9\xc5\x99e, ale tak\xc3\xa9 p\xc5\x99im\xc4\x9bl Schmidtovou politikou znepokojen\xc3\xa9 soci\xc3\xa1ln\xc3\xad demokraty k zalo\xc5\xbeen\xc3\xad strany Zelen\xc3\xbdch.'
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Sociom=='USA' and Figure.Controller==self.Controller:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class CharlesdeGaulle:

    def __init__(self):
        self.Name = 'Charles de Gaulle'
        self.Occupation = 'Politik'
        self.Sociom = 'Francie'
        self.Resiliance = 90
        self.Assertivity = 90
        self.Money = 0
        self.Glory = 40
        self.Discipline = 10
        self.RulesToShow = 'Kdy\xc5\xbe p\xc5\x99ijde tato postava do hry, dostane\xc5\xa1 40 sl\xc3\xa1vy.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=4
            Opperation="+ Count"
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class PierreTrudeau:

    def __init__(self):
        self.Name = 'Pierre Trudeau'
        self.Occupation = 'Politik'
        self.Sociom = 'Kanada'
        self.Resiliance = 40
        self.Assertivity = 70
        self.Money = 10
        self.Glory = 15
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv jsi ovlivn\xc4\x9bn v\xc3\xbdchodn\xc3\xadm p\xc5\x99edstavitelem, l\xc3\xadzni si kartu.;'
        self.Controller = 0
        self.Legend = 'Tento sv\xc3\xa9r\xc3\xa1zn\xc3\xbd kanadsk\xc3\xbd premi\xc3\xa9r (a mimo jin\xc3\xa9 otec sou\xc4\x8dasn\xc3\xa9ho premi\xc3\xa9ra J. Trudeaua) si v\xc2\xa0zahrani\xc4\x8dn\xc3\xad politice razil svou vlastn\xc3\xad cestu. Nejen, \xc5\xbee proslul sj\xc3\xad\xc5\xbed\xc4\x9bn\xc3\xadm z\xc3\xa1bradl\xc3\xad po boku a piruetou za z\xc3\xa1dy Al\xc5\xbeb\xc4\x9bty II. (kter\xc3\xa1 je nejen britskou, ale tak\xc3\xa9 kanadskou kr\xc3\xa1lovnou), n\xc3\xbdbr\xc5\xbe se tak\xc3\xa9 velmi p\xc5\x99\xc3\xa1telil s\xc2\xa0Fidelem Castrem. Rozhodn\xc4\x9b v\xc5\xa1ak nem\xc4\x9bl v\xc2\xa0pl\xc3\xa1nu opou\xc5\xa1t\xc4\x9bt NATO a pop\xc5\x99\xc3\xadpad\xc4\x9b jakkoliv naru\xc5\xa1ovat kandadsko-americk\xc3\xa9 spojenectv\xc3\xad.'
        self.Register =['RedTriumph']

    def RedTriumph(self,Game,Communist,GameDelta):
        pId=Game.players[self.Controller]
        Player=self.Controller
        GameDelta = Game.DrawCard(pId,Player,GameDelta)
        return GameDelta

class AugustoPinochet:

    def __init__(self):
        self.Name = 'Augusto Pinochet'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Chile'
        self.Resiliance = 80
        self.Assertivity = 100
        self.Money = 35
        self.Glory = 20
        self.Discipline = 0
        self.RulesToShow = 'B\xc4\x9bhem sv\xc3\xa9ho tahu m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit 20 mor\xc3\xa1lky a zv\xc3\xbd\xc5\xa1it sv\xc3\xa9 pen\xc3\xadze o  90%.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =[]

    def Politics(self,Game,GameDelta):
        if Game.Phase=='Politics':
            GameDelta = {}
            Player=self.Controller
            Count=2
            Opperation="- Count"
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Count=9
            Opperation="* (Count + 100)/100 "
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class VGdeEstaing:

    def __init__(self):
        self.Name = 'V. G. de Estaing'
        self.Occupation = 'Politik'
        self.Sociom = 'Francie'
        self.Resiliance = 60
        self.Assertivity = 50
        self.Money = 30
        self.Glory = 0
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv p\xc5\x99ijde tv\xc3\xa1 postava z N\xc4\x9bmecka do hry, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = 'Nen\xc3\xad \xc5\xbe\xc3\xa1dn\xc3\xa9 tajemstv\xc3\xad, \xc5\xbee dva podobn\xc4\x9b siln\xc3\xa9 sousedn\xc3\xad n\xc3\xa1rody se v d\xc4\x9bjin\xc3\xa1ch lidstva sn\xc3\xa1\xc5\xa1ely t\xc4\x9b\xc5\xbeko. N\xc4\x9bmecko a Francie toho byly skv\xc4\x9bl\xc3\xbdm d\xc5\xafkazem a asi nikoho nep\xc5\x99ekvapilo, \xc5\xbee druh\xc3\xa1 sv\xc4\x9btov\xc3\xa1 v\xc3\xa1lka jejich vz\xc3\xa1jemn\xc3\xa9 l\xc3\xa1sce p\xc5\x99\xc3\xadli\xc5\xa1 neprosp\xc4\x9bla. I p\xc5\x99esto se v\xc5\xa1ak z\xc3\xa1padn\xc3\xad N\xc4\x9bmecko s Franci\xc3\xad v n\xc3\xa1sleduj\xc3\xadc\xc3\xadch letech velmi sbl\xc3\xad\xc5\xbeily v r\xc3\xa1mci v\xc5\xa1emo\xc5\xben\xc3\xbdch projekt\xc5\xaf evropsk\xc3\xa9 integrace. Tento francouzsk\xc3\xbd politik vl\xc3\xa1dnouc\xc3\xad na konci 70. let na nich m\xc4\x9bl, spolu se sv\xc3\xbdm p\xc5\x99\xc3\xadtelem n\xc4\x9bmeck\xc3\xbdm kancl\xc3\xa9\xc5\x99em Helmutem Schmidtem, lv\xc3\xad pod\xc3\xadl. Za jeho vl\xc3\xa1dy vznikla nap\xc5\x99\xc3\xadklad Evropsk\xc3\xa1 rada nebo p\xc5\xafda pro spole\xc4\x8dnou m\xc4\x9bnu.'
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Sociom=='N\xc4\x9bmecko' and Figure.Controller==self.Controller:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class Contras:

    def __init__(self):
        self.Name = 'Contras'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Nikaragua'
        self.Resiliance = 30
        self.Assertivity = 100
        self.Money = 30
        self.Glory = 0
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv tato postava triumfuje v\xc3\xbdchodn\xc3\xadho v\xc3\xa1le\xc4\x8dn\xc3\xadka, zv\xc3\xbd\xc5\xa1\xc3\xad se tv\xc3\xa9 pen\xc3\xadze o 30%.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            if Communist.Occupation=='V\xc3\xa1le\xc4\x8dn\xc3\xadk':
                Player=self.Controller
                Count=3
                Opperation="* (Count + 100)/100 "
                Commodity="Money"
                GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
                return GameDelta

class Alxc5xbebxc4x9btaII:

    def __init__(self):
        self.Name = 'Al\xc5\xbeb\xc4\x9bta II.'
        self.Occupation = 'Politik'
        self.Sociom = 'VB'
        self.Resiliance = 120
        self.Assertivity = 10
        self.Money = 20
        self.Glory = 0
        self.Discipline = 10
        self.RulesToShow = 'B\xc4\x9bhem sv\xc3\xa9ho tahu m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit 10 pen\xc4\x9bz a dostane\xc5\xa1 20 stabilit.;'
        self.Controller = 0
        self.Legend = 'A\xc4\x8dkoliv Brit\xc3\xa1nie v\xc2\xa0druh\xc3\xa9 sv\xc4\x9btov\xc3\xa9 v\xc3\xa1lce zv\xc3\xadt\xc4\x9bzila, byla pro ni n\xc3\xa1sleduj\xc3\xadc\xc3\xad desetilet\xc3\xad pom\xc4\x9brn\xc4\x9b sv\xc3\xadzeln\xc3\xa1. Zpo\xc4\x8d\xc3\xa1tku rozbombardovan\xc3\xa1 a zchudl\xc3\xa1 zem\xc4\x9b se musela postavit na nohy a je\xc5\xa1t\xc4\x9b k\xc2\xa0tomu spl\xc3\xa1cet Ameri\xc4\x8dan\xc5\xafm b\xc4\x9bhem v\xc3\xa1lky nast\xc5\x99\xc3\xa1dan\xc3\xa9 dluhy, z\xc3\xa1rove\xc5\x88 bylo t\xc5\x99eba \xc5\x99adou soci\xc3\xa1ln\xc3\xadch d\xc3\xa1vek a nov\xc3\xbdch pr\xc3\xa1v vyhnat d\xc4\x9bln\xc3\xadk\xc5\xafm z\xc2\xa0hlavy pokukov\xc3\xa1n\xc3\xad ke komunismu. Snad v\xc2\xa0tom v\xc5\xa1em britsk\xc3\xa9mu lidu aspo\xc5\x88 trochu pomohlo, \xc5\xbee se jej hlava st\xc3\xa1tu v\xc5\xbedy sna\xc5\xbeila spojovat a ne roze\xc5\xa1tv\xc3\xa1vat proti sob\xc4\x9b.'
        self.Register =[]

    def Politics(self,Game,GameDelta):
        if Game.Phase=='Politics':
            GameDelta = {}
            Player=self.Controller
            Count=1
            Opperation="- Count"
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Player=self.Controller
            Count=2
            Opperation="+ Count"
            Commodity="Lives"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class DouglesMcArthur:

    def __init__(self):
        self.Name = 'Dougles McArthur'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'USA'
        self.Resiliance = 90
        self.Assertivity = 90
        self.Money = 45
        self.Glory = 0
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv se tato postava st\xc5\x99etne s v\xc3\xbdchodn\xc3\xadm p\xc5\x99edstavitelem, dostane\xc5\xa1 90 stabilit; Kdykoliv tato postava triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, dostane\xc5\xa1 bod SDI;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['Conflict', 'EastDeath']

    def Conflict(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=9
            Opperation="+ Count"
            Commodity="Lives"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta
    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class HarrySTruman:

    def __init__(self):
        self.Name = 'Harry S. Truman'
        self.Occupation = 'Politik'
        self.Sociom = 'USA'
        self.Resiliance = 100
        self.Assertivity = 100
        self.Money = 15
        self.Glory = 25
        self.Discipline = 25
        self.RulesToShow = 'Kdykoliv jsi ovlivn\xc4\x9bn v\xc3\xbdchodn\xc3\xadm p\xc5\x99edstavitelem, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['RedTriumph']

    def RedTriumph(self,Game,Communist,GameDelta):
        Player=self.Controller
        Count=1
        GameDelta = Game.GetSDI(Player,Count,GameDelta)
        return GameDelta

class xc4x8cankajxc5xa1ek:

    def __init__(self):
        self.Name = '\xc4\x8cankaj\xc5\xa1ek'
        self.Occupation = 'Politik'
        self.Sociom = 'Taiwan'
        self.Resiliance = 60
        self.Assertivity = 30
        self.Money = 0
        self.Glory = 20
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv jsi ovlivn\xc4\x9bn v\xc3\xbdchodn\xc3\xadm v\xc3\xa1le\xc4\x8dn\xc3\xadkem, dostane\xc5\xa1 40 stabilit; Kdykoliv tato postava triumfuje v\xc3\xbdchodn\xc3\xadho p\xc5\x99edstavitele, dostane\xc5\xa1 bod SDI;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['RedTriumph', 'EastDeath']

    def RedTriumph(self,Game,Communist,GameDelta):
        if Communist.Occupation=='V\xc3\xa1le\xc4\x8dn\xc3\xadk':
            Player=self.Controller
            Count=4
            Opperation="+ Count"
            Commodity="Lives"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta
    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            Player=self.Controller
            Count=1
            GameDelta = Game.GetSDI(Player,Count,GameDelta)
            return GameDelta

class xc5xa0igeruJoxc5xa1ida:

    def __init__(self):
        self.Name = '\xc5\xa0igeru Jo\xc5\xa1ida'
        self.Occupation = 'Politik'
        self.Sociom = 'Japonsko'
        self.Resiliance = 40
        self.Assertivity = 40
        self.Money = 10
        self.Glory = 10
        self.Discipline = 10
        self.RulesToShow = 'B\xc4\x9bhem sv\xc3\xa9ho tahu m\xc5\xaf\xc5\xbee\xc5\xa1 zaplatit 10 mor\xc3\xa1lky a zv\xc3\xbd\xc5\xa1it sv\xc3\xa9 pen\xc3\xadze o  40%.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =[]

    def Politics(self,Game,GameDelta):
        if Game.Phase=='Politics':
            GameDelta = {}
            Player=self.Controller
            Count=1
            Opperation="- Count"
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            Count=4
            Opperation="* (Count + 100)/100 "
            Commodity="Money"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class LechWalesa:

    def __init__(self):
        self.Name = 'Lech Walesa'
        self.Occupation = 'Disident'
        self.Sociom = 'Polsko'
        self.Resiliance = 30
        self.Assertivity = 60
        self.Money = 0
        self.Glory = 0
        self.Discipline = 20
        self.RulesToShow = 'Kdykoliv tato postava triumfuje v\xc3\xbdchodn\xc3\xadho v\xc3\xa1le\xc4\x8dn\xc3\xadka, dostane\xc5\xa1 bod SDI.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['EastDeath']

    def EastDeath(self,Game,Figure,Communist,GameDelta):
        if Figure.Name==self.Name:
            if Communist.Occupation=='V\xc3\xa1le\xc4\x8dn\xc3\xadk':
                Player=self.Controller
                Count=1
                GameDelta = Game.GetSDI(Player,Count,GameDelta)
                return GameDelta

class ISungman:

    def __init__(self):
        self.Name = 'I Sung-man'
        self.Occupation = 'Politik'
        self.Sociom = 'Ji\xc5\xben\xc3\xad Korea'
        self.Resiliance = 80
        self.Assertivity = 30
        self.Money = 20
        self.Glory = 0
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv dostane\xc5\xa1 bod SDI, zv\xc3\xbd\xc5\xa1\xc3\xad se tv\xc3\xa1 stabilita o 80%.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['GainedSDI']

    def GainedSDI(self,Game,Player,GameDelta):
        if Player==Game.players[self.Controller]:
            Player=self.Controller
            Count=8
            Opperation="* (Count + 100)/100 "
            Commodity="Lives"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class ViktorOrbxc3xa1n:

    def __init__(self):
        self.Name = 'Viktor Orb\xc3\xa1n'
        self.Occupation = 'Disident'
        self.Sociom = 'Ma\xc4\x8farsko'
        self.Resiliance = 40
        self.Assertivity = 50
        self.Money = 25
        self.Glory = 0
        self.Discipline = 0
        self.RulesToShow = 'Kdykoliv si l\xc3\xadzne\xc5\xa1 kartu, dostane\xc5\xa1 10 sl\xc3\xa1vy.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['DrawnCard']

    def DrawnCard(self,Game,Player,GameDelta):
        if Player==Game.players[self.Controller]:
            Player=self.Controller
            Count=1
            Opperation="+ Count"
            Commodity="Glory"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class Vxc3xa1clavHavel:

    def __init__(self):
        self.Name = 'V\xc3\xa1clav Havel'
        self.Occupation = 'Disident'
        self.Sociom = '\xc4\x8ceskoslovensko'
        self.Resiliance = 30
        self.Assertivity = 30
        self.Money = 0
        self.Glory = 0
        self.Discipline = 15
        self.RulesToShow = 'Kdykoliv jsi ovlivn\xc4\x9bn v\xc3\xbdchodn\xc3\xadm politikem, dostane\xc5\xa1 30 stabilit.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['RedTriumph']

    def RedTriumph(self,Game,Communist,GameDelta):
        if Communist.Occupation=='Politik':
            Player=self.Controller
            Count=3
            Opperation="+ Count"
            Commodity="Lives"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta

class MartinLKing:

    def __init__(self):
        self.Name = 'Martin L. King'
        self.Occupation = 'Duchovn\xc3\xad'
        self.Sociom = 'USA'
        self.Resiliance = 25
        self.Assertivity = 60
        self.Money = 0
        self.Glory = 0
        self.Discipline = 30
        self.RulesToShow = 'Kdykoliv p\xc5\x99ijde tv\xc3\xa1 postava do hry, dostane\xc5\xa1 10 mor\xc3\xa1lky.;'
        self.Controller = 0
        self.Legend = ' '
        self.Register =['NewFigure']

    def NewFigure(self,Game,Figure,GameDelta):
        if Figure.Controller==self.Controller:
            Player=self.Controller
            Count=1
            Opperation="+ Count"
            Commodity="Discipline"
            GameDelta = Game.AlterComs(Player,Count,Opperation,Commodity,GameDelta)
            return GameDelta
def CreateDeck():
    c0=MargretTatcherovxc3xa1()
    c1=RonaldReagan()
    c2=UsamabinLadin()
    c3=Mudxc5xbeahedxc3xbdni()
    c4=WillyBrandt()
    c5=DEisenhower()
    c6=JFKennedy()
    c7=GeorgeMarshall()
    c8=JanPavelII()
    c9=KonradAdenauer()
    c10=HelmutKohl()
    c11=WLMKing()
    c12=Mosad()
    c13=DBGurion()
    c14=JicchakRabin()
    c15=RichardNixon()
    c16=JanXXIII()
    c17=NeilArmstrong()
    c18=LudwigErdhart()
    c19=HenryKissinger()
    c20=HelmutSchmidt()
    c21=CharlesdeGaulle()
    c22=PierreTrudeau()
    c23=AugustoPinochet()
    c24=VGdeEstaing()
    c25=Contras()
    c26=Alxc5xbebxc4x9btaII()
    c27=DouglesMcArthur()
    c28=HarrySTruman()
    c29=xc4x8cankajxc5xa1ek()
    c30=xc5xa0igeruJoxc5xa1ida()
    c31=LechWalesa()
    c32=ISungman()
    c33=ViktorOrbxc3xa1n()
    c34=Vxc3xa1clavHavel()
    c35=MartinLKing()
    return[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35]
class FidelCastro:

    def __init__(self):
        self.Name = 'Fidel Castro'
        self.Occupation = 'Politik'
        self.Sociom = 'Kuba'
        self.Resiliance = 30
        self.Assertivity = 80
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class NikitaChruxc5xa1xc4x8dov:

    def __init__(self):
        self.Name = 'Nikita Chru\xc5\xa1\xc4\x8dov'
        self.Occupation = 'Politik'
        self.Sociom = 'SSSR'
        self.Resiliance = 70
        self.Assertivity = 70
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class LeonidBrexc5xbenxc4x9bv:

    def __init__(self):
        self.Name = 'Leonid Bre\xc5\xben\xc4\x9bv'
        self.Occupation = 'Politik'
        self.Sociom = 'SSSR'
        self.Resiliance = 90
        self.Assertivity = 90
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class AndrejBabixc5xa1:

    def __init__(self):
        self.Name = 'Andrej Babi\xc5\xa1'
        self.Occupation = 'Obchodn\xc3\xadk'
        self.Sociom = '\xc4\x8ceskoslovensko'
        self.Resiliance = 10
        self.Assertivity = 5
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = 'Pozd\xc4\x9bj\xc5\xa1\xc3\xad \xc4\x8desk\xc3\xbd premi\xc3\xa9r Andrej Babi\xc5\xa1 byl v dob\xc4\x9b studen\xc3\xa9 v\xc3\xa1lky zcela bezv\xc3\xbdznamnou figurkou. Aktivn\xc4\x9b spolupracoval s komunistickou stranou, ale p\xc5\x99edev\xc5\xa1\xc3\xadm kv\xc5\xafli tomu, aby ho nechala obchodovat se z\xc3\xa1padem. I tak je dobr\xc3\xa9 si p\xc5\x99ipom\xc3\xadnat, na kter\xc3\xa9 stran\xc4\x9b tehdy st\xc3\xa1l...'

class GustavHusxc3xa1k:

    def __init__(self):
        self.Name = 'Gustav Hus\xc3\xa1k'
        self.Occupation = 'Politik'
        self.Sociom = '\xc4\x8ceskoslovensko'
        self.Resiliance = 70
        self.Assertivity = 20
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class JurijGagarin:

    def __init__(self):
        self.Name = 'Jurij Gagarin'
        self.Occupation = 'Kosmonaut'
        self.Sociom = 'SSSR'
        self.Resiliance = 20
        self.Assertivity = 60
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class KlementGottwald:

    def __init__(self):
        self.Name = 'Klement Gottwald'
        self.Occupation = 'Politik'
        self.Sociom = '\xc4\x8ceskoslovensko'
        self.Resiliance = 60
        self.Assertivity = 60
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class Hoxc4x8ciMin:

    def __init__(self):
        self.Name = 'Ho \xc4\x8ci Min'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Vietnam'
        self.Resiliance = 120
        self.Assertivity = 30
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class CheGuevara:

    def __init__(self):
        self.Name = 'Che Guevara'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Kuba'
        self.Resiliance = 20
        self.Assertivity = 60
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class Jxc3xa1nosKxc3xa1dxc3xa1r:

    def __init__(self):
        self.Name = 'J\xc3\xa1nos K\xc3\xa1d\xc3\xa1r'
        self.Occupation = 'Politik'
        self.Sociom = 'Ma\xc4\x8farsko'
        self.Resiliance = 40
        self.Assertivity = 40
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class WojciechJaruzelski:

    def __init__(self):
        self.Name = 'Wojciech Jaruzelski'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'Polsko'
        self.Resiliance = 20
        self.Assertivity = 90
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class Wxc5x82adysxc5x82awGomuxc5x82ka:

    def __init__(self):
        self.Name = 'W\xc5\x82adys\xc5\x82aw Gomu\xc5\x82ka'
        self.Occupation = 'Politik'
        self.Sociom = 'Polsko'
        self.Resiliance = 40
        self.Assertivity = 40
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class ErichHonecker:

    def __init__(self):
        self.Name = 'Erich Honecker'
        self.Occupation = 'Politik'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 80
        self.Assertivity = 40
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class LPBerija:

    def __init__(self):
        self.Name = 'L. P. Berija'
        self.Occupation = 'Politik'
        self.Sociom = 'SSSR'
        self.Resiliance = 50
        self.Assertivity = 50
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class RAF:

    def __init__(self):
        self.Name = 'RAF'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 30
        self.Assertivity = 50
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = 'Kdo v\xc3\xad, zda by se bez t\xc3\xa9to krajn\xc4\x9b levicov\xc3\xa9 teroristick\xc3\xa9 organizace (cel\xc3\xbdm n\xc3\xa1zvem: Frakce Rud\xc3\xa9 arm\xc3\xa1dy) nedo\xc5\xbeil n\xc4\x9bmeck\xc3\xbd kancl\xc3\xa9\xc5\x99 Helmut Schmidt v\xc3\xadce jak sto let. Pr\xc3\xa1v\xc4\x9b za jeho vl\xc3\xa1dy, tj. koncem 60. let, toti\xc5\xbe toto uskupen\xc3\xad trestalo SRN za podporu Ameri\xc4\x8dan\xc5\xaf ve v\xc3\xa1lce ve Vietnamu s\xc3\xa9ri\xc3\xad bombov\xc3\xbdch \xc3\xbatok\xc5\xaf. A te\xc4\x8f k\xc2\xa0tomu Schmidtovi \xe2\x80\x93 jednalo se v\xc3\xa1\xc5\xa1niv\xc3\xa9ho ku\xc5\x99\xc3\xa1ka a p\xc5\x99itom, s\xc2\xa0jak\xc3\xbdmi probl\xc3\xa9my se za sv\xc3\xa9 vl\xc3\xa1dy pot\xc3\xbdkal, to nen\xc3\xad velk\xc3\xbd div. Mo\xc5\xben\xc3\xa1, \xc5\xbee neb\xc3\xbdt RAF a stresu, kter\xc3\xbd mu p\xc5\x99ivodila, by \xc5\xbeil o ty t\xc5\x99i roky, kter\xc3\xa9 mu v\xc2\xa0dob\xc4\x9b smrti do stovky zb\xc3\xbdvaly, d\xc3\xa9le.  '

class Gxc3xbcnterGuillaume:

    def __init__(self):
        self.Name = 'G\xc3\xbcnter Guillaume'
        self.Occupation = 'Agent'
        self.Sociom = 'N\xc4\x9bmecko'
        self.Resiliance = 10
        self.Assertivity = 80
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = 'Kdy\xc5\xbe se pod\xc3\xadv\xc3\xa1me na historii posledn\xc3\xadch n\xc4\x9bkolika desetilet\xc3\xad, m\xc5\xaf\xc5\xbeeme se \xc5\x99\xc3\xadct, \xc5\xbee pokud n\xc4\x9bjak\xc3\xbd europoidn\xc3\xad n\xc3\xa1rod d\xc4\x9blal v\xc4\x9bci opravdu po\xc5\x99\xc3\xa1dn\xc4\x9b, pak to byli Izrael\xc5\xa1t\xc3\xad \xc5\xbdid\xc3\xa9 a N\xc4\x9bmci, sv\xc3\xa9ho \xc4\x8dasu jedin\xc3\xad ve v\xc3\xbdchodn\xc3\xadm bloku. Pr\xc3\xa1v\xc4\x9b t\xc4\x9bm se poda\xc5\x99il asi nejzda\xc5\x99ilej\xc5\xa1\xc3\xad \xc5\xa1pion\xc3\xa1\xc5\xben\xc3\xad kousek v d\xc4\x9bjin\xc3\xa1ch, kdy\xc5\xbe sv\xc3\xa9ho \xc5\xa1pi\xc3\xb3na G\xc3\xbcntera Guillaumeho prost\xc5\x99ednictv\xc3\xadm anga\xc5\xbem\xc3\xa1 v n\xc4\x9bmeck\xc3\xa9 SPD dostali a\xc5\xbe na pozici nejbli\xc5\xbe\xc5\xa1\xc3\xadho spolupracovn\xc3\xadka tehdej\xc5\xa1\xc3\xadho kancl\xc3\xa9\xc5\x99e Williho Brandta. '

class JosefVStalin:

    def __init__(self):
        self.Name = 'Josef V. Stalin'
        self.Occupation = 'Politik'
        self.Sociom = 'SSSR'
        self.Resiliance = 100
        self.Assertivity = 100
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = 'Nejv\xc4\x9bt\xc5\xa1\xc3\xad vrah v d\xc4\x9bjin\xc3\xa1ch lidstva. Jeho diktatura si vy\xc5\xbe\xc3\xa1dala n\xc4\x9bco mezi p\xc4\x9bty a\xc5\xbe osmi miliony lidsk\xc3\xbdch ob\xc4\x9bt\xc3\xad, kter\xc3\xa9 bohu\xc5\xbeel nelze p\xc5\x99i\xc4\x8d\xc3\xadtat ani Stalinov\xc4\x9b neschopnosti. Byl to toti\xc5\xbe pr\xc3\xa1v\xc4\x9b Stalin, kter\xc3\xbd po druh\xc3\xa9 sv\xc4\x9btov\xc3\xa9 v\xc3\xa1lce roz\xc5\xa1\xc3\xad\xc5\x99il sov\xc4\x9btsk\xc3\xbd vliv do st\xc5\x99edn\xc3\xad Evropy a uzav\xc5\x99el ji tak za \xc5\xbeeleznou oponou.'

class IvanSKonxc4x9bv:

    def __init__(self):
        self.Name = 'Ivan S. Kon\xc4\x9bv'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'SSSR'
        self.Resiliance = 50
        self.Assertivity = 90
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class KimIrsen:

    def __init__(self):
        self.Name = 'Kim Ir-sen'
        self.Occupation = 'Politik'
        self.Sociom = 'KLDR'
        self.Resiliance = 60
        self.Assertivity = 60
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '

class PIRA:

    def __init__(self):
        self.Name = 'PIRA'
        self.Occupation = 'V\xc3\xa1le\xc4\x8dn\xc3\xadk'
        self.Sociom = 'VB'
        self.Resiliance = 60
        self.Assertivity = 60
        self.RulesToShow = 'Zat\xc3\xadm nic;'
        self.Legend = ' '
def CreateEasternDeck():
    e0=FidelCastro()
    e1=NikitaChruxc5xa1xc4x8dov()
    e2=LeonidBrexc5xbenxc4x9bv()
    e3=AndrejBabixc5xa1()
    e4=GustavHusxc3xa1k()
    e5=JurijGagarin()
    e6=KlementGottwald()
    e7=Hoxc4x8ciMin()
    e8=CheGuevara()
    e9=Jxc3xa1nosKxc3xa1dxc3xa1r()
    e10=WojciechJaruzelski()
    e11=Wxc5x82adysxc5x82awGomuxc5x82ka()
    e12=ErichHonecker()
    e13=LPBerija()
    e14=RAF()
    e15=Gxc3xbcnterGuillaume()
    e16=JosefVStalin()
    e17=IvanSKonxc4x9bv()
    e18=KimIrsen()
    e19=PIRA()
    return[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19]