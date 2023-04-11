from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.template import loader
from .models import Question, Choice, Querys
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .gpt35 import answer
from .translate import get_translate
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .webpush import episode_webpush
from webpush import send_user_notification

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



def createform(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = QueryDict('', mutable=True)
        form.update(request.POST)
        form['query'] = get_translate(answer(get_translate(form["name"], True)), False)
        send_mail(
            form["name"],
            form['query'],
            "django2633@gmail.com",
            ["secrett2633@kakao.com"],
            fail_silently=False,
        )
        payload = {"head": form["name"], "body": form['query']}
        user = request.user #secrett
        send_user_notification(user=user, payload=payload, ttl=1000)
        
        # query = Querys()
        # query.studentID = request.POST.get('studentID')
        # query.name = request.POST.get('name')
        # query.query = "test"
        # query.save()
    return render(request, "polls/index.html", {"form": form["query"]})


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


