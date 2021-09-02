from datetime import datetime as dt

from django.db import models
from django.urls import reverse
from users.models import User


class AbstractModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    create_date = models.DateTimeField()
    mod_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
            self.create_date = dt.now()
        self.mod_date = dt.now()
        return super(AbstractModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(AbstractModel):
    name = models.CharField(max_length=30, unique=True, default='Default category')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('documents:category_detail', args=[self.id])

    @property
    def document_count(self):
        return Document.objects.filter(category_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']


class Document(AbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.TextField(max_length=30, verbose_name='Title', default='Default title')
    version_no = models.IntegerField(blank=True, verbose_name='Version No.', default=1)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True)
    
    # по дефолту идет привязка к 1 категории, потом переделать
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='documents', default=1)

    def __str__(self):
        return self.title

    def get_format(self):
        return self.docfile.url.split('.')[-1].upper()

    def get_absolute_url(self):
        return reverse('documents:document_detail', args=[str(self.id)])

    # переопределяем метод delete для удаления документа из файловой системы после удаления объекта модели
    def delete(self, *args, **kwargs):
        self.docfile.delete()
        super(Document, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['-mod_date']

