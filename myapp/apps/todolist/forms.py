from django import forms

# 任務追加用フォーム
class ToDoAddForm(forms.Form):
    title = forms.CharField(label="Title",max_length=255)
    contents = forms.CharField(label="内容", widget=forms.Textarea) # forms包中没有TextFeild
    deadline = forms.DateField(label="締切日")
