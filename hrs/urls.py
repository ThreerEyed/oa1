from django.urls import path

from hrs import views

urlpatterns = [
    path('depts', views.depts, name='depts'),
    path('depts/emps/<int:no>', views.emps, name='empsindept'),
    path('deldept/<int:no>', views.del_dept, name='ddel'),
    path('add', views.add, name='add')
]
