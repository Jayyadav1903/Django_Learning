from django.shortcuts import render
from.models import biryani_variety,store
from django.shortcuts import get_object_or_404
from .forms import BiryaniForm

# Create your views here.
def all_biryani(request):
    biryanis=biryani_variety.objects.all()
    return render(request, 'biryani/all_biryani.html',{'biryani_list':biryanis})

def biryani_detail(request, biryani_id):
    biryani = get_object_or_404(biryani_variety, id=biryani_id)
    return render(request, 'biryani/biryani_detail.html', {'biryani': biryani})

def biryani_stores_view(request):
    stores=None
    if request.method=="POST":
        form=BiryaniForm(request.POST)
        if form.is_valid():
            selected_biryani=form.cleaned_data['biryani_variety']
            stores=store.objects.filter(biryani=selected_biryani)
    else:
        form=BiryaniForm()    
    return render(request, 'biryani/biryani_stores.html', {'form':BiryaniForm(),'stores':stores} )