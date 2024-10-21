from django.shortcuts import render, render, get_object_or_404, redirect
from card.models import Card
from .models import Conversation, Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def new_conversation(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    
    if card.created_by == request.user:
        return redirect('user_profile:profile')
    
    conversations = Conversation.objects.filter(card=card).filter(members__in=[request.user.id])
    
    if conversations.exists():
        conversation = conversations.first()
        return redirect('conversation:detail', pk=conversation.id)
        pass

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(card=card)
            conversation.members.add(request.user)
            conversation.members.add(card.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('card:detail', pk=card.id)
    else:
        form = MessageForm()
    return render(request, 'conversation/new.html', {
        'form': form
    })
    
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members=request.user)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = MessageForm()


    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })

