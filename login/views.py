from django.shortcuts import render
import mysql.connector as sql
from django.shortcuts import redirect
from django.contrib import messages
from datetime import date
import datetime

em=''
pwd=''
head=''
desc=''
email=''
time=''
# Create your views here.
def loginaction(request):
    global em,pwd,time
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value

        # request.Email==em
          
        c="select * from users where Email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        # auth
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            today = date.today()
            d2 = today.strftime("%B %d, %Y")
            m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
            cursor=m.cursor()
            # print('***********')
            time = str(datetime.datetime.now())
            # print(time)
            # print(em)
            # print(d2)
            # c="UPDATE users SET Last_login = '12' WHERE Email = 'jango@gmail.com'"
            c=("UPDATE users SET Last_login = '{}' WHERE Email = '{}'").format(time,em)
            cursor.execute(c)
            logging.warning('555555555555')

            logging.warning(d2)

            tt=tuple(cursor.fetchall())
            print(tt)
            m.commit()
            return redirect("/welcome")
            # return render(request,'welcome.html')  
            # return render(request,'feed.html')
    return render(request,'login_page.html')
###################################################################################
# NOTEACTION

# Create your views here.
def addNotes(request):
    global head,body,email
    print('oooh')
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="head":
                head=value
            if key=="body":
                body=value
            if key=="email":
                email=value
        
        data =tuple(head,body)
        # c="select * from users where email='{}' and password='{}'".format(em,pwd)
        # c="INSERT INTO users where(CustomerName, City, Country)
        #     VALUES ('Cardinal', 'Stavanger', 'Norway').format(head,desc)
        cursor.execute(c)
        m.commit()
        c="UPDATE users SET notes = '{}' WHERE Email = '{}'".format(data,email)

        cursor.execute(c)
        # auth
        # t=tuple(cursor.fetchall())
        # if t==():
        #     return render(request,'error.html')
        # else:
        #     return render(request,"welcome.html")
    return render(request,'welcome.html')  
    

###################################################################################
# WELCOME

from django.shortcuts import render

# import the logging library
import logging
# Get an instance of a logger
# logger = logging.getLogger(__name__)
# logger.warning()

def wel(request):
    print('=============')
    heading,content,email = '','',''
    notes = ''
    otherNotes = ''
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
        cursor=m.cursor()
        d=request.POST
        cursor.execute("select count(*) from notes")
        row = cursor.fetchone()
        rowCount = row[0]
        print('row:',row,'rowCount:',rowCount)
        for key,value in d.items():
            if key=="head":
                heading=value
            if key=="body":
                content=value
            if key=="userEmail":
                email=value
            # print(key,':',value)
            if(heading != '' and content != '' and email != ''):
                c="insert into notes Values('{}','{}','{}','{}')".format(rowCount+1,email,heading,content)
                cursor.execute(c)
                m.commit()
        context ={"body": "head"}
        messages.info(request, em)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    else:
        print('else...')
        m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
        cursor=m.cursor()
        # d=request.GET
        c="select Sno, Title, Content, Email from notes where Email = '{}'".format(em)
        c1= "select Sno, Title, Content, Email from notes where Email != '{}'".format(em)
        cursor.execute(c)
        notes = cursor.fetchall()
        cursor=m.cursor()
        cursor.execute(c1)
        print('c:',c,'c1:',c1)
        otherNotes = cursor.fetchall()
        print(otherNotes)
        
        # context = {"notes": otherNotes}
        # print('^^^^^^^^^^^^^^^^^^^^^^^',otherNotes)
        # messages.info(request, em,otherNotes)

        context = {"notes": notes, "otherNotes": otherNotes}
        print('^^^^^^^^^^^^^^^^^^^^^^^',otherNotes)
        messages.info(request, em, context)

        m.commit()
    return render(request,"welcome.html",context)
    # def wel(request):
#     logging.warning('hefwfwaefafeaw')
#     logging.warning(em)
#     print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

#     return render(request,'welcome.html')
# head=''
# body=''
# def test(request):
#     logging.warning(request)
#     global head,body
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="head":
#                 head=value
#             if key=="body":
#                 body=value
#         print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#         print(head)
#         print(body)        
#     return render(request,'welcome.html')

###################################################################################
# SIGNUP
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd,time)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')

#####################################################################
# FETCH NOTES
notes=''
def fetch(request):
    global notes
    if request.method=="GET":
        m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
        cursor=m.cursor()
        d=request.GET
        
        c="select * from notes "
        
        cursor.execute(c)
        m.commit()
        notes = cursor.fetchall()
        print(notes)
        print('^^^^^^^^^^^^^^^^^^^^^^^')
    return render(request,'welcome.html')


# def delete(request):
#     print('delete func executed')