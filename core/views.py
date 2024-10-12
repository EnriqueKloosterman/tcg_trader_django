from django.shortcuts import render, redirect
from card.models import Card, Card_Type, Faction

# Create your views here.
def base(request):
    return render(request, 'core/base.html')

def home(request):
    cards = Card.objects.filter(is_active=True)[0:8]
    card_types = Card_Type.objects.all()
    factions = Faction.objects.all()
    
    return render(request, 'core/index.html', {
        'cards': cards,
        'card_types': card_types,
        'factions': factions
    })