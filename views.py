from django.http import HttpResponse
from django.shortcuts import render, redirect  
from .forms import *  
from .models import *  
from django.db.models import Q

# Create your views here.

import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def index(request):
    return render(request,"index.html")

def login(request):
    msg=''
    if request.method=="POST":
        
        mb= request.POST.get("username", "")
        ps =request.POST.get("password", "")
        if mb !="" and ps !="":
            print(mb,' ',ps)
            lg= Login.objects.filter(Q(mobileno=mb) & Q(password=ps))
            if(lg.count() >0):
                user=lg.first()
                if(user.usertype =="admin"):
                    return redirect('/admin_home')
                elif(user.usertype=="owner"):
                    return redirect('/owner_home')
                elif(user.usertype=="rentee"):
                    return redirect('/rentee_home')
                elif(user.usertype=="security"):
                    return redirect('/security_home')
                
                    
            else:
                msg="Invalid Details"
        else:
            msg="Must Enter Values"
                
            
    return render(request,"login.html",{'msg':msg})

def forgot1(request):
    msg=''
    if request.method=="POST":
        
        mb= request.POST.get("username", "")
        if mb !="" :
            
            lg= Login.objects.filter(Q(mobileno=mb))
            if(lg.count() >0):
                user=lg.first()
                form = LoginForm(instance=user)
                return render(request,'forgot2.html', {'login':user,'form':form}) 
                
                    
            else:
                msg="Invalid Details"
        else:
            msg="Must Enter Values"
                
            
    return render(request,"forgot1.html",{'msg':msg})

def logininsert(request):  
    if request.method == "POST":  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/loginshow')  
            except:  
                pass  
    else:  
        form = LoginForm()  
    return render(request,'loginindex.html',{'form':form})  
def loginshow(request):  
    logins = Login.objects.all()  
    return render(request,"loginshow.html",{'logins':logins})  
def loginedit(request, id):  
    login = Login.objects.get(id=id)  
    form = LoginForm(instance=login)
    return render(request,'loginedit.html', {'login':login,'form':form})  

def loginupdate(request, id):  
    login = Login.objects.get(id=id)  
    form = LoginForm(request.POST, instance = login)  
    if form.is_valid():  
        form.save()  
        return redirect("/loginshow")  
    return render(request, 'loginedit.html', {'login': login})  

import datetime
def forgot3(request, id):  
    login = Login.objects.get(id=id)
   
    form = LoginForm(request.POST, instance = login)
    
     
    print(form.errors) 
    if form.is_valid():  
        form.save()  
        return redirect("/login")  
    return render(request, 'forgot2.html', {'login': login})  


def logindestroy(request, id):  
    login = Login.objects.get(id=id)  
    login.delete()  
    return redirect("/loginshow")  

def blockinsert(request):  
    if request.method == "POST":  
        form = BlockForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/blockshow')  
            except:  
                pass  
    else:  
        form = BlockForm()  
    return render(request,'blockindex.html',{'form':form})  
def blockshow(request):  
    blocks = Block.objects.all()  
    return render(request,"blockshow.html",{'blocks':blocks})  
def blockedit(request, id):  
    block = Block.objects.get(id=id)  
    form = BlockForm(instance=block)
    return render(request,'blockedit.html', {'block':block,'form':form})  

def blockupdate(request, id):  
    block = Block.objects.get(id=id)  
    form = BlockForm(request.POST, instance = block)  
    if form.is_valid():  
        form.save()  
        return redirect("/blockshow")  
    return render(request, 'blockedit.html', {'block': block})  
def blockdestroy(request, id):  
    block = Block.objects.get(id=id)  
    block.delete()  
    return redirect("/blockshow")  

def societyinsert(request):  
    if request.method == "POST":  
        form = SocietyForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/societyshow')  
            except:  
                pass  
    else:  
        form = SocietyForm()  
    return render(request,'societyindex.html',{'form':form})  
def societyshow(request):  
    societys = Society.objects.all()  
    return render(request,"societyshow.html",{'societys':societys})  
def societyedit(request, id):  
    society= Society.objects.get(id=id)  
    form = SocietyForm(instance=society)
    return render(request,'societyedit.html', {'society':society,'form':form})  

def admin_home(request):
    return render(request,'admin_home.html')

def owner_home(request):
    return render(request,'owner_home.html')

def rentee_home(request):
    return render(request,'rentee_home.html')

def security_home(request):
    return render(request,'security_home.html')

def societyupdate(request, id):  
    society = Society.objects.get(id=id)  
    form = SocietyForm(request.POST, instance = society)  
    if form.is_valid():  
        form.save()  
        return redirect("/societyshow")  
    return render(request, 'societyedit.html', {'society': society})  
def societydestroy(request, id):  
    society = Society.objects.get(id=id)  
    society.delete()  
    return redirect("/societyshow")  

def unittypeinsert(request):  
    if request.method == "POST":  
        form = UnitTypeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/unittypeshow')  
            except:  
                pass  
    else:  
        form = UnitTypeForm()  
    return render(request,'unittypeindex.html',{'form':form})  
def unittypeshow(request):  
    unittypes = UnitType.objects.all()  
    return render(request,"unittypeshow.html",{'unittypes':unittypes})  
def unittypeedit(request, id):  
    unittype= UnitType.objects.get(id=id)  
    form = UnitTypeForm(instance=unittype)
    return render(request,'unittypeedit.html', {'unittype':unittype,'form':form})  

def unittypeupdate(request, id):  
    unittype = UnitType.objects.get(id=id)  
    form = UnitTypeForm(request.POST, instance = unittype)  
    if form.is_valid():  
        form.save()  
        return redirect("/unittypeshow")  
    return render(request, 'unittypeedit.html', {'unittype': unittype})  
def unittypedestroy(request, id):  
    unittype = UnitType.objects.get(id=id)  
    unittype.delete()  
    return redirect("/unittypeshow")  

def unitinsert(request):  
    if request.method == "POST":  
        form = UnitForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/unitshow')  
            except:  
                pass  
    else:  
        form = UnitForm()  
    return render(request,'unitindex.html',{'form':form})  
def unitshow(request):  
    units = Unit.objects.all()  
    return render(request,"unitshow.html",{'units':units})  
def unitedit(request, id):  
    unit= Unit.objects.get(id=id)  
    form = UnitForm(instance=unit)
    return render(request,'unitedit.html', {'unit':unit,'form':form})  

