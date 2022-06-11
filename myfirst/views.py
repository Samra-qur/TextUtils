#This file is created by ME

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def Analyser(request):
    text=request.GET.get('text','default')
    punc_button=request.GET.get('check','off')
    capital=request.GET.get('capitalize','off')
    punctuations=''',#$%@!&;'''
    new_text=text
    if punc_button=='on':
        temp_str=""
        for i in new_text:
            if i not in punctuations:
                temp_str+=i
        params={'purpose':'Remove Punctuations','analyse':temp_str}
        new_text=temp_str


    if capital=='on':
        new_text=new_text.upper()
        params = {'purpose': 'Remove Punctuations', 'analyse': new_text}
    params={'purpose':'Performed','analyse':new_text}

    if capital=='on' or punc_button=='on':
        return render(request, 'analyse.html', params)













