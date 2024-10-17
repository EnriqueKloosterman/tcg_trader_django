from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Card_Type, Faction
from django.contrib.auth.decorators import login_required
from .forms import NewCardForm, UpdateCardForm
from django.db.models import Q


# Create your views here.
def detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    related_items = Card.objects.filter(card_type=card.card_type, faction=card.faction, is_active=True).exclude(pk=pk)
    
    return render(request,'card/detail.html',{
        'card': card,
        'related_items': related_items
    })



from django.shortcuts import render
from django.db.models import Q
from .models import Card, Faction, Card_Type

def card_list(request):
    query = request.GET.get('query', '')
    faction_ids = request.GET.getlist('faction')  
    card_type_ids = request.GET.getlist('card_type')  

    factions = Faction.objects.all()
    card_types = Card_Type.objects.all()
    

    cards = Card.objects.filter(is_active=True).order_by('card_name')

    if faction_ids:
        cards = cards.filter(faction_id__in=faction_ids)

    if card_type_ids:
        cards = cards.filter(card_type_id__in=card_type_ids)

    if query:
        cards = cards.filter(
            Q(card_name__icontains=query) | 
            Q(card_text__icontains=query)
        )

    return render(request, 'card/list.html', {
        'cards': cards,
        'factions': factions,
        'card_types': card_types,
        'selected_factions': [int(f) for f in faction_ids],
        'selected_card_types': [int(ct) for ct in card_type_ids],
        'query': query
    })


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
