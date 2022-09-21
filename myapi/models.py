from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=25)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField('.jpg', upload_to='static/img/', height_field=None, width_field=None, max_length=100)
    author = models.CharField('Автор', max_length=25)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
