"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index),
    path('parentreg/',views.parentreg),
    path('studentreg/',views.studentreg),
    path('login/',views.login),
    path('adminhome/',views.adminhome),
    path('parenthome/',views.parenthome),
    path('tutorhome/',views.tutorhome),
    path('studenthome/',views.studenthome),
    path('addtutor/',views.addtutor),
    path('viewtutorad/',views.viewtutor_ad),
    path('deletetutor/',views.deletetutor),
    path('viewstudentad/',views.viewstudent_ad),
    path('deletestudent/',views.deletestudent),
     path('viewparentad/',views.viewparent_ad),
     path('Approve_parent/',views.Approve_parent),
    path('deleteparentad/',views.deleteparent_ad),
    path('addbook/',views.addbook),
    path('viewbookad/',views.viewbook_ad),
    path('viewbookpa/',views.viewbook_pa),  
    path('viewbookstu/',views.viewbook_stu),
    path('deletebookad/',views.deletebook_ad),
    #path('viewparent/',views.viewparent),
    path('actionparent/',views.actionparent),
    path('deleteparent/',views.deleteparent),
    path('viewtutorpa/',views.viewtutor_pa),
    path('selecttutor/',views.select_tutor),
    path('bookingtutor/',views.addbooking_tutor),
    path('bookingtutorst/',views.booking_tutor_st),
    path('viewbooking/',views.viewbooking_tutor),
    path('viewbookingst/',views.viewbooking_stu),
    path('viewbooking_pa/',views.viewbooking_parent),
    path('viewbooking_st/',views.viewbooking_student),
    path('actionbooking/',views.actionbooking),
    path('deletebooking/',views.deletebooking),
     path('actionbookingst/',views.actionbooking_st),
    path('deletebookingst/',views.deletebooking_st),
    path('addrequestdemo/',views.addrequest_demo),
    path('viewrequestdemo/',views.viewrequest_demo),
    path('viewrequestdemost/',views.viewrequest_demo_st),
    path('request_demo/',views.request_democlass),
    path('request_demost/',views.request_democlass_st),
    path('viewprofile/',views.viewprofile),
    path('parentchat/',views.parentchat),
    path('teacherchat/',views.teacherchat),
    path('addreview/',views.addreview),
    path('viewreview/',views.viewreview_tutor),
    path('deletereview/',views.deletereview),
    path('calculaterating/',views.calculate_average_rating),
    path('addreview_parent/',views.addreview_parent),
    path('viewreview_st/',views.view_review_student),
    path('viewreview_pa/',views.view_review_parent),
    path('addpaymentpa/',views.addpayment_pa),
    path('viewpaymentpa/',views.viewpayment_pa),
    path('addpaymentst/',views.addpayment_st),
    path('viewpaymentst/',views.viewpayment_st),
]
