# Compte rendu - Exo shell Django (2.2.2)

## Préambule

question 1: Lister tous les objets de type Question : faites une boucle pour afficher les attributs de chaque question sur une ligne différente. Indice : remarquer que Question.objects.all() est un itérable sur lequel vous pouvez boucler avec une simple boucle for

Ouvrir un terminal PowerShell, se placer dans le dossier du projet (tutos) et lancer le shell :
'''**
C:\Users\PeyrousP\OneDrive - Facylities Multi Services\Documents\Python\django\exos\tutos>.\env\Scripts\Activate

(env) C:\Users\PeyrousP\OneDrive - Facylities Multi Services\Documents\Python\django\exos\tutos>python -c "import django; print(django.get_version())"
5.2

(env) C:\Users\PeyrousP\OneDrive - Facylities Multi Services\Documents\Python\django\exos\tutos>python manage.py shell
8 objects imported automatically (use -v 2 for details).

Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Question
>>> for q in Question.objects.all():
...     print(q.id, q.question_text, q.pub_date)
...
1 Quelle est la capitale de la France ? 2026-11-03 12:46:26+00:00
2 quel est la couleur du ciel 2026-11-02 05:00:00+00:00
3 combien font 4 + 5? 2026-11-11 13:46:26+00:00
**
'''


question 2: Ajoutez un filtre sur la date de publication – portant par ex. sur un de ses composants4 suivants : year, month, day – de vos questions et lister un sous-ensemble de vos questions suivant les dates que vous avez saisies à l'exercice précédent.
>>> Question.objects.filter(pub_date__year=2026)
<QuerySet [<Question: Quelle est la capitale de la France ?>, <Question: quel est la couleur du ciel>, <Question: combien font 4 + 5?>]>
>>> Question.objects.filter(pub_date__month=11)
<QuerySet [<Question: Quelle est la capitale de la France ?>, <Question: quel est la couleur du ciel>, <Question: combien font 4 + 5?>]>
>>> Question.objects.filter(pub_date__day=3)
<QuerySet [<Question: Quelle est la capitale de la France ?>]>
>>> Question.objects.filter(pub_date__day=2)
<QuerySet [<Question: quel est la couleur du ciel>]>

question 3: Trouvez la deuxième question (pour laquelle l'attribut de clé primaire id = 2) de votre base de données, puis affichez les valeurs de tous ses attributs et tous les choix associés.
>>> q = Question.objects.get(pk=2)
>>> q.__dict__
{'_state': <django.db.models.base.ModelState object at 0x000001596B54F950>, 'id': 2, 'question_text': 'quel est la couleur du ciel', 'pub_date': datetime.datetime(2026, 11, 2, 5, 0, tzinfo=datetime.timezone.utc)}
>>> q.choice_set.all()
<QuerySet [<Choice: gris>, <Choice: bleu>]>

question 4: Faites une boucle pour afficher les attributs de chaque question et leurs choix associés.
>>> for q in Question.objects.all():
...     print(q.id, q.question_text, q.pub_date)
...     for c in q.choice_set.all():
...             print("  ", c.id, c.choice_text, c.votes)
...     print()
...
1 Quelle est la capitale de la France ? 2026-11-03 12:46:26+00:00
   1 pau 0
   6 paris 0

2 quel est la couleur du ciel 2026-11-02 05:00:00+00:00
   2 gris 0
   4 bleu 0

3 combien font 4 + 5? 2026-11-11 13:46:26+00:00
   3 45 0
   5 9 0


question 5: Affichez le nombre de choix enregistrés pour chaque question.
>>> for q in Question.objects.all():
...     print(q.id, q.question_text, "→", q.choice_set.count(), "choix")
...
1 Quelle est la capitale de la France ? → 2 choix
2 quel est la couleur du ciel → 2 choix
3 combien font 4 + 5? → 2 choix

question 7: Triez les questions par ordre antéchronologique.
>>> for q in Question.objects.order_by("-pub_date"):
...     print(q.id, q.question_text, q.pub_date)
...
3 combien font 4 + 5? 2026-11-11 13:46:26+00:00
1 Quelle est la capitale de la France ? 2026-11-03 12:46:26+00:00
2 quel est la couleur du ciel 2026-11-02 05:00:00+00:00

question 8: Créez une question en utilisant le shell.
>>> from django.utils import timezone
>>> q = Question.objects.create(question_text="Quel est votre langage préféré ?", pub_date=timezone.now())
>>> q
<Question: Quel est votre langage préféré ?>
>>> q.id
4


question 9: Ajoutez 3 choix à cette question en utilisant le shell.
>>> q.choice_set.create(choice_text="Python", votes=0)
<Choice: Python>
>>> q.choice_set.create(choice_text="JavaScript", votes=0)
<Choice: JavaScript>
>>> q.choice_set.create(choice_text="Java", votes=0)
<Choice: Java>

question 11: Listez les questions publiées récemment.
>>> for q in Question.objects.all():
...     if q.was_published_recently():
...             print(q.id, q.question_text, q.pub_date)
...
1 Quelle est la capitale de la France ? 2026-11-03 12:46:26+00:00
3 combien font 4 + 5? 2026-11-11 13:46:26+00:00
4 Quel est votre langage préféré ? 2026-11-04 09:59:45.780259+00:00

