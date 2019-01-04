from django.urls import re_path

from tenant_app import views

appname = 'tenant_app'

urlpatterns = [
    re_path('add/', views.add_tenant, name = 'add-tenant'),
    re_path('all_tenants', views.all_tenants, name = 'all-tenants'),
    # re_path('')
]