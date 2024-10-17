from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Card_Type(models.Model):
    type_name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['type_name'] # ordena las categorias por nombre
        verbose_name_plural = 'Type'
    
    def __str__(self):
        return self.type_name
    
class Faction(models.Model):
    faction_name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['faction_name'] 
        verbose_name_plural = 'Faction'

    def __str__(self):
        return self.faction_name
    
class Card(models.Model):
    card_name = models.CharField(max_length=100)
    card_type = models.ForeignKey(Card_Type, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    card_text = models.TextField()
    card_cost = models.IntegerField()
    card_power = models.IntegerField()
    card_defense = models.IntegerField()
    card_image = CloudinaryField('image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.card_name