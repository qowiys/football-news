from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406435982',
        'name': 'Muhammad Qowiy Shabir',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)