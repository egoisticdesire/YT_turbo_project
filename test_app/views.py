from django.shortcuts import render

from test_app.models import Rubric


def test(request):
    return render(request, "test_app/test.html", {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass
