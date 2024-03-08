from django.shortcuts import render,redirect
from stellar.forms import StellarForm
from stellar.models import Stellar
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = StellarForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StellarForm()
    return render(request,'index.html',{'form':form})
def show(request):
    employees = Stellar.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Stellar.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Stellar.objects.get(id=id)
    form = StellarForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
        employee = Stellar.objects.get(id=id)
        employee.delete()
        return redirect("/show")

    # Create your views here.
