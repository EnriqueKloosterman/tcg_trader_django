from django.shortcuts import render, redirect
from card.models import Card, Card_Type, Faction
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm


# Create your views here.
def base(request):
    return render(request, 'core/base.html')

def home(request):
    cards = Card.objects.filter(is_active=True).order_by('?')[0:5]
    # cards = Card.objects.filter(is_active=True).order_by('-created_at')[0:5]
    card_types = Card_Type.objects.all()
    factions = Faction.objects.all()
    
    return render(request, 'core/index.html', {
        'cards': cards,
        'card_types': card_types,
        'factions': factions
    })
    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })    