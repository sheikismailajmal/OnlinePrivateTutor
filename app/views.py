from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request,"index.html")

def parentreg(request):
    if request.POST:
        username=request.POST['username3']
        email=request.POST['email3']
        phonenumber=request.POST['phoneno3']
        password=request.POST['password3']
        address=request.POST['address3']
        if Parent.objects.filter(Email=email).exists():
            messages.info(request,"Already Have Registered")
        else:
            parent=Login.objects.create_user(
            username=email,password=password,usertype='parent',viewPassword=password,is_active=0)
            parent.save()
            register=Parent.objects.create(
            Username=username,Email=email,Phonenumber=phonenumber,Password=password,Address=address,parent=parent)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"parentreg.html")

def studentreg(request):
    if request.POST:
        Username9=request.POST['username8']
        Email9=request.POST['email8']
        Phonenumber9=request.POST['phoneno8']
        Password9=request.POST['password8']
        Address9=request.POST['address8']
        if Student.objects.filter(Email2=Email9).exists():
            messages.info(request,"Already Have Registered")
        else:
            student=Login.objects.create_user(
            username=Email9,password=Password9,usertype='student',viewPassword=Password9)
            student.save()
            register2=Student.objects.create(
            Username2=Username9,Email2=Email9,Phonenumber2=Phonenumber9,Password2=Password9,Address2=Address9,student=student)
            register2.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"studentreg.html")    

def login(request):
    if request.POST:
        Email1=request.POST['email2']
        Password1=request.POST['password2']
        user=authenticate(username=Email1,password=Password1)
        if user is not None:
            if user.usertype=="admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/adminhome")
            elif user.usertype=="parent":
                request.session['uid']=user.id
                request.session['email']=user.email
                messages.info(request,"Welcome To The Student Page")
                return redirect("/parenthome")
            elif user.usertype=="student":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Student Page")
                return redirect("/studenthome")
            elif user.usertype=="teacher":
                request.session['uid']=user.id
                request.session['email']=user.email
                request.session['type']=user.usertype
                messages.info(request,"Welcome To The Tutor Page")
                return redirect("/tutorhome")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
    return render(request,"login.html")

def adminhome(request):
    return render(request,"Admin/adminhome.html")

def parenthome(request):
    return render(request,"Student/parenthome.html")

def tutorhome(request):
    return render(request,"Tutor/tutorhome.html")

def studenthome(request):
    return render(request,"Student/studenthome.html")

def addtutor(request):
    if request.POST:
        Username10=request.POST['username4']
        Email10=request.POST['email4']
        Password10=request.POST['password4']
        Subject10=request.POST['subject']
        image10=request.FILES['image4']
        Location10=request.POST['location']
        Fee10=request.POST['fee']
        if Teacher3.objects.filter(email5=Email10).exists():
            messages.info(request,"Already Have Registered")
        else:
            teacher=Login.objects.create_user(
            username=Email10,password=Password10,usertype='teacher',viewPassword=Password10)
            teacher.save()
            register3=Teacher3.objects.create(
            username5=Username10,email5=Email10,password5=Password10,image5=image10,subject5=Subject10,location5=Location10,fee=Fee10,teacher=teacher)
            register3.save()
            messages.info(request,"Successfully")
            return redirect("/viewtutorad")
    return render(request,"Admin/addtutor.html")

def viewtutor_ad(request):
    data=Teacher3.objects.all()
    return render(request,"Admin/viewtutor_ad.html",{"data":data})

def deletetutor(request):
    id=request.GET['id']
    t=Teacher3.objects.filter(id=id)        
    t.delete()
    messages.info(request,"Tutor Deleted Successfully")
    return redirect("/viewtutorad")

def viewstudent_ad(request):
    data=Student.objects.all()
    return render(request,"Admin/viewstudent_ad.html",{"data":data})

def deletestudent(request):
    id=request.GET['id']
    w=Student.objects.filter(id=id)        
    w.delete()
    messages.info(request,"Student Deleted Successfully")
    return redirect("/viewstudentad")

def viewparent_ad(request):
    data=Parent.objects.all()
    return render(request,"Admin/viewparent_ad.html",{"data":data})

