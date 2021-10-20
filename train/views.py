from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import render
from .forms import HomeForm,NameForm
import pickle
from math import log10
import random
from time import sleep






#def index(request):
#       return render (request,"index.html",{'nombre':200})

#class home_view(ViewSet):
    #def get(request):
    #    form=HomeForm()
    #    return render(request,"index.html",{'form': form})

def post(request):
    form = HomeForm(request.POST)
    temp = 1.0
    temp1 = 1.0
    temp2 = 1.0
    temp3 = 1.0
    if form.is_valid():
        temp = form.cleaned_data['post']
        temp1 = form.cleaned_data.get("post1")
        temp2 = form.cleaned_data.get("post2")
        temp3 = form.cleaned_data.get("post3")
    loaded_model = pickle.load(open('finalized_model.pkl', 'rb'))
    loaded_model1 = pickle.load(open('model_2.pkl', 'rb'))
    loaded_model2 = pickle.load(open('model_3.pkl', 'rb'))
    loaded_model3 = pickle.load(open('model_4.pkl', 'rb'))
    t = [[log10(temp), log10(temp2), log10(temp1), log10(temp3)]]
    s=0
    if loaded_model.predict(t)==0:
        s = 10 ** (2.35363 + 0.31563 *t[0][0] + 0.07569 * t[0][1] + 0.49092 * t[0][2])

    else:
        if loaded_model1.predict(t) > 4 :
            if loaded_model2.predict(t)== 5:
                s = 10 ** (2.52038 + 0.06492 * t[0][1] + 0.36897 * t[0][0] + 0.40747 * t[0][2])
            else :
                s = 10 ** (2.6651 + 0.06176 * t[0][1] + 0.3616 * t[0][0] + 0.3929 * t[0][2])
        else:
            if loaded_model3.predict(t)==3:
                s = 10 ** (2.28602 + 0.06674 * t[0][1] + 0.30387 * t[0][0] + 0.46898 * t[0][2])
            else :
                s = 10 ** (2.1289 + 0.06324 * log10(400) + 0.3459 * log10(44.02) + 0.4388 * log10(9))
    args = {'form': form, 'nombre': s}
    return render(request, "index.html", args)