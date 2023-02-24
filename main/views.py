from django.shortcuts import render, redirect
from .models import WorkExample
from main.forms import ClientForm
# Create your views here.

def landing(request):
    work_examples = WorkExample.objects.all()
    context = {'works':work_examples}
    return render(request, 'main/landing.html', context)

def contact(request):
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
        else:
            context = {'form':form}
            return render(request, 'main/contact_form.html', context)     
    else:
        form = ClientForm
        context = {'form':form}
        return render(request, 'main/contact_form.html', context)
    
def confirmation(request):
    return render(request, 'main/confirmation.html')