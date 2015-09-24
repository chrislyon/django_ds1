from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from cr2.models import Book, Author, AuthorForm

def cr2_list(request, template_name='cr2/cr2_list.html'):
    cr2s = Author.objects.all()
    data = {}
    data['object_list'] = cr2s
    return render(request, template_name, data)

def cr2_create(request, template_name='cr2/cr2_form.html'):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cr2_list')
    return render(request, template_name, {'form':form})

def cr2_update(request, pk, template_name='cr2/cr2_form.html'):
    cr2 = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=cr2)
    if form.is_valid():
        form.save()
        return redirect('cr2_list')
    return render(request, template_name, {'form':form})

def cr2_delete(request, pk, template_name='cr2/cr2_confirm_delete.html'):
    cr2 = get_object_or_404(Author, pk=pk)    
    if request.method=='POST':
        cr2.delete()
        return redirect('cr2_list')
    return render(request, template_name, {'object':cr2})