def unitupdate(request, id):  
    unit = Unit.objects.get(id=id)  
    form = UnitForm(request.POST, instance = unit)  
    if form.is_valid():  
        form.save()  
        return redirect("/unitshow")  
    return render(request, 'unitedit.html', {'unit': unit})  
def unitdestroy(request, id):  
    unit = Unit.objects.get(id=id)  
    unit.delete()  
    return redirect("/unitshow")

def ownerinsert(request):  
    if request.method == "POST":  
        form = OwnerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/ownershow')  
            except:  
                pass  
    else:  
        form = OwnerForm()  
    return render(request,'ownerindex.html',{'form':form})  
def ownershow(request):  
    owners = Owner.objects.all()  
    return render(request,"ownershow.html",{'owners':owners})  
def owneredit(request, id):  
    owner= Owner.objects.get(id=id)  
    form = OwnerForm(instance=owner)
    return render(request,'owneredit.html', {'owner':owner,'form':form})  

def ownerupdate(request, id):  
    owner = Owner.objects.get(id=id)  
    form = OwnerForm(request.POST, instance = owner)  
    if form.is_valid():  
        form.save()  
        return redirect("/ownershow")  
    return render(request, 'owneredit.html', {'owner': owner})  
def ownerdestroy(request, id):  
    owner = Owner.objects.get(id=id)  
    owner.delete()  
    return redirect("/ownershow")

def renteeinsert(request):  
    if request.method == "POST":  
        form = RenteeForm(request.POST)
          
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/renteeshow')  
            except:  
                pass  
    else:  
        form = RenteeForm()  
    return render(request,'renteeindex.html',{'form':form})  
def renteeshow(request):  
    rentees = Rentee.objects.all()  
    return render(request,"renteeshow.html",{'rentees':rentees})  
def renteeedit(request, id):  
    rentee = Rentee.objects.get(id=id)  
    form = RenteeForm(instance=rentee)
    return render(request,'renteeedit.html', {'rentee':rentee,'form':form})  

def renteeupdate(request, id):  
    rentee = Rentee.objects.get(id=id)  
    form = RenteeForm(request.POST, instance = rentee)  
    if form.is_valid():  
        form.save()  
        return redirect("/renteeshow")  
    return render(request, 'renteeedit.html', {'rentee': rentee})  
def renteedestroy(request, id):  
    rentee = Rentee.objects.get(id=id)  
    rentee.delete()  
    return redirect("/renteeshow")

def serviceinsert(request):  
    if request.method == "POST":  
        form = ServiceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/serviceshow')  
            except:  
                pass  
    else:  
        form = ServiceForm()  
    return render(request,'serviceindex.html',{'form':form})  
def serviceshow(request):  
    services = Service.objects.all()  
    return render(request,"serviceshow.html",{'services':services})  
def serviceedit(request, id):  
    service = Service.objects.get(id=id)  
    form = ServiceForm(instance=service)
    return render(request,'serviceedit.html', {'service':service,'form':form})  

def serviceupdate(request, id):  
    service = Service.objects.get(id=id)  
    form = ServiceForm(request.POST, instance = service)  
    if form.is_valid():  
        form.save()  
        return redirect("/serviceshow")  
    return render(request, 'serviceedit.html', {'service': service})  
def servicedestroy(request, id):  
    service = Service.objects.get(id=id)  
    service.delete()  
    return redirect("/serviceshow")

def securityinsert(request):  
    if request.method == "POST":  
        form = SecurityForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/securityshow')  
            except:  
                pass  
    else:  
        form = SecurityForm()  
    return render(request,'securityindex.html',{'form':form})  
def securityshow(request):  
    securitys = Security.objects.all()  
    return render(request,"securityshow.html",{'securitys':securitys})  
def securityedit(request, id):  
    security = Security.objects.get(id=id)  
    form = SecurityForm(instance=security)
    return render(request,'securityedit.html', {'security':security,'form':form})  

def securityupdate(request, id):  
    security = Security.objects.get(id=id)  
    form = SecurityForm(request.POST, instance = security)  
    if form.is_valid():  
        form.save()  
        return redirect("/securityshow")  
    return render(request, 'securityedit.html', {'security': security})  
def securitydestroy(request, id):  
    security = Security.objects.get(id=id)  
    security.delete()  
    return redirect("/securityshow")

def committeeinsert(request):  
    if request.method == "POST":  
        form = CommitteeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/committeeshow')  
            except:
                print("Error ")  
                pass  
    else:  
        form = CommitteeForm()  
    return render(request,'committeeindex.html',{'form':form})  
def committeeshow(request):  
    committees = Committee.objects.all()  
    return render(request,"committeeshow.html",{'committees':committees})  
def committeeedit(request, id):  
    committee = Committee.objects.get(id=id)  
    form = CommitteeForm(instance=committee)
    return render(request,'committeeedit.html', {'committee':committee,'form':form})  

def committeeupdate(request, id):  
    committee = Committee.objects.get(id=id)  
    form = CommitteeForm(request.POST, instance = committee)  
    if form.is_valid():  
        form.save()  
        return redirect("/committeeshow")  
    return render(request, 'committeeedit.html', {'committee': committee})  
def committeedestroy(request, id):  
    committee = Committee.objects.get(id=id)  
    committee.delete()  
    return redirect("/committeeshow")

def serviceproviderinsert(request):  
    if request.method == "POST":  
        form = ServiceProviderForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/serviceprovidershow')  
            except:  
                pass  
    else:  
        form = ServiceProviderForm()  
    return render(request,'serviceproviderindex.html',{'form':form})  
def serviceprovidershow(request):  
    serviceproviders = ServiceProvider.objects.all()  
    return render(request,"serviceprovidershow.html",{'serviceproviders':serviceproviders})  
def serviceprovideredit(request, id):  
    serviceprovider = ServiceProvider.objects.get(id=id)  
    form = ServiceProviderForm(instance=serviceprovider)
    return render(request,'serviceprovideredit.html', {'serviceprovider':serviceprovider,'form':form})  

def serviceproviderupdate(request, id):  
    serviceprovider = ServiceProvider.objects.get(id=id)  
    form = ServiceProviderForm(request.POST, instance = serviceprovider)  
    if form.is_valid():  
        form.save()  
        return redirect("/serviceprovidershow")  
    return render(request, 'serviceprovideredit.html', {'serviceprovider': serviceprovider})  
def serviceproviderdestroy(request, id):  
    serviceprovider = ServiceProvider.objects.get(id=id)  
    serviceprovider.delete()  
    return redirect("/serviceprovidershow")

