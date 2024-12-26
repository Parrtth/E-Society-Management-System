"""esociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path,include



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('forgot1', views.forgot1, name='forgot1'),
    path('forgot3/<int:id>', views.forgot3, name='forgot3'),
    path('admin_home',views.admin_home),
  
    path('logininsert', views.logininsert),  
    path('loginshow',views.loginshow),  
    path('loginedit/<int:id>', views.loginedit),  
    path('loginupdate/<int:id>', views.loginupdate),  
    path('logindelete/<int:id>', views.logindestroy),
    
    path('blockinsert', views.blockinsert),  
    path('blockshow',views.blockshow),  
    path('blockedit/<int:id>', views.blockedit),  
    path('blockupdate/<int:id>', views.blockupdate),  
    path('blockdelete/<int:id>', views.blockdestroy),
    
    path('societyinsert', views.societyinsert),  
    path('societyshow',views.societyshow),  
    path('societyedit/<int:id>', views.societyedit),  
    path('societyupdate/<int:id>', views.societyupdate),  
    path('societydelete/<int:id>', views.societydestroy),
    
    path('unittypeinsert', views.unittypeinsert),  
    path('unittypeshow',views.unittypeshow),  
    path('unittypeedit/<int:id>', views.unittypeedit),  
    path('unittypeupdate/<int:id>', views.unittypeupdate),  
    path('unittypedelete/<int:id>', views.unittypedestroy),
    
    path('unitinsert', views.unitinsert),  
    path('unitshow',views.unitshow),  
    path('unitedit/<int:id>', views.unitedit),  
    path('unitupdate/<int:id>', views.unitupdate),  
    path('unitdelete/<int:id>', views.unitdestroy),
    
    path('ownerinsert', views.ownerinsert),  
    path('ownershow',views.ownershow),  
    path('owneredit/<int:id>', views.owneredit),  
    path('ownerupdate/<int:id>', views.ownerupdate),  
    path('ownerdelete/<int:id>', views.ownerdestroy),  

    path('renteeinsert', views.renteeinsert),  
    path('renteeshow',views.renteeshow),  
    path('renteeedit/<int:id>', views.renteeedit),  
    path('renteeupdate/<int:id>', views.renteeupdate),  
    path('renteedelete/<int:id>', views.renteedestroy),  
    
    path('serviceinsert', views.serviceinsert),  
    path('serviceshow',views.serviceshow),  
    path('serviceedit/<int:id>', views.serviceedit),  
    path('serviceupdate/<int:id>', views.serviceupdate),  
    path('servicedelete/<int:id>', views.servicedestroy),
    
    path('securityinsert', views.securityinsert),  
    path('securityshow',views.securityshow),  
    path('securityedit/<int:id>', views.securityedit),  
    path('securityupdate/<int:id>', views.securityupdate),  
    path('securitydelete/<int:id>', views.securitydestroy),
    
    path('committeeinsert', views.committeeinsert),  
    path('committeeshow',views.committeeshow),  
    path('committeeedit/<int:id>', views.committeeedit),  
    path('committeeupdate/<int:id>', views.committeeupdate),  
    path('committeedelete/<int:id>', views.committeedestroy),
    
    path('serviceproviderinsert', views.serviceproviderinsert),  
    path('serviceprovidershow',views.serviceprovidershow),  
    path('serviceprovideredit/<int:id>', views.serviceprovideredit),  
    path('serviceproviderupdate/<int:id>', views.serviceproviderupdate),  
    path('serviceproviderdelete/<int:id>', views.serviceproviderdestroy),
    
    path('expenseinsert', views.expenseinsert),  
    path('expenseshow',views.expenseshow),  
    path('expenseedit/<int:id>', views.expenseedit),  
    path('expenseupdate/<int:id>', views.expenseupdate),  
    path('expensedelete/<int:id>', views.expensedestroy),
    
    path('incomeinsert', views.incomeinsert),  
    path('incomeshow',views.incomeshow),  
    path('incomeedit/<int:id>', views.incomeedit),  
    path('incomeupdate/<int:id>', views.incomeupdate),  
    path('incomedelete/<int:id>', views.incomedestroy),
    
    path('complaininsert', views.complaininsert),  
    path('complainshow',views.complainshow),  
    path('complainedit/<int:id>', views.complainedit),  
    path('complainupdate/<int:id>', views.complainupdate),  
    path('complaindelete/<int:id>', views.complaindestroy),
    
    path('solutioninsert', views.solutioninsert),  
    path('solutionshow',views.solutionshow),  
    path('solutionedit/<int:id>', views.solutionedit),  
    path('solutionupdate/<int:id>', views.solutionupdate),  
    path('solutiondelete/<int:id>', views.solutiondestroy),
    
    path('circularsinsert', views.circularsinsert),  
    path('circularsshow',views.circularsshow),  
    path('circularsedit/<int:id>', views.circularsedit),  
    path('circularsupdate/<int:id>', views.circularsupdate),  
    path('circularsdelete/<int:id>', views.circularsdestroy),
    
    path('eventinsert', views.eventinsert),  
    path('eventshow',views.eventshow),  
    path('eventedit/<int:id>', views.eventedit),  
    path('eventupdate/<int:id>', views.eventupdate),  
    path('eventdelete/<int:id>', views.eventdestroy),
    
    path('eventphotosinsert', views.eventphotosinsert),  
    path('eventphotosshow',views.eventphotosshow),  
    path('eventphotosedit/<int:id>', views.eventphotosedit),  
    path('eventphotosupdate/<int:id>', views.eventphotosupdate),  
    path('eventphotosdelete/<int:id>', views.eventphotosdestroy),
    
    path('vehicledetailsinsert', views.vehicledetailsinsert),  
    path('vehicledetailsshow',views.vehicledetailsshow),  
    path('vehicledetailsedit/<int:id>', views.vehicledetailsedit),  
    path('vehicledetailsupdate/<int:id>', views.vehicledetailsupdate),  
    path('vehicledetailsdelete/<int:id>', views.vehicledetailsdestroy),
    
    path('visitorentryinsert', views.visitorentryinsert),  
    path('visitorentryshow',views.visitorentryshow),  
    path('visitorentryedit/<int:id>', views.visitorentryedit),  
    path('visitorentryupdate/<int:id>', views.visitorentryupdate),  
    path('visitorentrydelete/<int:id>', views.visitorentrydestroy),
    
    path('security_home',views.security_home),
    
    path('security_vehicledetailsinsert', views.security_vehicledetailsinsert),  
    path('security_vehicledetailsshow',views.security_vehicledetailsshow),  
    path('security_vehicledetailsedit/<int:id>', views.security_vehicledetailsedit),  
    path('security_vehicledetailsupdate/<int:id>', views.security_vehicledetailsupdate),  
    path('security_vehicledetailsdelete/<int:id>', views.security_vehicledetailsdestroy),
    
    path('security_visitorentryinsert', views.security_visitorentryinsert),  
    path('security_visitorentryshow',views.security_visitorentryshow),  
    path('security_visitorentryedit/<int:id>', views.security_visitorentryedit),  
    path('security_visitorentryupdate/<int:id>', views.security_visitorentryupdate),  
    path('security_visitorentrydelete/<int:id>', views.security_visitorentrydestroy),
    
    path('rentee_home',views.rentee_home),
    
    path('rentee_committeeinsert', views.rentee_committeeinsert),  
    path('rentee_committeeshow',views.rentee_committeeshow),  
    path('rentee_committeeedit/<int:id>', views.rentee_committeeedit),  
    path('rentee_committeeupdate/<int:id>', views.rentee_committeeupdate),  
    path('rentee_committeedelete/<int:id>', views.rentee_committeedestroy),
    
    path('rentee_circularsinsert', views.rentee_circularsinsert),  
    path('rentee_circularsshow',views.rentee_circularsshow),  
    path('rentee_circularsedit/<int:id>', views.rentee_circularsedit),  
    path('rentee_circularsupdate/<int:id>', views.rentee_circularsupdate),  
    path('rentee_circularsdelete/<int:id>', views.rentee_circularsdestroy),
    
    path('rentee_eventinsert', views.rentee_eventinsert),  
    path('rentee_eventshow',views.rentee_eventshow),  
    path('rentee_eventedit/<int:id>', views.rentee_eventedit),  
    path('rentee_eventupdate/<int:id>', views.rentee_eventupdate),  
    path('rentee_eventdelete/<int:id>', views.rentee_eventdestroy),
    
    path('rentee_eventphotosinsert', views.rentee_eventphotosinsert),  
    path('rentee_eventphotosshow',views.rentee_eventphotosshow),  
    path('rentee_eventphotosedit/<int:id>', views.rentee_eventphotosedit),  
    path('rentee_eventphotosupdate/<int:id>', views.rentee_eventphotosupdate),  
    path('rentee_eventphotosdelete/<int:id>', views.rentee_eventphotosdestroy),
    
    path('rentee_vehicledetailsinsert', views.rentee_vehicledetailsinsert),  
    path('rentee_vehicledetailsshow',views.rentee_vehicledetailsshow),  
    path('rentee_vehicledetailsedit/<int:id>', views.rentee_vehicledetailsedit),  
    path('rentee_vehicledetailsupdate/<int:id>', views.rentee_vehicledetailsupdate),  
    path('rentee_vehicledetailsdelete/<int:id>', views.rentee_vehicledetailsdestroy),
    
    path('rentee_visitorentryinsert', views.rentee_visitorentryinsert),  
    path('rentee_visitorentryshow',views.rentee_visitorentryshow),  
    path('rentee_visitorentryedit/<int:id>', views.rentee_visitorentryedit),  
    path('rentee_visitorentryupdate/<int:id>', views.rentee_visitorentryupdate),  
    path('rentee_visitorentrydelete/<int:id>', views.rentee_visitorentrydestroy),
    
    path('rentee_serviceinsert', views.rentee_serviceinsert),  
    path('rentee_serviceshow',views.rentee_serviceshow),  
    path('rentee_serviceedit/<int:id>', views.rentee_serviceedit),  
    path('rentee_serviceupdate/<int:id>', views.rentee_serviceupdate),  
    path('rentee_servicedelete/<int:id>', views.rentee_servicedestroy),
    
    path('rentee_serviceproviderinsert', views.rentee_serviceproviderinsert),  
    path('rentee_serviceprovidershow',views.rentee_serviceprovidershow),  
    path('rentee_serviceprovideredit/<int:id>', views.rentee_serviceprovideredit),  
    path('rentee_serviceproviderupdate/<int:id>', views.rentee_serviceproviderupdate),  
    path('rentee_serviceproviderdelete/<int:id>', views.rentee_serviceproviderdestroy),
    
    path('rentee_complaininsert', views.rentee_complaininsert),  
    path('rentee_complainshow',views.rentee_complainshow),  
    path('rentee_complainedit/<int:id>', views.rentee_complainedit),  
    path('rentee_complainupdate/<int:id>', views.rentee_complainupdate),  
    path('rentee_complaindelete/<int:id>', views.rentee_complaindestroy),
    
    path('rentee_solutioninsert', views.rentee_solutioninsert),  
    path('rentee_solutionshow',views.rentee_solutionshow),  
    path('rentee_solutionedit/<int:id>', views.rentee_solutionedit),  
    path('rentee_solutionupdate/<int:id>', views.rentee_solutionupdate),  
    path('rentee_solutiondelete/<int:id>', views.rentee_solutiondestroy),
    
    path('owner_home',views.owner_home),
    
    path('owner_committeeinsert', views.owner_committeeinsert),  
    path('owner_committeeshow',views.owner_committeeshow),  
    path('owner_committeeedit/<int:id>', views.owner_committeeedit),  
    path('owner_committeeupdate/<int:id>', views.owner_committeeupdate),  
    path('owner_committeedelete/<int:id>', views.owner_committeedestroy),
    
    path('owner_circularsinsert', views.owner_circularsinsert),  
    path('owner_circularsshow',views.owner_circularsshow),  
    path('owner_circularsedit/<int:id>', views.owner_circularsedit),  
    path('owner_circularsupdate/<int:id>', views.owner_circularsupdate),  
    path('owner_circularsdelete/<int:id>', views.owner_circularsdestroy),
    
    path('owner_eventinsert', views.owner_eventinsert),  
    path('owner_eventshow',views.owner_eventshow),  
    path('owner_eventedit/<int:id>', views.owner_eventedit),  
    path('owner_eventupdate/<int:id>', views.owner_eventupdate),  
    path('owner_eventdelete/<int:id>', views.owner_eventdestroy),
    
    path('owner_eventphotosinsert', views.owner_eventphotosinsert),  
    path('owner_eventphotosshow',views.owner_eventphotosshow),  
    path('owner_eventphotosedit/<int:id>', views.owner_eventphotosedit),  
    path('owner_eventphotosupdate/<int:id>', views.owner_eventphotosupdate),  
    path('owner_eventphotosdelete/<int:id>', views.owner_eventphotosdestroy),
    
    path('owner_vehicledetailsinsert', views.owner_vehicledetailsinsert),  
    path('owner_vehicledetailsshow',views.owner_vehicledetailsshow),  
    path('owner_vehicledetailsedit/<int:id>', views.owner_vehicledetailsedit),  
    path('owner_vehicledetailsupdate/<int:id>', views.owner_vehicledetailsupdate),  
    path('owner_vehicledetailsdelete/<int:id>', views.owner_vehicledetailsdestroy),
    
    path('owner_visitorentryinsert', views.owner_visitorentryinsert),  
    path('owner_visitorentryshow',views.owner_visitorentryshow),  
    path('owner_visitorentryedit/<int:id>', views.owner_visitorentryedit),  
    path('owner_visitorentryupdate/<int:id>', views.owner_visitorentryupdate),  
    path('owner_visitorentrydelete/<int:id>', views.owner_visitorentrydestroy),
    
    path('owner_expenseinsert', views.owner_expenseinsert),  
    path('owner_expenseshow',views.owner_expenseshow),  
    path('owner_expenseedit/<int:id>', views.owner_expenseedit),  
    path('owner_expenseupdate/<int:id>', views.owner_expenseupdate),  
    path('owner_expensedelete/<int:id>', views.owner_expensedestroy),
    
    path('owner_incomeinsert', views.owner_incomeinsert),  
    path('owner_incomeshow',views.owner_incomeshow),  
    path('owner_incomeedit/<int:id>', views.owner_incomeedit),  
    path('owner_incomeupdate/<int:id>', views.owner_incomeupdate),  
    path('owner_incomedelete/<int:id>', views.owner_incomedestroy),
    
    path('owner_renteeinsert', views.owner_renteeinsert),  
    path('owner_renteeshow',views.owner_renteeshow),  
    path('owner_renteeedit/<int:id>', views.owner_renteeedit),  
    path('owner_renteeupdate/<int:id>', views.owner_renteeupdate),  
    path('owner_renteedelete/<int:id>', views.owner_renteedestroy),
    
    path('owner_serviceinsert', views.owner_serviceinsert),  
    path('owner_serviceshow',views.owner_serviceshow),  
    path('owner_serviceedit/<int:id>', views.owner_serviceedit),  
    path('owner_serviceupdate/<int:id>', views.owner_serviceupdate),  
    path('owner_servicedelete/<int:id>', views.owner_servicedestroy),
    
    path('owner_serviceproviderinsert', views.owner_serviceproviderinsert),  
    path('owner_serviceprovidershow',views.owner_serviceprovidershow),  
    path('owner_serviceprovideredit/<int:id>', views.owner_serviceprovideredit),  
    path('owner_serviceproviderupdate/<int:id>', views.owner_serviceproviderupdate),  
    path('owner_serviceproviderdelete/<int:id>', views.owner_serviceproviderdestroy),
    
    path('owner_complaininsert', views.owner_complaininsert),  
    path('owner_complainshow',views.owner_complainshow),  
    path('owner_complainedit/<int:id>', views.owner_complainedit),  
    path('owner_complainupdate/<int:id>', views.owner_complainupdate),  
    path('owner_complaindelete/<int:id>', views.owner_complaindestroy),
    
    path('owner_solutioninsert', views.owner_solutioninsert),  
    path('owner_solutionshow',views.owner_solutionshow),  
    path('owner_solutionedit/<int:id>', views.owner_solutionedit),  
    path('owner_solutionupdate/<int:id>', views.owner_solutionupdate),  
    path('owner_solutiondelete/<int:id>', views.owner_solutiondestroy),
    path('download', views.download)


]