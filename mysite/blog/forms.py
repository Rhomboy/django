from django import forms
from .models import Comment
class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields ="__all__"
        exclude = ["post"]
        labels = {"writer": "Your Name",
                  "content": "Your Comment"}
        
        

