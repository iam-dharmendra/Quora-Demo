from .models import Post,Answer
from django import forms



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['question', 'description', 'image']
      
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request from kwargs
        super().__init__(*args, **kwargs)
    
    def clean(self):
        
        question = self.cleaned_data.get('question')
        description = self.cleaned_data.get('description')
        
        if not str(question).strip():
            raise forms.ValidationError("Question is required.")
        if not str(description).strip(): 
            raise forms.ValidationError("Description is required.")
        final_data=super().clean()
        
        return final_data


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'image']
        
        
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request from kwargs
        super().__init__(*args, **kwargs)
    
    def clean(self):
        
        answer = self.cleaned_data.get('answer')
        if not str(answer).strip():
            raise forms.ValidationError("Question is required.")
       
        final_data=super().clean()
        
        return final_data    
      
        