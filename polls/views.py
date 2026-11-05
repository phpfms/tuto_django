from django.db.models import F, Count, Sum, Avg, Max
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def all_polls(request):
    all_questions = Question.objects.all()
    return render(request, "polls/all.html", {"all_questions": all_questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def frequency(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choix_stats = question.get_choices()

    return render(request, "polls/frequency.html", {
        "question": question,
        "choix_stats": choix_stats
    })


def statistics(request):
    nb_sondages = Question.objects.count()
    nb_choix = Choice.objects.count()

    total_votes_dict = Choice.objects.aggregate(total=Sum('votes'))
    total_votes = total_votes_dict['total'] or 0

    moyenne_votes = (total_votes / nb_sondages) if nb_sondages > 0 else 0

    derniere_date = Question.objects.aggregate(derniere=Max('pub_date'))['derniere']
    derniere_question = Question.objects.filter(pub_date=derniere_date).first()

    plus_populaire = Question.get_most_popular()
    moins_populaire = Question.get_least_popular()

    return render(request, "polls/statistics.html", {
        "nb_sondages": nb_sondages,
        "nb_choix": nb_choix,
        "total_votes": total_votes,
        "moyenne_votes": moyenne_votes,
        "derniere_question": derniere_question,
        "plus_populaire": plus_populaire,
        "moins_populaire": moins_populaire,
    })