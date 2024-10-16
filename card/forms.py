from django import forms
from .models import Card
from django.contrib.auth.forms import UserCreationForm

class NewCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_name', 'card_type', 'faction', 'card_text', 'card_cost', 'card_power', 'card_defense', 'card_image']
        
        widgets = {
            'card_name': forms.TextInput(attrs={'placeholder': 'Card Name', 'class': 'w-full rounded-md'}),
            'card_type': forms.Select(attrs={'class': 'w-full rounded-md'}),
            'faction': forms.Select(attrs={'class': 'w-full rounded-md'}),
            'card_text': forms.Textarea(attrs={'class': 'w-full rounded-md'}),
            'card_cost': forms.NumberInput(attrs={'placeholder': 'Card Cost', 'class': 'w-full rounded-md'}),
            'card_power': forms.NumberInput(attrs={'placeholder': 'Card Power', 'class': 'w-full rounded-md'}),
            'card_defense': forms.NumberInput(attrs={'placeholder': 'Card Defense', 'class': 'w-full rounded-md'}),
            'card_image': forms.FileInput(attrs={'class': 'w-full rounded-md'}),
        }
        
class UpdateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_name', 'card_type', 'faction', 'card_text', 'card_cost', 'card_power', 'card_defense', 'card_image', 'is_active']
        
        widgets = {
            'card_name': forms.TextInput(attrs={'placeholder': 'Card Name', 'class': 'w-full rounded-md'}),
            'card_type': forms.Select(attrs={'class': 'w-full rounded-md'}),
            'faction': forms.Select(attrs={'class': 'w-full rounded-md'}),
            'card_text': forms.Textarea(attrs={'class': 'w-full rounded-md'}),
            'card_cost': forms.NumberInput(attrs={'placeholder': 'Card Cost', 'class': 'w-full rounded-md'}),
            'card_power': forms.NumberInput(attrs={'placeholder': 'Card Power', 'class': 'w-full rounded-md'}),
            'card_defense': forms.NumberInput(attrs={'placeholder': 'Card Defense', 'class': 'w-full rounded-md'}),
            'card_image': forms.FileInput(attrs={'class': 'w-full rounded-md'}),
        }
