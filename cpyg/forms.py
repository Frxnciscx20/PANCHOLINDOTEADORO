from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget 
from .models import Producto, Cliente , Categoria


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombre', 'marca', 'precio','imagen']
        labels ={
            'idProducto': 'idProducto', 
            'nombre': 'nombre', 
            'marca': 'marca', 
            'precio': 'precio',
            'imagen': 'imagen',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese idProducto', 
                    'id': 'idProducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            

        }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'comentario']
        labels ={
            'rut': 'rut', 
            'nombre': 'nombre', 
            'comentario': 'comentario', 
            
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'comentario': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese informacion', 
                    'id': 'comentario'
                }
            ),         

        }

class CategoriaForm(forms.ModelForm):

    class Meta: 
        model= Categoria
        fields = ['idCategoria', 'nombreCategoria']
        labels ={
            'idCategoria': 'ID', 
            'nombreCategoria': 'Nombre',

        }
        widgets={
            'idCategoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'ID', 
                    'id': 'idCategoria'
                }
            ), 
            'nombreCategoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre', 
                    'id': 'nombreCategoria'
                }
            )

        }


