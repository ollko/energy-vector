from django import forms

from pagedown.widgets import PagedownWidget
from .models import New

class NewsForm(forms.ModelForm):
    content = forms.CharField(widget = PagedownWidget(show_preview = False))
    publish = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model = New
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]
