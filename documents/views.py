from django.shortcuts import redirect, render, get_object_or_404
from .models import Document
from .forms import DocumentForm


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
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


def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect('index')
