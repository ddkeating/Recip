from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Recipe(models.Model):
    ASIAN = 'asian'
    AMERICAN = 'american'
    MEXICAN = 'mexican'
    ITALIAN = 'italian'
    FRENCH = 'french'
    EGYPTIAN = 'egyptian'
    MORROCAN = 'morrocan'
    INDIAN = 'indian'
    CHINESE = 'chinese'
    JAPANESE = 'japanese'
    OTHER = 'other'

    CATEGORY_CHOICES = [
        (ASIAN, 'asian'),
        (AMERICAN, 'american'),
        (MEXICAN, 'mexican'),
        (ITALIAN, 'italian'),
        (FRENCH, 'french'),
        (EGYPTIAN, 'egyptian'),
        (MORROCAN, 'morrocan'),
        (INDIAN, 'indian'),
        (CHINESE, 'chinese'),
        (JAPANESE, 'japanese'),
        (OTHER, 'other')
    ]

    title = models.CharField(max_length=100, default='Enter the name of your dish...')
    
    description = models.TextField() 

    image = models.ImageField(upload_to='recipe_images', default='recipe_images/default.jpg')

    ingredients = RichTextField(default='Write your ingredients here...')

    instructions = RichTextField(default='Write your instructions here...')

    category = models.CharField(max_length=30, default=OTHER, choices=CATEGORY_CHOICES)

    total_cook_time = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recipes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})
    