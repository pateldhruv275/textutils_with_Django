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

# Remove punctuation in the sentences.
    if removepunc == "on":
        analyzed = ""
        punctuation = '''+-*/{}[]()\/?."'<>`~'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

# Capitalize sentences
    elif capfirst == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'capitalize_word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

# Newline remove in the textarea
    elif newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != ("\n"):
                analyzed = analyzed + char
        param = {'purpose': 'newline remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

# Spaceremove in the sentences
    elif spaceremove == "on":
        analyzed = ""
        for char in djtext:
            if char == "  ":
                pass
            else:
                analyzed = analyzed + char
        param = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

# Charcter count in the textarea
    elif charcount == "on":
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        param = {'purpose': 'charcter count', 'analyzed_text': len(
            analyzed), 'l': 'count of charcter'}
        return render(request, 'analyze.html', param)
    else:
        return HttpResponse("Error")
