from django import forms
from gameshop.models import Game

class GameModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'  
    
    def __init__(self, *args, **kwargs):
        super(GameModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'