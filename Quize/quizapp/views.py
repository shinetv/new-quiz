
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Adminu, Aptitude, GKresult,Ques, Result
from django.contrib.auth import logout as log
from Quiz.utils import render_to_pdf
import pandas as pd
import datetime
from django.conf import settings
from django.core.mail import send_mail


# Create your views here

def home(request):
    return render(request,'login.html')

def register(request):
    x             = datetime.datetime.now()
    time          = x.strftime("%X %p")
    if request.method=="POST":
        if Adminu.objects.filter(email=request.POST['email']):
            return render(request,'register.html',{'msgs': 'This Email Already Registered with us.!'})
        else:
            users_dis =Adminu()
            users_dis.email=request.POST['email']
            users_dis.user=request.POST['user']
            users_dis.Phone_number=request.POST['Phone_number']
            users_dis.Course=request.POST['Course']
            users_dis.std_type="Student" 
            users_dis.logintime=time
            users_dis.save() 
            subject='Quiz Registration'
            message='Hello,you are Successfully registered with Edure Quiz World'
            email_from=settings.EMAIL_HOST_USER
            recepient=request.POST.get('email')
            print("check:",recepient)
            send_mail(subject, message, email_from, [recepient], fail_silently = False)
            return redirect(login)
    return render(request,'register.html')    

def login(request):
    if request.method == "POST":
        user = request.POST['user']
        email = request.POST['email']
        User = Adminu.objects.filter(
            user=user, email=email, std_type="Student")
        Admin = Adminu.objects.filter(
            user=user, email=email, std_type="Admin")
       
        # admin = Tbl_Registration.objects.filter(Adm_UserName=username, Adm_Password=password,Adm_Type="Admin")
        if User:
            for x in User:
                request.session['id'] = x.id
                request.session['user'] = x.user
                request.session['std_type'] = x.std_type
                request.session['email'] = x.email
                print("________________________", request.session['id'])
                return HttpResponseRedirect('/quest/')
        elif Admin:
            for x in Admin:
                request.session['id'] = x.id
                request.session['user'] = x.user
                request.session['std_type'] = x.std_type
                request.session['email'] = x.email
                print("________________________", request.session['id'])
                return HttpResponseRedirect('/addquest/')
        else:
            return render(request, 'login.html', {'msg': 'Invalid login credentials.!'})
    else:
        return render(request,'login.html')
       
           

def quest(request):
    SessionId     =request.session['id']
    var3=Adminu.objects.all().filter(id=SessionId)
    sid=Adminu.objects.get(id=SessionId)
    Admin=Adminu.objects.filter(id=SessionId,std_type="Admin").count()
    User=Adminu.objects.filter(id=SessionId,std_type="Student").count()
    questions=Ques.objects.all()
    ap_quest=Aptitude.objects.all()
    varas=GKresult.objects.all().filter(GK_idD=sid).count()
    return render(request,'question.html',{'var3':var3,'questions':questions,'Admin':Admin,'User':User,'ap_quest':ap_quest,'varas':varas})
   

def addquest(request):
    
   
    if request.method=="POST":
        add_ques=Ques()
        add_ques.question=request.POST['question']
        add_ques.op1=request.POST['op1']
        add_ques.op2=request.POST['op2']
        add_ques.op3=request.POST['op3']
        add_ques.op4=request.POST['op4']
        add_ques.ans=request.POST['ans']
        
        add_ques.save()
        print("yyyyyyyyyyyyyyyyyyyyy",add_ques)
        return redirect(addquest)
    else: 
       return render(request,'addquestion.html')        

# def addaptitude(request):
#     if request.method=="POST":
#         add_ap=Aptitude()
#         add_ap.ap_question=request.POST['ap_question'] 
#         add_ap.ap_op1=request.POST['ap_op1']
#         add_ap.ap_op2=request.POST['ap_op2']
#         add_ap.ap_op3=request.POST['ap_op3']
#         add_ap.ap_op4=request.POST['ap_op4']
#         add_ap.ap_ans=request.POST['ap_ans']    
#         add_ap.save()
#         print("ccccccccccccccccccccccc",add_ap)
#         return redirect(quest) 
#     else:
#         return render(request,'Aptitude.html')    

   
      


def logout(request):
    log(request)
    return render(request,'login.html')

def result(request):
    if request.method == 'POST':
        print(request.POST)
        Sessionid=request.session['id']
        sid=Adminu.objects.get(id=Sessionid)
        questions=Ques.objects.all()
        
        
        gk_score=0
        gk_wrong=0
        gk_correct=0
        x             = datetime.datetime.now()
        date          =x.strftime("%Y-%m-%d")
        time          = x.strftime("%X %p")
        varas=GKresult()
        for q in questions:
            varas.gk_total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                varas.gk_score+=10
                varas.gk_correct+=1
                varas.gk_percent = varas.gk_score/(varas.gk_total*10) *100
                varas.GK_idD=sid
                varas.gk_date=date
                varas.gk_time=time
                varas.save()
                vara=Adminu.objects.all().filter(id=Sessionid).update(std_type="Submit")
            else:
                varas.gk_wrong+=1

        
        return redirect(logout)

def all_detail(request):
    varp=GKresult.objects.all()
    
    print("vvvvvvvvvvvvvvvvvvvvvvvvv",varp)
    return render(request,'resultdetail.html',{'varp':varp})         

# def resulttwo(request):
#     if request.method == 'POST':
#         print(request.POST)
#         Sessionid=request.session['id']
#         sid=Adminu.objects.get(id=Sessionid)
#         ap_quest=Aptitude.objects.all()
        
        
#         score=0
#         wrong=0
#         correct=0
#         total=0
#         vara=Result()
#         x             = datetime.datetime.now()
#         date          =x.strftime("%Y-%m-%d")
#         for s in ap_quest:
#             vara.total+=1
            
#             print(request.POST.get(s.ap_question))
#             print(s.ap_ans)
#             print()
#             if s.ap_ans ==  request.POST.get(s.ap_question):
#                 vara.score+=10
#                 vara.correct+=1
#                 vara.percent = vara.score/(vara.total*10) *100
#                 vara.User_iDD=sid
#                 vara.ap_date=date
#                 vara.save()
#             else:
#                 vara.wrong+=1
       
        

#         context = {
#             'score':score,
#             'correct':correct,
#             'wrong':wrong,
#             'percent':vara.percent,
#             'total':vara.total,
#             'vara' :vara
#         }
        
        
#         return render(request,'resulttwo.html',context)    

# def DownloadCV(request):
#     Sessionid=request.session['id']
#     sid=Adminu.objects.get(id=Sessionid)
#     varas=GKresult.objects.all().filter(GK_idD=sid)
#     pdf = render_to_pdf('certificate.html',{'varas':varas})
#     response = HttpResponse(pdf, content_type="application/pdf")
#     response['Content-Disposition'] = 'attachment; filename=Certificate.pdf'
#     return response
def dowcv(request):
    data = Adminu.objects.all().filter(std_type='Submit').values("user","email","Phone_number","logintime","Course")
    df1 = pd.DataFrame(list(data), index=None)
    data2=GKresult.objects.all().values("gk_score","gk_percent","gk_correct","gk_total","gk_date","gk_time")
    df2=pd.DataFrame(list(data2),index=None)
    data_frame=pd.concat([df1,df2],axis=1,ignore_index=True)
    csv = data_frame.to_csv(header=[ "Student Name","Email","Phone Number","Login Time","Course","Score","Percentage","Correct","Total Questions","Date submitted","Submitted Time"], index=True)
    response = HttpResponse(csv, content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=transaction.csv'
    return response