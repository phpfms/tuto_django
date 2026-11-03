from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    # 1. Affiche plusieurs colonnes dans la liste
    list_display = ["question_text", "pub_date"]
    # 2. Ajoute le panneau de filtres à droite
    list_filter = ["pub_date"]
    # 3. Trie par date (le '-' signifie du plus récent au plus ancien)
    ordering = ["-pub_date"]
    # 4. Ajoute une barre de recherche
    search_fields = ["question_text"]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "votes", "question"]
    list_filter = ["votes", "question"]
    ordering = ["-votes"]
    search_fields = ["choice_text"]

# On enregistre les modèles avec leurs classes personnalisées
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)