from django.forms import ModelForm
from myapp2.models import Example


class ExampleForm(ModelForm):
    template_name = 'myapp2/form_template.html'
    class Meta:
        model = Example
        fields=['name','surname','email','text']