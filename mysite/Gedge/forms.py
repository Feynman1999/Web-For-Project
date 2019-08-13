from django import forms
from .models import UploadImage


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = {'img1'}

        labels = {
            'img1': '',
        }

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        # self.fields['img1'].widget.attrs['style'] = 'position: absolute; top: 20%;     font-size:21px;'
        # self.fields['img1'].widget.attrs['class'] = 'form-control'
