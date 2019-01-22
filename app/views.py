from django.shortcuts import render
from django.http import JsonResponse
from googletrans import Translator
import enchant

# Create your views here.
def home(request):
    return render(request,"home.html")
def search(request):
    if request.method=='GET':
        name=request.GET['name']
        translator = Translator()
        #translator = Translator()
        s=name.split(" ")
        s.pop()
        n=s.pop()
        d=enchant.Dict("en_us")
        #s.append("haa ")
        #name=" ".join(s)
        if(d.check(n)):#or if(translator.detect(n)!='en')
             n=n
        else:
             n=translator.translate(n,dest='hi').text
             #r=r.join(s)
             s.append(n+" ")
             name=" ".join(s)

        return JsonResponse({'name':name})
