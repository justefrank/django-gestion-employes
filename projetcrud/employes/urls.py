from django.urls import path
from .views import EmployeListView, EmployeAjout, EmployEdit, EmployeDelete

urlpatterns =[
    path('', EmployeListView.as_view(), name='employe_list'),
    path('ajout/', EmployeAjout.as_view(), name = 'employe_ajout'),
    path('edit/<int:pk>/', EmployEdit.as_view(), name='employe_edit'),
    path('delete/<int:pk>/', EmployeDelete.as_view(), name='employe_delete')
]