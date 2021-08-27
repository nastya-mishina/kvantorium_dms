from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='')
    docfile.widget.attrs.update({'class': 'form-control', 'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;'})
