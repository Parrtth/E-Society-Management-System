from django.db import models

USER_TYPES = (
    ('security','Security'),
    ('owner', 'Owner'),
    ('rentee','Rentee'),
    ('admin','Admin'),
    
)
SEC_QUES = (
    ('What is your Society Name?','What is your Society Name?'),
    ('What is your Share No?', 'What is your Share No?'),
    ('What is your Blood Group?','What is your Blood Group?'),
    ('What is your First School Name?','What is your First School Name?'),
    
)
STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)
# Create your models here.
class Login(models.Model):  
    id = models.AutoField
    mobileno = models.CharField(max_length=12)  
    password = models.CharField(max_length=20)  
    usertype =models.CharField(max_length=15, choices=USER_TYPES, default='Rentee')
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    registerdate = models.DateField(max_length=15)
    security_question = models.CharField(max_length=255,choices=SEC_QUES, default='What is your Society Name?')
    answer=models.CharField(max_length=255)
    def __str__(self):
        return self.mobileno
    
    class Meta:  
        db_table = "tbllogin"  
        
class Block(models.Model):  
    blockid = models.AutoField  
    blockname = models.CharField(max_length=8)  
    def __str__(self):
        return self.blockname
    
    class Meta:  
        db_table = "tblblock" 
    
class Society(models.Model):  
    societyid = models.AutoField  
    societyname = models.CharField(max_length=15)  
    logo = models.CharField(max_length=10)  
    address = models.CharField(max_length=300) 
    class Meta:  
        db_table = "tblsociety"  

class UnitType(models.Model):  
    unittypeid = models.AutoField  
    unittype = models.CharField(max_length=10)
    def __str__(self):
        return self.unittype
    
    class Meta:  
        db_table = "tblunittype" 

STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)

class Unit(models.Model):  
    unitid = models.AutoField  
    blockid = models.ForeignKey("Block",on_delete=models.CASCADE)
    unittypeid = models.ForeignKey("UnitType",on_delete=models.CASCADE)
    unitno = models.CharField(max_length=15) 
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    floorno = models.CharField(max_length=15)
    parkingno = models.CharField(max_length=15)
    def __str__(self):
        return self.unitno
    
    class Meta:  
        db_table = "tblunit"  


class Owner(models.Model):  
    ownerid = models.AutoField  
    ownername = models.CharField(max_length=12)  
    address = models.CharField(max_length=300)  
    shareno = models.CharField(max_length=15) 
    registerdate = models.DateField(max_length=15)
    unitid = models.ForeignKey("Unit",on_delete=models.CASCADE)
    fromdate = models.DateField(max_length=15)
    todate = models.DateField(max_length=15)
    loginid = models.ForeignKey("Login",on_delete=models.CASCADE)
    totalfamilymembers = models.CharField(max_length=10)
    class Meta:  
        db_table = "tblowner"  

STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)

class Rentee(models.Model):  
    renteeid = models.AutoField  
    unitid = models.ForeignKey("Unit",on_delete=models.CASCADE)  
    name = models.CharField(max_length=20)  
    rentagreementdt = models.DateField(max_length=15) 
    loginid = models.ForeignKey("Login",on_delete=models.CASCADE)
    permanentaddress = models.CharField(max_length=300)
    fromdate = models.DateField(max_length=15)
    todate = models.DateField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    class Meta:  
        db_table = "tblrentee"  

class Service(models.Model):  
    serviceid = models.AutoField  
    servicename = models.CharField(max_length=20)  
    def __str__(self):
        return self.servicename
    
    class Meta:  
        db_table = "tblservice" 

STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)
        
class Security(models.Model):  
    securityid = models.AutoField  
    agencyname = models.CharField(max_length=12)  
    personname = models.CharField(max_length=20)   
    fromdate = models.DateField(max_length=15)
    todate = models.DateField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    loginid = models.ForeignKey("Login",on_delete=models.CASCADE)
    def __str__(self):
        return self.personname
    
    class Meta:  
        db_table = "tblsecurity"  