def expenseinsert(request):  
    if request.method == "POST":  
        form = ExpenseForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/expenseshow')  
            except:  
                pass  
    else:  
        form = ExpenseForm()  
    return render(request,'expenseindex.html',{'form':form})  
def expenseshow(request):  
    expenses = Expense.objects.all()  
    return render(request,"expenseshow.html",{'expenses':expenses})  
def expenseedit(request, id):  
    expense = Expense.objects.get(id=id)  
    form = ExpenseForm(instance=expense)
    return render(request,'expenseedit.html', {'expense':expense,'form':form})  

def expenseupdate(request, id):  
    expense = Expense.objects.get(id=id)  
    form = ExpenseForm(request.POST, instance = expense) 
    print(form) 
    if form.is_valid():  
        form.save()  
        return redirect("/expenseshow") 
    else:
        print(form.errors)
    return render(request, 'expenseedit.html', {'expense': expense})  
def expensedestroy(request, id):  
    expense = Expense.objects.get(id=id)  
    expense.delete()  
    return redirect("/expenseshow")

def incomeinsert(request):  
    if request.method == "POST":  
        form = IncomeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/incomeshow')  
            except:  
                pass  
    else:  
        form = IncomeForm()  
    return render(request,'incomeindex.html',{'form':form})  
def incomeshow(request):  
    incomes = Income.objects.all()  
    return render(request,"incomeshow.html",{'incomes':incomes})  
def incomeedit(request, id):  
    income = Income.objects.get(id=id)  
    form = IncomeForm(instance=income)
    return render(request,'incomeedit.html', {'income':income,'form':form})  

def incomeupdate(request, id):  
    income = Income.objects.get(id=id)  
    form = IncomeForm(request.POST, instance = income)  
    if form.is_valid():  
        form.save()  
        return redirect("/incomeshow")  
    return render(request, 'incomeedit.html', {'income': income})  
def incomedestroy(request, id):  
    income = Income.objects.get(id=id)  
    income.delete()  
    return redirect("/incomeshow")

def complaininsert(request):  
    if request.method == "POST":  
        form = ComplainForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/complainshow')  
            except:  
                pass  
    else:  
        form = ComplainForm()  
    return render(request,'complainindex.html',{'form':form})  
def complainshow(request):  
    complains = Complain.objects.all()  
    return render(request,"complainshow.html",{'complains':complains})  
def complainedit(request, id):  
    complain = Complain.objects.get(id=id)  
    form = ComplainForm(instance=complain)
    return render(request,'complainedit.html', {'complain':complain,'form':form})  

def complainupdate(request, id):  
    complain = Complain.objects.get(id=id)  
    form = ComplainForm(request.POST, instance = complain)  
    if form.is_valid():  
        form.save()  
        return redirect("/complainshow")  
    return render(request, 'complainedit.html', {'complain': complain})  
def complaindestroy(request, id):  
    complain = Complain.objects.get(id=id)  
    complain.delete()  
    return redirect("/complainshow")

def solutioninsert(request):  
    if request.method == "POST":  
        form = SolutionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/solutionshow')  
            except:  
                pass  
    else:  
        form = SolutionForm()  
    return render(request,'solutionindex.html',{'form':form})  
def solutionshow(request):  
    solutions = Solution.objects.all()  
    return render(request,"solutionshow.html",{'solutions':solutions})  
def solutionedit(request, id):  
    solution = Solution.objects.get(id=id)  
    form = SolutionForm(instance=solution)
    return render(request,'solutionedit.html', {'solution':solution,'form':form})  

def solutionupdate(request, id):  
    solution = Solution.objects.get(id=id)  
    form = SolutionForm(request.POST, instance = solution)  
    if form.is_valid():  
        form.save()  
        return redirect("/solutionshow")  
    return render(request, 'solutionedit.html', {'solution': solution})  
def solutiondestroy(request, id):  
    solution = Solution.objects.get(id=id)  
    solution.delete()  
    return redirect("/solutionshow")

def circularsinsert(request):  
    if request.method == "POST":  
        form = CircularsForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/circularsshow')  
            except:  
                pass  
    else:  
        form = CircularsForm()  
    return render(request,'circularsindex.html',{'form':form})  
def circularsshow(request):  
    circularss = Circulars.objects.all()  
    return render(request,"circularsshow.html",{'circularss':circularss})  
def circularsedit(request, id):  
    circulars = Circulars.objects.get(id=id)  
    form = CircularsForm(instance=circulars)
    return render(request,'circularsedit.html', {'circulars':circulars,'form':form})  

def circularsupdate(request, id):  
    circulars = Circulars.objects.get(id=id)  
    form = CircularsForm(request.POST, instance = circulars)  
    if form.is_valid():  
        form.save()  
        return redirect("/circularsshow")  
    return render(request, 'circularsedit.html', {'circulars': circulars})  
def circularsdestroy(request, id):  
    circulars = Circulars.objects.get(id=id)  
    circulars.delete()  
    return redirect("/circularsshow")

def eventinsert(request):  
    if request.method == "POST":  
        form = EventForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/eventshow')  
            except:  
                pass  
    else:  
        form = EventForm()  
    return render(request,'eventindex.html',{'form':form})  
def eventshow(request):  
    events = Event.objects.all()  
    return render(request,"eventshow.html",{'events':events})  
def eventedit(request, id):  
    event = Event.objects.get(id=id)  
    form = EventForm(instance=event)
    return render(request,'eventedit.html', {'event':event,'form':form})  

def eventupdate(request, id):  
    event = Event.objects.get(id=id)  
    form = EventForm(request.POST, instance = event)  
    if form.is_valid():  
        form.save()  
        return redirect("/eventshow")  
    return render(request, 'eventedit.html', {'event': event})  
def eventdestroy(request, id):  
    event = Event.objects.get(id=id)  
    event.delete()  
    return redirect("/eventshow")

def eventphotosinsert(request):  
    if request.method == "POST":  
        form = EventPhotosForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/eventphotosshow')  
            except:  
                pass  
    else:  
        form = EventPhotosForm()  
    return render(request,'eventphotosindex.html',{'form':form})  
def eventphotosshow(request):  
    eventphotoss = EventPhotos.objects.all()  
    return render(request,"eventphotosshow.html",{'eventphotoss':eventphotoss})  
def eventphotosedit(request, id):  
    eventphotos = EventPhotos.objects.get(id=id)  
    form = EventPhotosForm(instance=eventphotos)
    return render(request,'eventphotosedit.html', {'eventphotos':eventphotos,'form':form})  

