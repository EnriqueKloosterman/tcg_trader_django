from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Card_Type, Faction
from django.contrib.auth.decorators import login_required


# Create your views here.
def detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    related_items = Card.objects.filter(card_type=card.card_type, faction=card.faction, is_active=True).exclude(pk=pk)
    
    return render(request,'card/detail.html',{
        'card': card,
        'related_items': related_items
    })


@login_required
def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})