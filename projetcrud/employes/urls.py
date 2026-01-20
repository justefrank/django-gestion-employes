from django.urls import path
from .views import EmployeListView, EmployeAjout, EmployEdit

urlpatterns =[
    path('', EmployeListView.as_view(), name='employe_list'),
    path('ajout/', EmployeAjout.as_view(), name = 'employe_ajout'),
    path('edit/<int:pk>/', EmployEdit.as_view(), name='employe_edit'),
]