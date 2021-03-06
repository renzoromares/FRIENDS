from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory, TransacHistoryBackUp
from MakeupClass.models import Makeup_Class
from MemoRouting.models import Memo_Routing
from datetime import datetime

def MakeupClass(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None

    if request.method == 'POST':
        form = Form(Id_Number = employeeID, Type = 'Make-up Class' , Date_Requested = datetime.today(),Date_Approved = dateApprove ,Status = 'Pending')  
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        if(request.POST.get('options') == "others"):
            makeupclass = Makeup_Class(Id_Number = employeeID  ,College = request.POST["college"],Reason = request.POST["Reason"],OfferCode =request.POST["offercode"] ,Date =  datetime.today() ,Time = request.POST["time"], Room= request.POST["room"], Date_Of = request.POST["dateOf"], FormID = formPK)
            makeupclass.save()
            if (data.Status_Dept == "Faculty"):
                memo_makeupclass = Memo_Routing(Id_Number = employeeID, Type_Request = 'Make-up Class', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
            if (data.Status_Dept == "Chairman"):
                memo_makeupclass = Memo_Routing(Id_Number = employeeID, Type_Request = 'Make-up Class', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today())
            if (data.Status_Dept == "Dean"):
                memo_makeupclass = Memo_Routing(Id_Number = employeeID, Type_Request = 'Make-up Class', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today(),Date_Dean_Approved=datetime.today())
            memo_makeupclass.save()
            history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Make-up Class', Type='Submitted', Date = datetime.today())
            history.save()
            historyback = TransacHistoryBackUp(Id_Number = employeeID, Transac_Type = 'Make-up Class', Type='Submitted', Date = datetime.today())
            historyback.save()
            return redirect("transachis", id = data.Id_Number.Id_Number) 
        else:
            makeupclass = Makeup_Class(Id_Number = employeeID  ,College =  request.POST["college"],Reason = request.POST.get('options'),OfferCode = request.POST["offercode"] ,Date =  datetime.today(),Time = request.POST["time"], Room= request.POST["room"], Date_Of = request.POST["dateOf"], FormID = formPK)
            makeupclass.save()
            if (data.Status_Dept == "Faculty"):
                memo_makeupclass = Memo_Routing(Id_Number = employeeID, Type_Request = 'Make-up Class', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
            if (data.Status_Dept == "Chairman"):
                memo_makeupclass = Memo_Routing(Id_Number = employeeID, Type_Request = 'Make-up Class', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today())
            if (data.Status_Dept == "Dean"):
                memo_makeupclass = Memo_Routing(Id_Number = employeeID, Type_Request = 'Make-up Class', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today(),Date_Dean_Approved=datetime.today())
            memo_makeupclass.save()
            history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Make-up Class', Type='Submitted', Date = datetime.today())
            history.save()
            historyback = TransacHistoryBackUp(Id_Number = employeeID, Transac_Type = 'Make-up Class', Type='Submitted', Date = datetime.today())
            historyback.save()
            return redirect("transachis", id = data.Id_Number.Id_Number) 
    else:
        return render(request,"makeup-class.html", {'data' : data}) 
        