def eventphotosupdate(request, id):  
    eventphotos = EventPhotos.objects.get(id=id)  
    form = EventPhotosForm(request.POST, instance = eventphotos)  
    if form.is_valid():  
        form.save()  
        return redirect("/eventphotosshow")  
    return render(request, 'eventphotosedit.html', {'eventphotos': eventphotos})  
def eventphotosdestroy(request, id):  
    eventphotos = EventPhotos.objects.get(id=id)  
    eventphotos.delete()  
    return redirect("/eventphotosshow")

def vehicledetailsinsert(request):  
    if request.method == "POST":  
        form = VehicleDetailsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/vehicledetailsshow')  
            except:  
                pass  
    else:  
        form = VehicleDetailsForm()  
    return render(request,'vehicledetailsindex.html',{'form':form})  
def vehicledetailsshow(request):  
    vehicledetailss = VehicleDetails.objects.all()  
    return render(request,"vehicledetailsshow.html",{'vehicledetailss':vehicledetailss})  
def vehicledetailsedit(request, id):  
    vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(instance=vehicledetails)
    return render(request,'vehicledetailsedit.html', {'vehicledetails':vehicledetails,'form':form})  

def vehicledetailsupdate(request, id):  
    vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(request.POST, instance = vehicledetails)  
    if form.is_valid():  
        form.save()  
        return redirect("/vehicledetailsshow")  
    return render(request, 'vehicledetailsedit.html', {'vehicledetails': vehicledetails})  
def vehicledetailsdestroy(request, id):  
    vehicledetails = VehicleDetails.objects.get(id=id)  
    vehicledetails.delete()  
    return redirect("/vehicledetailsshow")

def visitorentryinsert(request):  
    if request.method == "POST":  
        form = VisitorentryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/visitorentryshow')  
            except:  
                pass  
    else:  
        form = VisitorentryForm()  
    return render(request,'visitorentryindex.html',{'form':form})  
def visitorentryshow(request):  
    visitorentrys = Visitorentry.objects.all()  
    return render(request,"visitorentryshow.html",{'visitorentrys':visitorentrys})  
def visitorentryedit(request, id):  
    visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(instance=visitorentry)
    return render(request,'visitorentryedit.html', {'visitorentry':visitorentry,'form':form})  

def visitorentryupdate(request, id):  
    visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(request.POST, instance = visitorentry)  
    if form.is_valid():  
        form.save()  
        return redirect("/visitorentryshow")  
    return render(request, 'visitorentryedit.html', {'visitorentry': visitorentry})  
def visitorentrydestroy(request, id):  
    visitorentry = Visitorentry.objects.get(id=id)  
    visitorentry.delete()  
    return redirect("/visitorentryshow")

def security_vehicledetailsinsert(request):  
    if request.method == "POST":  
        form = VehicleDetailsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/security_vehicledetailsshow')  
            except:  
                pass  
    else:  
        form = VehicleDetailsForm()  
    return render(request,'security_vehicledetailsindex.html',{'form':form})  
def security_vehicledetailsshow(request):  
    security_vehicledetailss = VehicleDetails.objects.all()  
    return render(request,"security_vehicledetailsshow.html",{'security_vehicledetailss':security_vehicledetailss})  

def security_vehicledetailsedit(request, id):  
    security_vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(instance=security_vehicledetails)
    return render(request,'security_vehicledetailsedit.html', {'security_vehicledetails':security_vehicledetails,'form':form})  

def security_vehicledetailsupdate(request, id):  
    security_vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(request.POST, instance = security_vehicledetails)  
    if form.is_valid():  
        form.save()  
        return redirect("/security_vehicledetailsshow")  
    return render(request, 'security_vehicledetailsedit.html', {'security_vehicledetails': security_vehicledetails})  
def security_vehicledetailsdestroy(request, id):  
    security_vehicledetails = VehicleDetails.objects.get(id=id)  
    security_vehicledetails.delete()  
    return redirect("/security_vehicledetailsshow")

def security_visitorentryinsert(request):  
    if request.method == "POST":  
        form = VisitorentryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/security_visitorentryshow')  
            except:  
                pass  
    else:  
        form = VisitorentryForm()  
    return render(request,'security_visitorentryindex.html',{'form':form})  
def security_visitorentryshow(request):  
    security_visitorentrys = Visitorentry.objects.all()  
    return render(request,"security_visitorentryshow.html",{'security_visitorentrys':security_visitorentrys})  
def security_visitorentryedit(request, id):  
    security_visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(instance=security_visitorentry)
    return render(request,'security_visitorentryedit.html', {'security_visitorentry':security_visitorentry,'form':form})  

def security_visitorentryupdate(request, id):  
    security_visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(request.POST, instance = security_visitorentry)  
    if form.is_valid():  
        form.save()  
        return redirect("/security_visitorentryshow")  
    return render(request, 'security_visitorentryedit.html', {'security_visitorentry': security_visitorentry})  
def security_visitorentrydestroy(request, id):  
    security_visitorentry = Visitorentry.objects.get(id=id)  
    security_visitorentry.delete()  
    return redirect("/security_visitorentryshow")

def rentee_committeeinsert(request):  
    if request.method == "POST":  
        form = CommitteeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_committeeshow')  
            except:
                print("Error ")  
                pass  
    else:  
        form = CommitteeForm()  
    return render(request,'rentee_committeeindex.html',{'form':form})  
def rentee_committeeshow(request):  
    rentee_committees = Committee.objects.all()  
    return render(request,"rentee_committeeshow.html",{'rentee_committees':rentee_committees})  
def rentee_committeeedit(request, id):  
    rentee_committee = Committee.objects.get(id=id)  
    form = CommitteeForm(instance=rentee_committee)
    return render(request,'rentee_committeeedit.html', {'rentee_committee':rentee_committee,'form':form})  

def rentee_committeeupdate(request, id):  
    rentee_committee = Committee.objects.get(id=id)  
    form = CommitteeForm(request.POST, instance = rentee_committee)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_committeeshow")  
    return render(request, 'rentee_committeeedit.html', {'rentee_committee': rentee_committee})  
def rentee_committeedestroy(request, id):  
    rentee_committee = Committee.objects.get(id=id)  
    rentee_committee.delete()  
    return redirect("/rentee_committeeshow")

def rentee_circularsinsert(request):  
    if request.method == "POST":  
        form = CircularsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_circularsshow')  
            except:  
                pass  
    else:  
        form = CircularsForm()  
    return render(request,'rentee_circularsindex.html',{'form':form})  