def Approve_parent(request):
    status=request.GET['status']
    id=request.GET['id']
    wo=Login.objects.get(id=id)
    wo.is_active=int(status)
    wo.save()
    if status == '1':
        messages.info(request," Approved successfully")
    else:
        Login.objects.filter(id=id).delete()
        messages.info(request," Rejected successfully")
    return redirect("/viewparentad/")

def deleteparent_ad(request):
    id=request.GET['id']
    u=Parent.objects.filter(id=id)        
    u.delete()
    messages.info(request,"Parent Deleted Successfully")
    return redirect("/viewparentad/")

def addbook(request):
    if request.POST:
        subject=request.POST['subject8']
        bookname=request.POST['bookname1']
        image=request.FILES['image1']
        description=request.POST['description1'] 
        link=request.POST['link']
        data=Book.objects.create(subject1=subject,link=link,Bookname=bookname,Image=image,Description=description)
        data.save()
        messages.info(request,"Book Added successfully")
        return redirect("/viewbookad")
    return render(request,"Admin/addebooks.html")

def viewbook_ad(request):
    data=Book.objects.all()
    return render(request,"Admin/viewbook_ad.html",{"data":data})

def viewbook_pa(request):
    data=Book.objects.all()
    return render(request,"Student/viewebook_pa.html",{"data":data})

def deletebook_ad(request):
    id=request.GET['id']
    b=Book.objects.filter(id=id)        
    b.delete()
    messages.info(request,"Book Deleted Successfully")
    return redirect("/viewbookad")

def viewbook_stu(request):
    data=Book.objects.all()
    return render(request,"Student/viewebooks_stu.html",{"data":data})

#def viewparent(request):
#    data=Parent.objects.all()
#    return render(request,"Tutor/viewparents.html",{"data":data})

def actionparent(request):
    id=request.GET['id']
    d=Parent.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewparent")

def deleteparent(request):
    id=request.GET.get('id')
    bbb=Parent.objects.filter(id=id).delete()
    bao=Login.objects.filter(id=id).delete()
    messages.info(request,"deleted successfully")
    return redirect("/viewparent")

def viewtutor_pa(request):
    data=Teacher3.objects.all()
    return render(request,"Student/viewtutor_pa.html",{"data":data})

def addreview(request):
    uid = request.session['uid']
    student = Student.objects.get(student=uid)
    tutor_id=request.GET.get('id')
   # id=request.GET.get('id')
   # teacher=Teacher3.objects.get(id=id)
    # tutor_data = Teacher3.objects.all() 
    if request.POST:
        rating = request.POST.get('rating1')
        review = request.POST.get('review1')
        # tutor_id = request.POST['tutors']
        teacher = get_object_or_404(Teacher3, id=tutor_id)
        if rating and review:
            review = Review.objects.create(rating=rating, review=review, teacher=teacher, student=student)  
            review.save()
            messages.info(request,"Review Added successfully")
            teacher.reviews_count = Review.objects.filter(teacher=teacher).count()

            total_ratings = sum(review.rating for review in Review.objects.filter(teacher=teacher))
            teacher.average_rating = total_ratings / teacher.reviews_count if teacher.reviews_count > 0 else 0

            teacher.save()
    return render(request, "Student/addreview_tutor.html")

def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total_ratings = sum(review.rating for review in reviews)
    return total_ratings/len(reviews)

def deletereview(request):
    id=request.GET['id']
    o=Review.objects.filter(id=id)        
    o.delete()
    messages.info(request,"Review Deleted Successfully")
    return redirect("/viewreview")

