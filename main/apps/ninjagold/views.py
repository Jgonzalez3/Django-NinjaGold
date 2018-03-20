# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from datetime import datetime
from random import randint
# create new array then loop backwards to store activity newest at top
log = []


def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    return render(request, "ninjagold/index.html")

def farm(request):
    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        request.session["date"] = timestamp
        earnings = randint(10, 20)
        request.session["farmearnings"] = earnings
        gold = earnings
        print gold
        request.session["gold"] += gold
        activity = {
            "intro": "Earned",
            "middle": "from the farm!",
            "gold": request.session["farmearnings"],
            "date": request.session["date"],
            "result": "win",
        }
        log.append(activity)
        request.session["log"] = log
        return redirect("/")
def cave(request):
    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        print timestamp
        earnings = randint(5, 10)
        request.session["caveearnings"] = earnings
        gold = earnings
        print gold
        request.session["gold"] += gold
        activity = {
            "intro": "Earned",
            "middle": "from the cave!",
            "gold": request.session["caveearnings"],
            "date": request.session["date"],
            "result": "win",
        }
        log.append(activity)
        request.session["log"] = log
        print request.session["log"]
        return redirect("/")
def house(request):
    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        print timestamp
        earnings = randint(2, 5)
        request.session["houseearnings"] = earnings
        gold = earnings
        print gold
        request.session["gold"] += gold
        activity = {
            "intro": "Earned",
            "middle": "from the house!",
            "gold": request.session["houseearnings"],
            "date": request.session["date"],
            "result": "win",
        }
        log.append(activity)
        request.session["log"] = log
        return redirect("/")
def casino(request):
    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        chance = randint(0, 50)
        if chance == 50:
            earnings = randint(0,50)
            gold = earnings
            request.session["casinoearnings"] = gold
            request.session["gold"] += gold
            activity = {
            "intro": "Entered a casino and won",
            "middle": "Winner Winner!",
            "gold": request.session["casinoearnings"],
            "date": request.session["date"],
            "result": "win",
            }
            log.append(activity)
            request.session["log"] = log
            return redirect("/")
        else:
            gamble = randint(0, 50)
            request.session["casinogamble"] = gamble
            gold = gamble
            activity = {
            "intro": "Entered a casino and lost",
            "middle": "... Ouch..",
            "gold": request.session["casinogamble"],
            "date": request.session["date"],
            "result": "lose",
            }
            log.append(activity)
            request.session["log"] = log
            if gold > request.session["gold"]:
                request.session["gold"] = 0
                return redirect("/")
            else:
                request.session["gold"] -= gold
                return redirect("/")

