from django.shortcuts import render

def poem_test_view(request):
    return render(request, 'main/poem_test.html')