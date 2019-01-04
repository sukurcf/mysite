from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from tenant_app.models import Tenant
from .forms import TenantForm


def add_tenant(request):
    if request.method == 'GET':
        form = TenantForm()
        return render(request, 'tenant_app/tenant_add.html', {'form':form})
    elif request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            mobile_1 = form.cleaned_data['mobile_1']
            mobile_2 = form.cleaned_data['mobile_2']
            mobile_3 = form.cleaned_data['mobile_3']
            address_1 = form.cleaned_data['address_1']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            location = form.cleaned_data['location']
            tenant = Tenant(name=name, age=age, gender=gender, mobile_1=mobile_1, mobile_2=mobile_2, mobile_3=mobile_3, address_1=address_1, city=city, country=country, location=location)
            tenant.save()
            return render(request, 'tenant_app/tenant_add_success.html')
        else:
            error = 'Your data is <b style="color:red">NOT</b> saved because of the following errors: <br/>'+form.errors.as_json() +'<br/>Rectify them and resubmit with correct data'
            return HttpResponse(error)

def all_tenants(request):
    tenants = Tenant.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tenants, 100)
    try:
        tenants = paginator.page(page)
    except PageNotAnInteger:
        tenants = paginator.page(1)
    except EmptyPage:
        tenants = paginator.page(paginator.num_pages)
    return render(request, 'tenant_app/tenants_list.html', {'tenants':tenants})

def edit_tenant(request, id):
    if request.method == 'GET':
        tenant = Tenant.objects.get(pk=id)
        form = TenantForm(instance=tenant)
        return render(request, 'tenant_app/edit_tenant.html', {'form':form})
    elif request.method =='POST':
        tenant = Tenant.objects.get(pk=id)
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            tenant.name = form.cleaned_data['name']
            tenant.age = form.cleaned_data['age']
            tenant.gender = form.cleaned_data['gender']
            tenant.mobile_1 = form.cleaned_data['mobile_1']
            tenant.mobile_2 = form.cleaned_data['mobile_2']
            tenant.mobile_3 = form.cleaned_data['mobile_3']
            tenant.address_1 = form.cleaned_data['address_1']
            tenant.city = form.cleaned_data['city']
            tenant.country = form.cleaned_data['country']
            tenant.location = form.cleaned_data['location']
            tenant.save()
            return render(request, 'tenant_app/tenant_edit_success.html')
        else:
            error = 'Your data is <b style="color:red">NOT</b> saved because of the following errors: <br/>' + form.errors.as_json() + '<br/>Rectify them and resubmit with correct data'
            return HttpResponse(error)

def delete_tenant(request, id):
    tenant = Tenant.objects.get(pk = id)
    try:
        tenant.delete()
        return render(request, 'tenant_app/tenant_delete_success.html')
    except:
        return HttpResponseRedirect('www.google.com')
