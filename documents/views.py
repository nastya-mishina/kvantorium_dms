from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentForm
from .models import Document


@login_required
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'], author=request.user)
            newdoc.save()
            return redirect('index')
        else:
            message = 'Ошибка'
    else:
        form = DocumentForm()
        documents = Document.objects.all()
        context = {'documents': documents, 'form': form}
        return render(request, 'index.html', context)
    return render(request, 'index.html')


@login_required
def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect('index')


@login_required
def categoty_detail(request):
    pass


@login_required
def document_detail(request):
    pass


@login_required
def add_docuemnt(request):
    pass


@login_required
def add_category(request):
    pass
