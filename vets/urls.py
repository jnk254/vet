from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='admdashboard'),
    path('registration',views.reg_member,name='regmember'),
    path('viewMembers',views.view_members, name='ViewMembers'),
    path('<int:id>/registration',views.reg_member,name='memberupdate'),
    path('<int:id>/viewMembers',views.view_members, name='ViewMembers'),
    
    path('signup',views.signup, name='Signup'),
    path('signin', views.signin, name='Signin'),
    path('reset',views.resetpassword, name='Reset-password'),
    
    path('create',views.createView),
    path('store',views.store,name='store') #handling POST Request 

]