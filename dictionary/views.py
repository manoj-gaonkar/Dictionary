from django.shortcuts import render, redirect
from django.http import HttpResponse
from PyDictionary import PyDictionary
import json

def index(request):
    return render(request, "index.html")


def meaning(request):
    print("python is")
    if request.method == "POST":
        word = request.POST['word']
        if word == "":
            return redirect('index')
        dictionary=PyDictionary()
        context={
            'data':dictionary.meaning(word)
        }
        dictionary = dictionary.meaning(word)
        meaning = json.dumps(dictionary, indent = 4) 
        return HttpResponse(meaning)

    return redirect('index')