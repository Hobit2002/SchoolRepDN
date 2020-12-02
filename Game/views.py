from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from urllib.parse import urlencode
from django.core.cache import cache
from django.urls import reverse
from Game import GameStats
import json
import Authentication

# Create your views here.

def CallGame(token):
    base_url = reverse('Game')
    urlkey = 'Game'
    query_string =  urlencode({urlkey: token})
    url = '{}?{}'.format(base_url, query_string)
    return url

def CardDetails(request):
    PlayerNum = request.COOKIES["PlayerNum"]
    ConrNum = request.GET["Plnum"]
    ElNum = request.GET["Elnum"]
    CardType = request.GET["CardType"]
    if CardType == '/Figure/g':Elnum=str(int(ElNum)-1)
    Details = GameStats.ShowDetails(PlayerNum,ConrNum,ElNum,CardType)
    return JsonResponse(Details)


def Connect(request):
    if Authentication.ExcludeROB(request):
        GameToken =request.GET["GameToken"]
        Token = GameStats.AddPlayer(GameToken)
        URL = CallGame(Token)
        cache.set(str(Token),GameToken,2)
        return redirect(URL)
    else:
        return HttpResponse("Leave me!")

def Game(request):
    GameCode = request.GET["Game"]
    CachePlayer = cache.get(GameCode)
    if CachePlayer != None:
        Token = GameCode
        cache.delete(GameCode)
    else:
        try:
            Token = request.COOKIES["PlayerNum"]
        except KeyError:
            return redirect('StartPoint')

    GameToken = Token[:(len(Token)-1)]
    DataPack = {"GameCode":GameToken, "UserCode":Token,"MoneyHTML":"Peníze","GloryHTML":"Sláva","DisciplineHTML":"Morálka"}
    PlayerList = GameStats.PlayerList(GameToken)
    ub = 0/4
    if PlayerList != "End":
        DataPack["PlayerList"] = PlayerList
        DataPack["GameStarted"] = (GameStats.GameStarted(GameToken)).lower()
        if Token[(len(GameCode)-1):]=="1":
            DataPack["Role"] = "GameLeader"
        GamePannel = render(request,'GamePannel.html',DataPack)
        if CachePlayer != None:
            GamePannel.set_cookie("PlayerNum", str(Token), max_age = 7200)

        return GamePannel
    else:
        return redirect("StartPoint")

def NewGame(request):
    if Authentication.ExcludeROB(request):
        Token = GameStats.CreateGame()
        #raise ValueError(Token,Skok)
        URL = CallGame(str(Token))
        cache.set(str(Token),Token[:(len(Token)-1)],700)
        
        return redirect(URL)
    else:
        return HttpResponse("Leave me!")

def StartPoint(request):
    return render(request,'GameStart.html')