" thest file create my best file"

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
 
def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capfirst = request.GET.get('capfirst', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')

    
    
    
    
    
    if removepunc == "on":
        analyzed = ""
        punctuation = '''+-*/{}[]()\/?."'<>`~'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
                
        param = {'purpose':'Removed punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)
    
    if capfirst == "on":
        
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        param = {'purpose':'capitalize_word', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)
    
    if newlineremove == "on":
        
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                pass
        param = {'purpose':'newline remover', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)
    
    if spaceremove == "on":
        
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        param = {'purpose':'extra space remover', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)
    
    if charcount == "on":
        analyzed=""
        for char in djtext:
            if char != " ":
                analyzed= analyzed + char
        param = {'purpose':'charcter count', 'analyzed_text':len(analyzed)}
        djtext = analyzed
        # return render(request,'analyze.html',param)
    # else:
        # return HttpResponse("Error")
        # return render(request,'analyze.html',param)
    return render(request,'analyze.html',param)

    


