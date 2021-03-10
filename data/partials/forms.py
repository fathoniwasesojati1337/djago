from django import forms
from ..models import Data
class FormFiled(forms.ModelForm):

    class Meta:
        model = Data
        fields=[
        'nama',
        'nim',
        'alamat',
        'status'
        ]
        widgets = {
        'nama': forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'masukan nama lengkap',
            'id':'nama'
        }
        ),
                'nim': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'masukan nim',
                    'id':'nim'
                }
                ),
                        'alamat': forms.TextInput(
                        attrs={
                            'class':'form-control',
                            'placeholder':'masukan alamat',
                            'id':'alamat'
                        }
                        ),
                                'status': forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'masukan status',
                                    'id':'status'
                                }
                                ),

        }
