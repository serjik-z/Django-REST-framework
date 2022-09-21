# from .models import Item
# from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
#
# class ItemForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'price', 'image', 'author', 'date']
#         widgets = {
#             "name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Название товара'
#             }),
#              "price": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Цена товара'
#             }),
#             "image": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Изображение'
#             }),
#             "date": DateTimeInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Дата публикации'
#             }),
#
#         }