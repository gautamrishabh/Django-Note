# from django.shortcuts import render
# import mysql.connector as sql
# head=''
# desc=''
# email=''
# # Create your views here.
# def addNotes(request):
#     global head,desc,email
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="rishabh1",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="head":
#                 head=value
#             if key=="desc":
#                 desc=value
#             if key=="email":
#                 email=value
        
#         data =tuple(head,desc)
#         # c="select * from users where email='{}' and password='{}'".format(em,pwd)
#         # c="INSERT INTO users where(CustomerName, City, Country)
#         #     VALUES ('Cardinal', 'Stavanger', 'Norway').format(head,desc)
        
#         c="UPDATE users SET notes = '{}' WHERE Email = '{}'".format(data,email)

#         cursor.execute(c)
#         # auth
#         # t=tuple(cursor.fetchall())
#         # if t==():
#         #     return render(request,'error.html')
#         # else:
#         #     return render(request,"welcome.html")
#     return render(request,'welcome.html')  
    