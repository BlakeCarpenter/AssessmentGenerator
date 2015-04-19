from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from assessmentgenerator.models import UserProfile, Question

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gen/dashboard/')
            else:
                return HttpResponse("The account listed for "+username+" is no longer active")
        else:
            print "Invalid Login: {0}, {1}a".format(username, password)
            return HttpResponse("Invalid login credentials.")

    else:
        return render(request, 'assessmentgenerator/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def generator_home(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('/gen/dashboard/')
    else:
        return render(request, 'assessmentgenerator/generator_home.html')

@login_required
def dashboard(request):
    return render(request, 'assessmentgenerator/dashboard.html')

@login_required
def generator_main(request):
    user_questions = Question.objects.filter(creator=UserProfile.objects.get(user=request.user))
    context_dict = {'user_questions':user_questions}
    return render(request, 'assessmentgenerator/generator.html',context_dict)

@login_required
def add_question(request):
    if request.method =='GET':
        q_type = request.GET['type']
        q_text = request.GET['text']
        q_body = request.GET['body']

        print(q_type)
        print(q_text)
        print(q_body)

        q = Question.objects.get_or_create(creator=UserProfile.objects.get(user=request.user), question_text=q_text)[0]
        print(q)
#        q.creator = request.user
        q.question_type = q_type
        q.question_text = q_text
        q.question_body = q_body
        q.save()

    return HttpResponse("Question Added")
