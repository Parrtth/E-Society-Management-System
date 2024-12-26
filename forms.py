from django import forms  
from .models import Login
from .models import Block
from .models import Society
from .models import UnitType
from .models import Unit
from .models import Owner
from .models import Rentee
from .models import Service
from .models import Security
from .models import Committee
from .models import ServiceProvider
from .models import Expense
from .models import Income
from .models import Complain
from .models import Solution
from .models import Circulars
from .models import Event
from .models import EventPhotos
from .models import VehicleDetails
from .models import Visitorentry

class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class LoginForm(forms.ModelForm):  
    class Meta:  
        model = Login  
        fields = "__all__"  
        widgets = {
            'registerdate': DateInput()
        }

class BlockForm(forms.ModelForm):  
    class Meta:  
        model = Block  
        fields = "__all__"  
        
class SocietyForm(forms.ModelForm):  
    class Meta:  
        model = Society 
        fields = "__all__"  
        
class UnitTypeForm(forms.ModelForm):  
    class Meta:  
        model = UnitType 
        fields = "__all__"
        
class UnitForm(forms.ModelForm):  
    class Meta:  
        model = Unit 
        fields = "__all__"
        
class OwnerForm(forms.ModelForm):  
    class Meta:  
        model = Owner 
        fields = "__all__"
        widgets = {
            'registerdate': DateInput(),
            'fromdate':DateInput(),
            'todate':DateInput()
        }
        
class RenteeForm(forms.ModelForm):  
    class Meta:  
        model = Rentee 
        fields = "__all__"
        widgets = {
            'rentagreementdt': DateInput(),
            'fromdate':DateInput(),
            'todate':DateInput()
        }
        
class ServiceForm(forms.ModelForm):  
    class Meta:  
        model = Service
        fields = "__all__"
    
class SecurityForm(forms.ModelForm):  
    class Meta:  
        model = Security 
        fields = "__all__"
        widgets = {
            'fromdate':DateInput(),
            'todate':DateInput()
        }
        
class CommitteeForm(forms.ModelForm):  
    class Meta:  
        model = Committee 
        fields = "__all__"
        widgets = {
            'foryear': DateInput(),
            'fromdate':DateInput(),
            'todate':DateInput()
        }
    
class ServiceProviderForm(forms.ModelForm):  
    class Meta:  
        model = ServiceProvider
        fields = "__all__"
        
class ExpenseForm(forms.ModelForm):  
    class Meta:  
        model = Expense
        fields = "__all__"
        widgets = {
            'expencedate':DateInput()
        }
        
class IncomeForm(forms.ModelForm):  
    class Meta:  
        model = Income
        fields = "__all__"
        widgets = {
            'incomedate':DateInput()
        }
        
class ComplainForm(forms.ModelForm):  
    class Meta:  
        model = Complain
        fields = "__all__"
        widgets = {
            'complaindate':DateInput()
        }
        
class SolutionForm(forms.ModelForm):  
    class Meta:  
        model = Solution
        fields = "__all__"
        widgets = {
            'date':DateInput()
        }
    
class CircularsForm(forms.ModelForm):  
    class Meta:  
        model = Circulars
        fields = "__all__"
        widgets = {
            'date':DateInput()
        }
        
class EventForm(forms.ModelForm):  
    class Meta:  
        model = Event
        fields = "__all__"
        widgets = {
            'eventdate': DateInput(),
            'fromdate':DateInput(),
            'todate':DateInput()
        }
        
class EventPhotosForm(forms.ModelForm):  
    class Meta:  
        model = EventPhotos
        fields = "__all__"

class VehicleDetailsForm(forms.ModelForm):  
    class Meta:  
        model = VehicleDetails
        fields = "__all__"
        
class VisitorentryForm(forms.ModelForm):  
    class Meta:  
        model = Visitorentry
        fields = "__all__"
        widgets = {
            'date':DateInput()
        }