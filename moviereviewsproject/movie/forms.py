from .models import Review
from django.forms import ModelForm, Textarea

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchagain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Review
        fields = ['text', 'watchagain']
        labels = {'text': 'Review', 'watchagain': 'Watch Again'}
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 4}),
        }