def rentee_circularsshow(request):  
    rentee_circularss = Circulars.objects.all()  
    return render(request,"rentee_circularsshow.html",{'rentee_circularss':rentee_circularss})  
def rentee_circularsedit(request, id):  
    rentee_circulars = Circulars.objects.get(id=id)  
    form = CircularsForm(instance=rentee_circulars)
    return render(request,'rentee_circularsedit.html', {'rentee_circulars':rentee_circulars,'form':form})  

def rentee_circularsupdate(request, id):  
    rentee_circulars = Circulars.objects.get(id=id)  
    form = CircularsForm(request.POST, instance = rentee_circulars)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_circularsshow")  
    return render(request, 'rentee_circularsedit.html', {'rentee_circulars': rentee_circulars})  
def rentee_circularsdestroy(request, id):  
    rentee_circulars = Circulars.objects.get(id=id)  
    rentee_circulars.delete()  
    return redirect("/rentee_circularsshow") 

def rentee_eventinsert(request):  
    if request.method == "POST":  
        form = EventForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_eventshow')  
            except:  
                pass  
    else:  
        form = EventForm()  
    return render(request,'rentee_eventindex.html',{'form':form})  
def rentee_eventshow(request):  
    rentee_events = Event.objects.all()  
    return render(request,"rentee_eventshow.html",{'rentee_events':rentee_events})  
def rentee_eventedit(request, id):  
    rentee_event = Event.objects.get(id=id)  
    form = EventForm(instance=rentee_event)
    return render(request,'rentee_eventedit.html', {'rentee_event':rentee_event,'form':form})  

def rentee_eventupdate(request, id):  
    rentee_event = Event.objects.get(id=id)  
    form = EventForm(request.POST, instance = rentee_event)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_eventshow")  
    return render(request, 'rentee_eventedit.html', {'rentee_event': rentee_event})  
def rentee_eventdestroy(request, id):  
    rentee_event = Event.objects.get(id=id)  
    rentee_event.delete()  
    return redirect("/rentee_eventshow")

def rentee_eventphotosinsert(request):  
    if request.method == "POST":  
        form = EventPhotosForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_eventphotosshow')  
            except:  
                pass  
    else:  
        form = EventPhotosForm()  
    return render(request,'rentee_eventphotosindex.html',{'form':form})  
def rentee_eventphotosshow(request):  
    rentee_eventphotoss = EventPhotos.objects.all()  
    return render(request,"rentee_eventphotosshow.html",{'rentee_eventphotoss':rentee_eventphotoss})  
def rentee_eventphotosedit(request, id):  
    rentee_eventphotos = EventPhotos.objects.get(id=id)  
    form = EventPhotosForm(instance=rentee_eventphotos)
    return render(request,'rentee_eventphotosedit.html', {'rentee_eventphotos':rentee_eventphotos,'form':form})  

def rentee_eventphotosupdate(request, id):  
    rentee_eventphotos = EventPhotos.objects.get(id=id)  
    form = EventPhotosForm(request.POST, instance = rentee_eventphotos)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_eventphotosshow")  
    return render(request, 'rentee_eventphotosedit.html', {'rentee_eventphotos': rentee_eventphotos})  
def rentee_eventphotosdestroy(request, id):  
    rentee_eventphotos = EventPhotos.objects.get(id=id)  
    rentee_eventphotos.delete()  
    return redirect("/rentee_eventphotosshow")

def rentee_vehicledetailsinsert(request):  
    if request.method == "POST":  
        form = VehicleDetailsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_vehicledetailsshow')  
            except:  
                pass  
    else:  
        form = VehicleDetailsForm()  
    return render(request,'rentee_vehicledetailsindex.html',{'form':form})  
def rentee_vehicledetailsshow(request):  
    rentee_vehicledetailss = VehicleDetails.objects.all()  
    return render(request,"rentee_vehicledetailsshow.html",{'rentee_vehicledetailss':rentee_vehicledetailss})  

def rentee_vehicledetailsedit(request, id):  
    rentee_vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(instance=rentee_vehicledetails)
    return render(request,'rentee_vehicledetailsedit.html', {'rentee_vehicledetails':rentee_vehicledetails,'form':form})  

def rentee_vehicledetailsupdate(request, id):  
    rentee_vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(request.POST, instance = rentee_vehicledetails)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_vehicledetailsshow")  
    return render(request, 'rentee_vehicledetailsedit.html', {'rentee_vehicledetails': rentee_vehicledetails})  
def rentee_vehicledetailsdestroy(request, id):  
    rentee_vehicledetails = VehicleDetails.objects.get(id=id)  
    rentee_vehicledetails.delete()  
    return redirect("/rentee_vehicledetailsshow")

def rentee_visitorentryinsert(request):  
    if request.method == "POST":  
        form = VisitorentryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_visitorentryshow')  
            except:  
                pass  
    else:  
        form = VisitorentryForm()  
    return render(request,'rentee_visitorentryindex.html',{'form':form})  
def rentee_visitorentryshow(request):  
    rentee_visitorentrys = Visitorentry.objects.all()  
    return render(request,"rentee_visitorentryshow.html",{'rentee_visitorentrys':rentee_visitorentrys})  
def rentee_visitorentryedit(request, id):  
    rentee_visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(instance=rentee_visitorentry)
    return render(request,'rentee_visitorentryedit.html', {'rentee_visitorentry':rentee_visitorentry,'form':form})  

def rentee_visitorentryupdate(request, id):  
    rentee_visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(request.POST, instance = rentee_visitorentry)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_visitorentryshow")  
    return render(request, 'rentee_visitorentryedit.html', {'rentee_visitorentry': rentee_visitorentry})  
def rentee_visitorentrydestroy(request, id):  
    rentee_visitorentry = Visitorentry.objects.get(id=id)  
    rentee_visitorentry.delete()  
    return redirect("/rentee_visitorentryshow")

def rentee_serviceinsert(request):  
    if request.method == "POST":  
        form = ServiceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_serviceshow')  
            except:  
                pass  
    else:  
        form = ServiceForm()  
    return render(request,'rentee_serviceindex.html',{'form':form})  
def rentee_serviceshow(request):  
    rentee_services = Service.objects.all()  
    return render(request,"rentee_serviceshow.html",{'rentee_services':rentee_services})  
def rentee_serviceedit(request, id):  
    rentee_service = Service.objects.get(id=id)  
    form = ServiceForm(instance=rentee_service)
    return render(request,'rentee_serviceedit.html', {'rentee_service':rentee_service,'form':form})  

