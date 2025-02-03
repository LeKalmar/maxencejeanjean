from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Page
from .forms import PageForm

def wiki(request):
    return render(request, 'wikiarras/wiki.html')

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'wikiarras/page_detail.html', {'page': page})

@login_required
def page_edit(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            page.last_modified_by = request.user
            page.save()
            return redirect('page_detail', page_id=page.id)
    else:
        form = PageForm(instance=page)
    return render(request, 'wikiarras/page_edit.html', {'form': form})