from django import forms
from .models import MyToDoList

#your code
#Add Form
#フォームでは、必ずlabelを指定するようにしましょう。
class todoAddForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    contents = forms.CharField(label="Contents", widget=forms.Textarea)
    #フォームのCharFieldは、デフォルトで「widget=forms.TextInput」となっています。つまり1行分しか入力できません。複数行入力できるようにしたい時は、「widget=forms.Textarea」とします。 またフォームでTextFieldを使わない理由は、単純にTextFieldがフォームで用意されていないからです。
    deadline= forms.DateField(label="Dealline")
