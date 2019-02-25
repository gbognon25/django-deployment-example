from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic = {'text': 'Drogba is the best', 'num': 11}
    return render(request, 'basic_app/index.html', context_dic)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relatives.html')
