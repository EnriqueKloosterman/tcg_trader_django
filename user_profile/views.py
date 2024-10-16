from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from card.models import Card, Card_Type, Faction

# Create your views here.
@login_required
def user_profile(request):
    cards = Card.objects.filter(created_by=request.user)
    card_types = Card_Type.objects.all()
    factions = Faction.objects.all()
    return render(request, 'user_profile/profile.html', {
        'cards': cards,
        'factions': factions,
        'card_types': card_types
    })
