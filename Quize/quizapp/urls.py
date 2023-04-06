from django.urls import path,include
from quizapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('quest/',views.quest),
    path('addquest/',views.addquest),
    path('result/',views.result),
    path('all_detail/',views.all_detail),
    path('dowcv/',views.dowcv),
    
    # path('DownloadCV/',views.DownloadCV),
]