from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebPageForm(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'



class AcessRecordForm(forms.ModelForm):
    class Meta:
        model=AcessRecord
        fields='__all__'