class Committee(models.Model):  
    committeeid = models.AutoField  
    membersname = models.CharField(max_length=12)  
    unitid = models.ForeignKey("Unit",on_delete=models.CASCADE) 
    foryear = models.DateField(max_length=15)  
    fromdate = models.DateField(max_length=15)
    todate = models.DateField(max_length=15)
    class Meta:  
        db_table = "tblcommittee"  

STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)

class ServiceProvider(models.Model):  
    serviceproid = models.AutoField  
    serviceproname = models.CharField(max_length=12)  
    servicedetails = models.CharField(max_length=200) 
    contactno = models.CharField(max_length=15)  
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    class Meta:  
        db_table = "tblserviceprovider"  

class Expense(models.Model):  
    expenseid = models.AutoField  
    Loginid = models.ForeignKey("Login",on_delete=models.CASCADE)  
    details = models.CharField(max_length=100) 
    amount = models.FloatField(max_length=25)  
    expencedate = models.DateField(max_length=15)
    expencetitle = models.CharField(max_length=15) 
    class Meta:  
        db_table = "tblexpense"  

class Income(models.Model):  
    incomeid = models.AutoField  
    Loginid = models.ForeignKey("Login",on_delete=models.CASCADE) 
    incometitle = models.CharField(max_length=25)
    incomedetails = models.CharField(max_length=200) 
    amount = models.FloatField(max_length=25)  
    incomedate = models.DateField(max_length=15) 
    class Meta:  
        db_table = "tblincome"  
        
STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)
        
class Complain(models.Model):  
    complainid = models.AutoField  
    Loginid = models.ForeignKey("Login",on_delete=models.CASCADE)  
    serviceid = models.ForeignKey("Service",on_delete=models.CASCADE)
    title = models.CharField(max_length=20) 
    details = models.CharField(max_length=250)  
    complaindate = models.DateField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    def __str__(self):
        return self.title
    
    class Meta:  
        db_table = "tblcomplain"  
        
class Solution(models.Model):  
    solutionid = models.AutoField  
    complainid = models.ForeignKey("Complain",on_delete=models.CASCADE) 
    solutiondetails = models.CharField(max_length=300)  
    date = models.DateField(max_length=10) 
    class Meta:  
        db_table = "tblsolution"  

STATUS = (
    ('active','Active'),
    ('inactive', 'Inactive'),
    
)

class Circulars(models.Model):  
    circularsid = models.AutoField  
    Loginid = models.ForeignKey("Login",on_delete=models.CASCADE)
    title = models.CharField(max_length=20) 
    filename = models.FileField(upload_to='documents/')
    date = models.DateField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    class Meta:  
        db_table = "tblcirculars"  
        
class Event(models.Model):  
    eventid = models.AutoField  
    eventdate = models.DateField(max_length=12)  
    eventtitle = models.CharField(max_length=20)   
    fromdate = models.DateField(max_length=15)
    todate = models.DateField(max_length=15)
    def __str__(self):
        return self.eventtitle
    
    class Meta:  
        db_table = "tblevent"  

class EventPhotos(models.Model):  
    photosid = models.AutoField    
    eventid = models.ForeignKey("Event",on_delete=models.CASCADE) 
    photopath =  models.FileField(upload_to='eventphoto/') 
    class Meta:  
        db_table = "tbleventphotos"  

class VehicleDetails(models.Model):  
    vehicleid = models.AutoField  
    vehicleno = models.CharField(max_length=12)  
    unitid = models.ForeignKey("Unit",on_delete=models.CASCADE)
    loginid = models.ForeignKey("Login",on_delete=models.CASCADE) 
    vehicletype = models.CharField(max_length=15)
    class Meta:  
        db_table = "tblvehicledetails" 
        
class Visitorentry(models.Model):
    visitorid = models.AutoField
    visitorname = models.CharField(max_length=20)
    mobileno = models.CharField(max_length=12)
    date = models.DateField(max_length=15)
    unitid = models.ForeignKey("Unit",on_delete=models.CASCADE)
    reason = models.CharField(max_length=60)         
    securityid = models.ForeignKey("Security",on_delete=models.CASCADE)
    class Meta:  
        db_table = "tblvisitorentry"