def rentee_serviceupdate(request, id):  
    rentee_service = Service.objects.get(id=id)  
    form = ServiceForm(request.POST, instance = rentee_service)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_serviceshow")  
    return render(request, 'rentee_serviceedit.html', {'rentee_service': rentee_service})  
def rentee_servicedestroy(request, id):  
    rentee_service = Service.objects.get(id=id)  
    rentee_service.delete()  
    return redirect("/rentee_serviceshow")

def rentee_serviceproviderinsert(request):  
    if request.method == "POST":  
        form = ServiceProviderForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_serviceprovidershow')  
            except:  
                pass  
    else:  
        form = ServiceProviderForm()  
    return render(request,'rentee_serviceproviderindex.html',{'form':form})  
def rentee_serviceprovidershow(request):  
    rentee_serviceproviders = ServiceProvider.objects.all()  
    return render(request,"rentee_serviceprovidershow.html",{'rentee_serviceproviders':rentee_serviceproviders})  
def rentee_serviceprovideredit(request, id):  
    rentee_serviceprovider = ServiceProvider.objects.get(id=id)  
    form = ServiceProviderForm(instance=rentee_serviceprovider)
    return render(request,'rentee_serviceprovideredit.html', {'rentee_serviceprovider':rentee_serviceprovider,'form':form})  

def rentee_serviceproviderupdate(request, id):  
    rentee_serviceprovider = ServiceProvider.objects.get(id=id)  
    form = ServiceProviderForm(request.POST, instance = rentee_serviceprovider)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_serviceprovidershow")  
    return render(request, 'rentee_serviceprovideredit.html', {'rentee_serviceprovider': rentee_serviceprovider})  
def rentee_serviceproviderdestroy(request, id):  
    rentee_serviceprovider = ServiceProvider.objects.get(id=id)  
    rentee_serviceprovider.delete()  
    return redirect("/rentee_serviceprovidershow")

def rentee_complaininsert(request):  
    if request.method == "POST":  
        form = ComplainForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_complainshow')  
            except:  
                pass  
    else:  
        form = ComplainForm()  
    return render(request,'rentee_complainindex.html',{'form':form})  
def rentee_complainshow(request):  
    rentee_complains = Complain.objects.all()  
    return render(request,"rentee_complainshow.html",{'rentee_complains':rentee_complains})  
def rentee_complainedit(request, id):  
    rentee_complain = Complain.objects.get(id=id)  
    form = ComplainForm(instance=rentee_complain)
    return render(request,'rentee_complainedit.html', {'rentee_complain':rentee_complain,'form':form})  

def rentee_complainupdate(request, id):  
    rentee_complain = Complain.objects.get(id=id)  
    form = ComplainForm(request.POST, instance = rentee_complain)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_complainshow")  
    return render(request, 'rentee_complainedit.html', {'rentee_complain': rentee_complain})  
def rentee_complaindestroy(request, id):  
    rentee_complain = Complain.objects.get(id=id)  
    rentee_complain.delete()  
    return redirect("/rentee_complainshow")

def rentee_solutioninsert(request):  
    if request.method == "POST":  
        form = SolutionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/rentee_solutionshow')  
            except:  
                pass  
    else:  
        form = SolutionForm()  
    return render(request,'rentee_solutionindex.html',{'form':form})  
def rentee_solutionshow(request):  
    rentee_solutions = Solution.objects.all()  
    return render(request,"rentee_solutionshow.html",{'rentee_solutions':rentee_solutions})  
def rentee_solutionedit(request, id):  
    rentee_solution = Solution.objects.get(id=id)  
    form = SolutionForm(instance=rentee_solution)
    return render(request,'rentee_solutionedit.html', {'rentee_solution':rentee_solution,'form':form})  

def rentee_solutionupdate(request, id):  
    rentee_solution = Solution.objects.get(id=id)  
    form = SolutionForm(request.POST, instance = rentee_solution)  
    if form.is_valid():  
        form.save()  
        return redirect("/rentee_solutionshow")  
    return render(request, 'rentee_solutionedit.html', {'rentee_solution': rentee_solution})  
def rentee_solutiondestroy(request, id):  
    rentee_solution = Solution.objects.get(id=id)  
    rentee_solution.delete()  
    return redirect("/rentee_solutionshow")

def owner_committeeinsert(request):  
    if request.method == "POST":  
        form = CommitteeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_committeeshow')  
            except:
                print("Error ")  
                pass  
    else:  
        form = CommitteeForm()  
    return render(request,'owner_committeeindex.html',{'form':form})  
def owner_committeeshow(request):  
    owner_committees = Committee.objects.all()  
    return render(request,"owner_committeeshow.html",{'owner_committees':owner_committees})  
def owner_committeeedit(request, id):  
    owner_committee = Committee.objects.get(id=id)  
    form = CommitteeForm(instance=owner_committee)
    return render(request,'owner_committeeedit.html', {'owner_committee':owner_committee,'form':form})  

def owner_committeeupdate(request, id):  
    owner_committee = Committee.objects.get(id=id)  
    form = CommitteeForm(request.POST, instance = owner_committee)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_committeeshow")  
    return render(request, 'owner_committeeedit.html', {'owner_committee': owner_committee})  
def owner_committeedestroy(request, id):  
    owner_committee = Committee.objects.get(id=id)  
    owner_committee.delete()  
    return redirect("/owner_committeeshow")

def owner_circularsinsert(request):  
    if request.method == "POST":  
        form = CircularsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_circularsshow')  
            except:  
                pass  
    else:  
        form = CircularsForm()  
    return render(request,'owner_circularsindex.html',{'form':form})  
def owner_circularsshow(request):  
    owner_circularss = Circulars.objects.all()  
    return render(request,"owner_circularsshow.html",{'owner_circularss':owner_circularss})  
def owner_circularsedit(request, id):  
    owner_circulars = Circulars.objects.get(id=id)  
    form = CircularsForm(instance=owner_circulars)
    return render(request,'owner_circularsedit.html', {'owner_circulars':owner_circulars,'form':form})  

def owner_circularsupdate(request, id):  
    owner_circulars = Circulars.objects.get(id=id)  
    form = CircularsForm(request.POST, instance = owner_circulars)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_circularsshow")  
    return render(request, 'owner_circularsedit.html', {'owner_circulars': owner_circulars})  
def owner_circularsdestroy(request, id):  
    owner_circulars = Circulars.objects.get(id=id)  
    owner_circulars.delete()  
    return redirect("/owner_circularsshow")

