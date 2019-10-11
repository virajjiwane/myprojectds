from django.contrib.auth import authenticate,login
from django.db.models import Max
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from reportlab.pdfgen import canvas
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse

from .forms import Form
from .models import Questions


# Create your views here.
@csrf_protect
@never_cache

def loginfun(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    print(username)
    user = authenticate(request, username=username, password=password)
    if user is None:
        return HttpResponseRedirect('fail/')
    if username != "hod":
        return HttpResponseRedirect('register/')



    count = Questions.objects.all().count()
    max_marks = Questions.objects.all().aggregate(Max('marks'))
    ques = Questions.objects.last().question
    ans = Questions.objects.last().answer

    login(request, user)
    request.session['user'] = username
    if ans == 1:
        ans = Questions.objects.last().optionA
    elif ans == 2:
        ans = Questions.objects.last().optionB
    elif ans == 3:
        ans = Questions.objects.last().optionC
    elif ans == 4:
        ans = Questions.objects.last().optionD
    return render(request, 'index.html', {
        'count': count,
        'max_marks': max_marks['marks__max'],
        'ques': ques,
        'ans': ans,
        'name': username
    })


def dash(request):

    #password = request.POST.get('password', False)
    #user = authenticate(request, username=username, password=password)
    #if user is None:
    #    return HttpResponseRedirect('/fail')


    count = Questions.objects.all().count()
    max_marks = Questions.objects.all().aggregate(Max('marks'))
    ques = Questions.objects.last().question
    ans = Questions.objects.last().answer
    if ans == 1:
        ans = Questions.objects.last().optionA
    elif ans == 2:
        ans = Questions.objects.last().optionB
    elif ans == 3:
        ans = Questions.objects.last().optionC
    elif ans == 4:
        ans = Questions.objects.last().optionD
    name = request.session['user']
    return render(request, 'index.html', {
        'count': count,
        'max_marks': max_marks['marks__max'],
        'ques': ques,
        'ans': ans,
        'name': name
    })



@csrf_protect
@never_cache
def form(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('success/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = Form()

    return render(request, 'register.html', {'form': form})


def success(request):
    return render(request, 'success.html', {})


def generate(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 35)
    p.drawString(100, 750, "Question Paper")
    p.setFont("Times-Roman", 13)
    i = 1
    for q in Questions.objects.order_by("?")[0:5]:
        p.drawString(50, 700 - i * 50, str(i) + ") " + q.question)
        p.drawString(60, 680 - i * 50,
                     "A) " + q.optionA + "      B) " + q.optionB + "        C) " + q.optionC + "        D) " + q.optionD)
        i = i + 1

    p.showPage()
    p.save()
    return response


def fail(request):
    return render(request, 'fail.html', {})


def que_ans_module(request):
    records = Questions.objects.all()
    return render(request, 'QueAns.html', {'records': records})
