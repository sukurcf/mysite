from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
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
            error = 'Your data is <b style="color:red">NOT</b> saved because of the following errors: <br/>'+form.errors.as_json() +'<br/>Go back and submit again with correct data'
            return HttpResponse(error)

def all_tenants(request):
    tenants = Tenant.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tenants, 2)
    try:
        tenants = paginator.page(page)
    except PageNotAnInteger:
        tenants = paginator.page(1)
    except EmptyPage:
        tenants = paginator.page(paginator.num_pages)
    return render(request, 'tenant_app/tenants_list.html', {'tenants':tenants})

def search(request):
    query = request.GET.get('q')
    if query:
        tenants = Tenant.objects.filter(
            Q(name__icontains=query) | Q(age__icontains=query) | Q(gender__icontains=query) | Q(mobile_1__icontains=query) | Q(mobile_2__icontains=query) | Q(mobile_3__icontains=query) | Q(address_1__icontains=query) | Q(city__icontains=query) | Q(country__icontains=query) | Q(location_icontains=query)
        ).distinct()
    return render(request, 'tenant_app/tenants_list.html', {'tenants':tenants})