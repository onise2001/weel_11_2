from django.shortcuts import render
import requests

# Create your views here.


def word_meaning(request):

    if request.method == "POST":
        word = request.POST.get("word")
        defenition = get_word_meaning(word)

        return render(request, "word/index.html", {"def": defenition})

    return render(request, "word/index.html")



def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        
        return response[0]["meanings"][0]["definitions"][0]["definition"]
    else:
        ...
    

