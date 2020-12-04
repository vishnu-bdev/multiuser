from django.urls import path
from . import  views

urlpatterns=[
     path('',views.index, name='index'),
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('labour_register/',views.labour_register.as_view(), name='labour_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]

# Inside router we have:

# url inside router :== localhost:port_no/api/

# GET             - list      - localhost:port_no/api/employee
#                 - retrive   - localhost:port_no/api/employee/id

# POST, UPDATE or PUT, DELETE.