def viewreview_tutor(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    data=Review.objects.filter(teacher=teacher)
    return render(request,"Tutor/viewreview.html",{"data":data})

def addbooking_tutor(request):
    tid=request.GET.get('id')
    teacher=Teacher3.objects.get(id=tid)
    uid=request.session['uid']
    parent=Parent.objects.get(parent=uid)
    if request.method == 'POST':
        booking_type2 = request.POST.get('booking')
        booking_time2 = request.POST.get('time')
        booking = Booking1(booking_type1=booking_type2, booking_time1=booking_time2,parent=parent,teacher=teacher)
        booking.save()
        messages.info(request,"Book Tutor successfully")
        return redirect("/viewbooking_pa")
    return render(request,"Student/bookingtutor.html")

def viewbooking_tutor(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    data=Booking1.objects.filter(teacher=teacher)
    return render(request,"Tutor/viewbookingtutor.html",{"data":data})

def viewbooking_parent(request):
    uid=request.session['uid']
    data=Booking1.objects.filter(parent__parent=uid)
    return render(request,"Student/viewbookingtutor1.html",{"data":data})

def actionbooking(request):
    id=request.GET['id']
    n=Booking1.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewbooking")

def deletebooking(request):
    id=request.GET.get('id')
    mbn=Booking1.objects.filter(id=id).delete()
    mnb=Login.objects.filter(id=id).delete()
    messages.info(request,"deleted successfully")
    return redirect("/viewbooking")

def booking_tutor_st(request):
    tid=request.GET.get('id')
    teacher=Teacher3.objects.get(id=tid)
    uid=request.session['uid']
    student=Student.objects.get(student=uid)
    if request.method == 'POST':
        booking_type3 = request.POST.get('booking1')
        booking_time3 = request.POST.get('time1')
        booking1 = Booking1(booking_type1=booking_type3, booking_time1=booking_time3,student=student,teacher=teacher)
        booking1.save()
        messages.info(request,"Book Tutor successfully")
        return redirect("/viewbooking_st")
    return render(request,"Student/bookingtutor_st.html")


def select_tutor(request):
    data=Teacher3.objects.all()
    return render(request,"Student/selecttutor.html",{"data":data})

def viewbooking_stu(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    data=Booking1.objects.filter(teacher=teacher)
    return render(request,"Tutor/viewbooking_stu.html",{"data":data})

def actionbooking_st(request):
    id=request.GET['id']
    i=Booking1.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewbookingst")

def deletebooking_st(request):
    id=request.GET.get('id')
    mpn=Booking1.objects.filter(id=id).delete()
    mpb=Login.objects.filter(id=id).delete()
    messages.info(request,"deleted successfully")
    return redirect("/viewbookingst")

def request_democlass(request):
    id=request.GET.get("id")
    n=Booking1.objects.filter(id=id).update(status='Request_demo')
    messages.info(request,"Request demo class Successfully")
    return redirect("/viewbooking_pa")

def request_democlass_st(request):
    id=request.GET.get("id")
    j=Booking1.objects.filter(id=id).update(status='Request_demo')
    messages.info(request,"Request demo class Successfully")
    return redirect("/viewbooking_st")

def addrequest_demo(request):
    uid=request.session['uid']
    teacher=Teacher3.objects.get(teacher=uid)
    vid=request.GET.get('id')
    booking=Booking1.objects.get(id=vid)
    if request.method == 'POST':
        video1 = request.FILES['video']
        requestdemo = Requestdemo(Video=video1,teacher=teacher,booking=booking)
        requestdemo.save()
        Booking1.objects.filter(id=vid).update(status='Uploaded')
        messages.info(request,"class uploaded successfully")
        return redirect('/viewbooking')
    return render(request,"Tutor/requestdemo.html")

def viewrequest_demo(request):
    id=request.GET.get('id')
    b=Booking1.objects.get(id=id)
    data=Requestdemo.objects.filter(booking=b)
    return render(request,"Student/viewrequestdemo.html",{"data":data})

def viewrequest_demo_st(request):
    id=request.GET.get('id')
    b=Booking1.objects.get(id=id)
    data=Requestdemo.objects.filter(booking=b)
    return render(request,"Student/viewrequestdemo.html",{"data":data})

def viewprofile(request):
    uid=request.session['uid']
    data=Teacher3.objects.filter(teacher=uid)
    return render(request,"Tutor/viewprofile.html",{"data":data})

def parentchat(request):
    id = request.GET.get("id")
    print(id)
    remail = request.GET.get("email")
    uid_id = Teacher3.objects.get(id=id)
    semail = request.session["email"]
    uid = request.session["uid"]
    parent_id = Parent.objects.get(parent=uid)
    type = "parent"
    time = datetime.now().time()
    date = datetime.now().date()
    formatted_time = time.strftime("%I:%M %p")
    formatted_date = date.strftime("%B %d")

    chats = Message.objects.filter(sender=parent_id,receiver=uid_id)

    print("Chats", chats)
    print(uid)

    if request.POST:
        message = request.POST["message"]
        sendMsg = Message.objects.create(
            message=message,
            date=formatted_date,
            time=formatted_time,
            type="parent",
            sender=parent_id,
            receiver=uid_id,
            senderemail=semail,
            reciveremail=remail,
        )
        sendMsg.save()
        # elif type == "Admin":
        #     sendMsg = Message.objects.create(
        #         message=message,
        #         date=formatted_date,
        #         time=formatted_time,
        #         type="Admin",
        #         sender=aid,
        #         receiver=childid,
        #     )
        #     sendMsg.save()
    return render(request, "Student/chat.html", {"chats": chats})


def teacherchat(request):
    pid = request.GET.get("id")
    print(pid)
    remail = request.GET.get("email")
    print(remail)
    parent_id = Parent.objects.get(id=pid)
    uid = request.session["uid"]
    Uidd = Teacher3.objects.get(teacher=uid)
    print("id", Uidd)
    semail = request.session["email"]
    type = request.session["type"]

    time = datetime.now().time()
    date = datetime.now().date()
    formatted_time = time.strftime("%I:%M %p")
    formatted_date = date.strftime("%B %d")

    chats = Message.objects.filter(sender=parent_id,receiver=Uidd)

    if request.POST:
        message = request.POST["message"]

        sendMsg = Message.objects.create(
            message=message,
            date=formatted_date,
            time=formatted_time,
            type="teacher",
            sender=parent_id,
            receiver=Uidd,
            senderemail=semail,
            reciveremail=remail,
        )
        sendMsg.save()
    return render(request, "Tutor/chat.html", {"chats": chats})

def addreview_parent(request):
    uid = request.session['uid']
    parent = Parent.objects.get(parent=uid)
    tutor_id=request.GET.get('id')
    # teacher=Teacher3.objects.get(id=id)
    # tutor_id=teacher.id
    # tutor_data = Teacher3.objects.all() 
    if request.POST:
        rating = request.POST.get('rating1')
        review = request.POST.get('review1')
        # tutor_id = request.POST['tutors']
        teacher = get_object_or_404(Teacher3, id=tutor_id)
        if rating and review:
            review = Review.objects.create(rating=rating, review=review, teacher=teacher, parent=parent)  
            review.save()
            messages.info(request,"Review Added successfully")
            teacher.reviews_count = Review.objects.filter(teacher=teacher).count()

            total_ratings = sum(review.rating for review in Review.objects.filter(teacher=teacher))
            teacher.average_rating = total_ratings / teacher.reviews_count if teacher.reviews_count > 0 else 0

            teacher.save()
            return redirect("/viewbooking_pa")
    return render(request, "Student/rate_tutor.html")

def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total_ratings = sum(review.rating for review in reviews)
    return total_ratings/len(reviews)

def viewbooking_student(request):
    uid=request.session['uid']
    data=Booking1.objects.filter(student__student=uid)
    return render(request,"Student/viewbookingtutor2.html",{"data":data})

def view_review_student(request):
    uid=request.session["uid"]
    data=Review.objects.filter(student__student=uid)
    return render(request,'Student/viewreview.html',{'data':data})

def view_review_parent(request):
    uid=request.session["uid"]
    data=Review.objects.filter(parent__parent=uid)
    return render(request,'Student/viewreview_pa.html',{'data':data})

def addpayment_pa(request):
    uid = request.session['uid']
    parent = Parent.objects.get(parent=uid)
    id = request.GET.get("id")
    teacher = Teacher3.objects.get(id=id)
    if request.method == 'POST':
        payment = Payment(parent=parent,teacher=teacher,status="paid")
        payment.save()
    return render(request, "Student/addpayment.html")

def viewpayment_pa(request):
    data=Payment.objects.all()
    return render(request,"Admin/viewpayment_pa.html",{"data":data})

def addpayment_st(request):
    uid = request.session['uid']
    student = Student.objects.get(student=uid)
    id = request.GET.get("id")
    teacher = Teacher3.objects.get(id=id)
    if request.method == 'POST':
        payment1 = Payment(student=student,teacher=teacher,status="paid")
        payment1.save()
    return render(request, "Student/addpayment.html")

def viewpayment_st(request):
    data=Payment.objects.all()
    return render(request,"Admin/viewpayment_st.html",{"data":data})



  


