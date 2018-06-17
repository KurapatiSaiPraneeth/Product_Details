from django.conf.urls import url
from .import views

app_name="budgetapp"

urlpatterns=[
    url(r'^Detail$', views.Detail,name = 'Detail'),
    url(r'^Dinsert$',views.Dinsert,name='Dinsert'),
    url(r'^Expense$',views.Expense,name='Expense'),
    url(r'^Einsert$',views.Einsert,name='Einsert'),
    url(r'^SplitBill$',views.SplitBill,name='SplitBill'),
    url(r'^Sinsert$',views.Sinsert,name='Sinsert'),
    url(r'^Sdisplay$',views.Sdisplay,name='Sdisplay')
]