# I have created this file : Shalvi

from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    params ={'name':'shalvi', 'place':'moon'}
    return render(request,'index.html',params)

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    perp=''

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        perp=perp+ 'Removed Punctuations'
        params = {'purpose':perp, 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        perp= perp + '+' + 'Change To Uppercase'
        params = {'purpose':perp, 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        perp= perp+'+'+'Removed NewLines'
        params = {'purpose':perp, 'analyzed_text': analyzed}
        djtext = analyzed


        # Analyze the text

        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        perp=perp+'+'+'Extraspaces'
        params = {'purpose': perp, 'analyzed_text': analyzed}

        # Analyze the text
        #return render(request, 'analyze.html', params)


    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)




def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
                 ]
    return HttpResponse((sites))

'''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Template is working</title>
</head>
<body>
   Hello I am {{name}} from {{place}}<br>
   Enter your text here!!
 <form action="/analyze" method="get">
     <textarea name="text" style="margin: 0px; height: 58px; width: 673px;"></textarea><br>
     <input type="checkbox" name="removepunc">Remove Punctuation <br>
      <input type="checkbox" name="fullcaps"> UPPERCASE<br>
     <input type="checkbox" name="newlineremover"> New Line Remover<br>
     <input type="checkbox" name="extraspaceremover"> Extra Spaces Remover<br>
     <button type="submit">Analyze Text </button>

 </form>
</body>'''
'''</html>'''