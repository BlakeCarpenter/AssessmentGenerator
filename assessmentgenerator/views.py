from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from assessmentgenerator.models import UserProfile, Question
import json
from xhtml2pdf import pisa
import cStringIO as StringIO
import cgi

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
        q_type = request.GET.get('type','')
        q_text = request.GET.get('text','')
        q_body = request.GET.get('body','')

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

    return HttpResponse(q.id)

@login_required
def generate_test(request):
    #GET INFORMATION
    if request.method=='POST':
        test_name = request.POST.get('test_name','')
        test_date = request.POST.get('test_date','')
        q_array = request.POST.get('q_array','')
        q_array = json.loads(q_array)

        #GENERATE HTML STRING
        questions = []
        for x in q_array:
            questions.append(Question.objects.get(id=x))

        string = '<!doctype html><html><head><style>.test-name{text-align:center;font-weight:700;text-transform:uppercase}.answer-block,.question-block{list-style-type:lower-alpha}.answer-block li{padding-left:15px}.question-num{width:15px;text-align:left;vertical-align:top}ol{margin-bottom:0px}tr{margin-bottom:0px}p{margin:0px;padding:0px}@page {@frame { margin:2.5cm}</style></head><body><div class="test-date">'+test_date+'</div><div class="test-name">'+test_name+'</div><table>'

	i = 0
        for x in questions:
            i+=1
            string += '<tr><td class="question-num">'+str(i)+'.</td><td><p class="question-body">'+x.question_text+'</p><ol class="answer-block">'
            choices = json.loads(x.question_body)['choices']
            for y in choices:
        
                string += '<li>'+y['choice']+'</li>'
            string += '</ol></td></tr>'

        string += '</table></body></html>'

        #BEGIN RETURNING
        result = StringIO.StringIO()
        pdf = pisa.CreatePDF(StringIO.StringIO(string),result)
        if not pdf.err:
            response = HttpResponse(result.getvalue(),content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="'+test_name+'.pdf"; pagesize=letter'
            return response

        pisa.showLogging()
        return HttpResponse("GENERATION FAILURE")
    else:
        return HttpResponse("POST FAILURE")
