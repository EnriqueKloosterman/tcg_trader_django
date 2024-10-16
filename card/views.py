from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Card_Type, Faction
from django.contrib.auth.decorators import login_required
from .forms import NewCardForm, UpdateCardForm


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

@login_required

def new_card(request):
    if request.method == 'POST':
        form = NewCardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.created_by = request.user
            card.save()
            return redirect('card:detail', pk=card.pk)
    else:
        form = NewCardForm()
    return render(request, 'card/new_card.html', {'form': form})

@login_required
def delete(request, pk):
    card = get_object_or_404(Card, pk=pk, created_by=request.user)
    card.delete()
    return redirect('user_profile:user_profile')

@login_required
def update(request, pk):
    card = get_object_or_404(Card, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = UpdateCardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card:detail', pk=card.pk)
    else:
        form = UpdateCardForm(instance=card)
    return render(request, 'card/new_card.html', {'form': form})