def owner_eventinsert(request):  
    if request.method == "POST":  
        form = EventForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_eventshow')  
            except:  
                pass  
    else:  
        form = EventForm()  
    return render(request,'owner_eventindex.html',{'form':form})  
def owner_eventshow(request):  
    owner_events = Event.objects.all()  
    return render(request,"owner_eventshow.html",{'owner_events':owner_events})  
def owner_eventedit(request, id):  
    owner_event = Event.objects.get(id=id)  
    form = EventForm(instance=owner_event)
    return render(request,'owner_eventedit.html', {'owner_event':owner_event,'form':form})  

def owner_eventupdate(request, id):  
    owner_event = Event.objects.get(id=id)  
    form = EventForm(request.POST, instance = owner_event)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_eventshow")  
    return render(request, 'owner_eventedit.html', {'owner_event': owner_event})  
def owner_eventdestroy(request, id):  
    owner_event = Event.objects.get(id=id)  
    owner_event.delete()  
    return redirect("/owner_eventshow")

def owner_eventphotosinsert(request):  
    if request.method == "POST":  
        form = EventPhotosForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_eventphotosshow')  
            except:  
                pass  
    else:  
        form = EventPhotosForm()  
    return render(request,'owner_eventphotosindex.html',{'form':form})  
def owner_eventphotosshow(request):  
    owner_eventphotoss = EventPhotos.objects.all()  
    return render(request,"owner_eventphotosshow.html",{'owner_eventphotoss':owner_eventphotoss})  
def owner_eventphotosedit(request, id):  
    owner_eventphotos = EventPhotos.objects.get(id=id)  
    form = EventPhotosForm(instance=owner_eventphotos)
    return render(request,'owner_eventphotosedit.html', {'owner_eventphotos':owner_eventphotos,'form':form})  

def owner_eventphotosupdate(request, id):  
    owner_eventphotos = EventPhotos.objects.get(id=id)  
    form = EventPhotosForm(request.POST, instance = owner_eventphotos)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_eventphotosshow")  
    return render(request, 'owner_eventphotosedit.html', {'owner_eventphotos': owner_eventphotos})  
def owner_eventphotosdestroy(request, id):  
    owner_eventphotos = EventPhotos.objects.get(id=id)  
    owner_eventphotos.delete()  
    return redirect("/owner_eventphotosshow")

def owner_vehicledetailsinsert(request):  
    if request.method == "POST":  
        form = VehicleDetailsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_vehicledetailsshow')  
            except:  
                pass  
    else:  
        form = VehicleDetailsForm()  
    return render(request,'owner_vehicledetailsindex.html',{'form':form})  
def owner_vehicledetailsshow(request):  
    owner_vehicledetailss = VehicleDetails.objects.all()  
    return render(request,"owner_vehicledetailsshow.html",{'owner_vehicledetailss':owner_vehicledetailss})  

def owner_vehicledetailsedit(request, id):  
    owner_vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(instance=owner_vehicledetails)
    return render(request,'owner_vehicledetailsedit.html', {'owner_vehicledetails':owner_vehicledetails,'form':form})  

def owner_vehicledetailsupdate(request, id):  
    owner_vehicledetails = VehicleDetails.objects.get(id=id)  
    form = VehicleDetailsForm(request.POST, instance = owner_vehicledetails)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_vehicledetailsshow")  
    return render(request, 'owner_vehicledetailsedit.html', {'owner_vehicledetails': owner_vehicledetails})  
def owner_vehicledetailsdestroy(request, id):  
    owner_vehicledetails = VehicleDetails.objects.get(id=id)  
    owner_vehicledetails.delete()  
    return redirect("/owner_vehicledetailsshow")

def owner_visitorentryinsert(request):  
    if request.method == "POST":  
        form = VisitorentryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_visitorentryshow')  
            except:  
                pass  
    else:  
        form = VisitorentryForm()  
    return render(request,'owner_visitorentryindex.html',{'form':form})  
def owner_visitorentryshow(request):  
    owner_visitorentrys = Visitorentry.objects.all()  
    return render(request,"owner_visitorentryshow.html",{'owner_visitorentrys':owner_visitorentrys})  
def owner_visitorentryedit(request, id):  
    owner_visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(instance=owner_visitorentry)
    return render(request,'owner_visitorentryedit.html', {'owner_visitorentry':owner_visitorentry,'form':form})  

def owner_visitorentryupdate(request, id):  
    owner_visitorentry = Visitorentry.objects.get(id=id)  
    form = VisitorentryForm(request.POST, instance = owner_visitorentry)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_visitorentryshow")  
    return render(request, 'owner_visitorentryedit.html', {'owner_visitorentry': owner_visitorentry})  
def owner_visitorentrydestroy(request, id):  
    owner_visitorentry = Visitorentry.objects.get(id=id)  
    owner_visitorentry.delete()  
    return redirect("/owner_visitorentryshow")

def owner_expenseinsert(request):  
    if request.method == "POST":  
        form = ExpenseForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_expenseshow')  
            except:  
                pass  
    else:  
        form = ExpenseForm()  
    return render(request,'owner_expenseindex.html',{'form':form})  
def owner_expenseshow(request):  
    owner_expenses = Expense.objects.all()  
    return render(request,"owner_expenseshow.html",{'owner_expenses':owner_expenses})  
def owner_expenseedit(request, id):  
    owner_expense = Expense.objects.get(id=id)  
    form = ExpenseForm(instance=owner_expense)
    return render(request,'owner_expenseedit.html', {'owner_expense':owner_expense,'form':form})  

def owner_expenseupdate(request, id):  
    owner_expense = Expense.objects.get(id=id)  
    form = ExpenseForm(request.POST, instance = owner_expense) 
    print(form) 
    if form.is_valid():  
        form.save()  
        return redirect("/owner_expenseshow") 
    else:
        print(form.errors)
    return render(request, 'expenseedit.html', {'owner_expense': owner_expense})  
def owner_expensedestroy(request, id):  
    owner_expense = Expense.objects.get(id=id)  
    owner_expense.delete()  
    return redirect("/owner_expenseshow")

def owner_incomeinsert(request):  
    if request.method == "POST":  
        form = IncomeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_incomeshow')  
            except:  
                pass  
    else:  
        form = IncomeForm()  
    return render(request,'owner_incomeindex.html',{'form':form})  
def owner_incomeshow(request):  
    owner_incomes = Income.objects.all()  
    return render(request,"owner_incomeshow.html",{'owner_incomes':owner_incomes})  
def owner_incomeedit(request, id):  
    owner_income = Income.objects.get(id=id)  
    form = IncomeForm(instance=owner_income)
    return render(request,'owner_incomeedit.html', {'owner_income':owner_income,'form':form})  

def owner_incomeupdate(request, id):  
    owner_income = Income.objects.get(id=id)  
    form = IncomeForm(request.POST, instance = owner_income)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_incomeshow")  
    return render(request, 'owner_incomeedit.html', {'owner_income': owner_income})  
def owner_incomedestroy(request, id):  
    owner_income = Income.objects.get(id=id)  
    owner_income.delete()  
    return redirect("/owner_incomeshow") 

def owner_renteeinsert(request):  
    if request.method == "POST":  
        form = RenteeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_renteeshow')  
            except:  
                pass  
    else:  
        form = RenteeForm()  
    return render(request,'owner_renteeindex.html',{'form':form})  
def owner_renteeshow(request):  
    owner_rentees = Rentee.objects.all()  
    return render(request,"owner_renteeshow.html",{'owner_rentees':owner_rentees})  
def owner_renteeedit(request, id):  
    owner_rentee = Rentee.objects.get(id=id)  
    form = RenteeForm(instance=owner_rentee)
    return render(request,'owner_renteeedit.html', {'owner_rentee':owner_rentee,'form':form})  

def owner_renteeupdate(request, id):  
    owner_rentee = Rentee.objects.get(id=id)  
    form = RenteeForm(request.POST, instance = owner_rentee)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_renteeshow")  
    return render(request, 'owner_renteeedit.html', {'owner_rentee':owner_rentee})  
def owner_renteedestroy(request, id):  
    owner_rentee = Rentee.objects.get(id=id)  
    owner_rentee.delete()  
    return redirect("/owner_renteeshow")

def owner_serviceinsert(request):  
    if request.method == "POST":  
        form = ServiceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_serviceshow')  
            except:  
                pass  
    else:  
        form = ServiceForm()  
    return render(request,'owner_serviceindex.html',{'form':form})  
def owner_serviceshow(request):  
    owner_services = Service.objects.all()  
    return render(request,"owner_serviceshow.html",{'owner_services':owner_services})  
def owner_serviceedit(request, id):  
    owner_service = Service.objects.get(id=id)  
    form = ServiceForm(instance=owner_service)
    return render(request,'owner_serviceedit.html', {'owner_service':owner_service,'form':form})  

def owner_serviceupdate(request, id):  
    owner_service = Service.objects.get(id=id)  
    form = ServiceForm(request.POST, instance = owner_service)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_serviceshow")  
    return render(request, 'owner_serviceedit.html', {'owner_service': owner_service})  
def owner_servicedestroy(request, id):  
    owner_service = Service.objects.get(id=id)  
    owner_service.delete()  
    return redirect("/owner_serviceshow")

def owner_serviceproviderinsert(request):  
    if request.method == "POST":  
        form = ServiceProviderForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_serviceprovidershow')  
            except:  
                pass  
    else:  
        form = ServiceProviderForm()  
    return render(request,'owner_serviceproviderindex.html',{'form':form}) 
def owner_serviceprovidershow(request):  
    owner_serviceproviders = ServiceProvider.objects.all()  
    return render(request,"owner_serviceprovidershow.html",{'owner_serviceproviders':owner_serviceproviders})  
def owner_serviceprovideredit(request, id):  
    owner_serviceprovider = ServiceProvider.objects.get(id=id)  
    form = ServiceProviderForm(instance=owner_serviceprovider)
    return render(request,'owner_serviceprovideredit.html', {'owner_serviceprovider':owner_serviceprovider,'form':form})  

def owner_serviceproviderupdate(request, id):  
    owner_serviceprovider = ServiceProvider.objects.get(id=id)  
    form = ServiceProviderForm(request.POST, instance = owner_serviceprovider)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_serviceprovidershow")  
    return render(request, 'owner_serviceprovideredit.html', {'owner_serviceprovider': owner_serviceprovider})  
def owner_serviceproviderdestroy(request, id):  
    owner_serviceprovider = ServiceProvider.objects.get(id=id)  
    owner_serviceprovider.delete()  
    return redirect("/owner_serviceprovidershow")

def owner_complaininsert(request):  
    if request.method == "POST":  
        form = ComplainForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_complainshow')  
            except:  
                pass  
    else:  
        form = ComplainForm()  
    return render(request,'owner_complainindex.html',{'form':form})  
def owner_complainshow(request):  
    owner_complains = Complain.objects.all()  
    return render(request,"owner_complainshow.html",{'owner_complains':owner_complains})  
def owner_complainedit(request, id):  
    owner_complain = Complain.objects.get(id=id)  
    form = ComplainForm(instance=owner_complain)
    return render(request,'owner_complainedit.html', {'owner_complain':owner_complain,'form':form})  

def owner_complainupdate(request, id):  
    owner_complain = Complain.objects.get(id=id)  
    form = ComplainForm(request.POST, instance = owner_complain)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_complainshow")  
    return render(request, 'owner_complainedit.html', {'owner_complain': owner_complain})  
def owner_complaindestroy(request, id):  
    owner_complain = Complain.objects.get(id=id)  
    owner_complain.delete()  
    return redirect("/owner_complainshow")

def owner_solutioninsert(request):  
    if request.method == "POST":  
        form = SolutionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/owner_solutionshow')  
            except:  
                pass  
    else:  
        form = SolutionForm()  
    return render(request,'owner_solutionindex.html',{'form':form})  
def owner_solutionshow(request):  
    owner_solutions = Solution.objects.all()  
    return render(request,"owner_solutionshow.html",{'owner_solutions':owner_solutions})  
def owner_solutionedit(request, id):  
    owner_solution = Solution.objects.get(id=id)  
    form = SolutionForm(instance=owner_solution)
    return render(request,'owner_solutionedit.html', {'owner_solution':owner_solution,'form':form})  

def owner_solutionupdate(request, id):  
    owner_solution = Solution.objects.get(id=id)  
    form = SolutionForm(request.POST, instance = owner_solution)  
    if form.is_valid():  
        form.save()  
        return redirect("/owner_solutionshow")  
    return render(request, 'owner_solutionedit.html', {'owner_solution': owner_solution})  
def owner_solutiondestroy(request, id):  
    owner_solution = Solution.objects.get(id=id)  
    owner_solution.delete()  
    return redirect("/owner_solutionshow")