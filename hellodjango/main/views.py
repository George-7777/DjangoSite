from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table
from .forms import TableForm
# Create your views here.
def text(request):
    return render(request, "main/index.html")
def text2(request):
    table = Table.objects.all()
    return render(request, "main/test.html", {"table": table})
def text3(request):
    error = ""
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tovari")
        else:
            error = "Что вы наделали? Вы допустили ошибку..."
    form = TableForm()
    context = {"form": form, "error": error}
    return render(request, "main/otziv.html", context)
#main это приложение, hellodjango это проект, НО hellodjango это ещё другая папка

