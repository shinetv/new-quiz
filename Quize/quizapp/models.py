from statistics import mode
from django.db import models

# Create your models here.
class Adminu(models.Model):
    user=models.CharField(max_length=200,default='')
    Phone_number=models.CharField(max_length=200,default='')
    email=models.CharField(max_length=300,default='') 
    std_type=models.CharField(max_length=200,default='')
    Course=models.CharField(max_length=300,default='')
    userimage=models.ImageField(upload_to='userimage',null=True,blank=True)
    logintime=models.CharField(max_length=300,default='')
   

    def __str__(self):
        return self.user  

class Ques(models.Model):
    user_IDD=models.ForeignKey(Adminu,on_delete=models.CASCADE, blank=True,null=True)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question             

class Aptitude(models.Model):
    ap_question = models.CharField(max_length=200,null=True)
    ap_op1 = models.CharField(max_length=200,null=True)
    ap_op2 = models.CharField(max_length=200,null=True)
    ap_op3 = models.CharField(max_length=200,null=True)
    ap_op4 = models.CharField(max_length=200,null=True)
    ap_ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.ap_question   

class Result(models.Model):
    User_iDD =models.ForeignKey(Adminu,on_delete=models.CASCADE, blank=True,null=True)
    score=models.IntegerField(blank=False, null=False, default=0)
    percent=models.IntegerField(blank=False, null=False, default=0)
    correct=models.IntegerField(blank=False, null=False, default=0)
    wrong=models.IntegerField(blank=False, null=False, default=0)
    total=models.IntegerField(blank=False, null=False, default=0)
    ap_date=models.CharField(max_length=100,default='')
    
    def __str__(self):
        return str(self.User_iDD)


class GKresult(models.Model):
    GK_idD=models.ForeignKey(Adminu,on_delete=models.CASCADE, blank=True,null=True)
    gk_score=models.IntegerField(blank=False, null=False, default=0)
    gk_percent=models.IntegerField(blank=False, null=False, default=0)
    gk_correct=models.IntegerField(blank=False, null=False, default=0)
    gk_wrong=models.IntegerField(blank=False, null=False, default=0)
    gk_total=models.IntegerField(blank=False, null=False, default=0)
    gk_date=models.CharField(max_length=300,default='')
    gk_time=models.CharField(max_length=300,default='')
 
    def __str__(self):
        return str(self.GK_idD)
