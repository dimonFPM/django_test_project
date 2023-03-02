from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>hello, world!</h1>")


def index_1(request):
    return HttpResponse("<h1>hello, mother fucker</h1>")
