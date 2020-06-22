from django import forms

# 任務追加用フォーム
class ToDoAddForm(forms.Form):
    title = forms.CharField(label="Title",max_length=255)
    contents = forms.CharField(label="内容", widget=forms.Textarea, required=False) # forms包中没有TextFeild
    deadline = forms.DateField(label="締切日")


# 任務削除用フォーム（論理削除）
class ToDoDeleteForm(forms.Form):
    title = forms.CharField(label="Title",max_length=255)
    contents = forms.CharField(label="内容", widget=forms.Textarea, required=False) 
    create_time = forms.DateTimeField(label="作成日")
    deadline = forms.DateField(label="締切日")
    done = forms.BooleanField(label="完成", required=False)

class ToDoEditForm(forms.Form):
    title = forms.CharField(label="Title",max_length=255)
    contents = forms.CharField(label="内容", widget=forms.Textarea, required=False) 
    deadline = forms.DateField(label="締切日")
    done = forms.BooleanField(label="完成", required=False)