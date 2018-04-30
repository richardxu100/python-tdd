from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home_page(request):
#     return render(request, 'home.html', {
#         'new_item_text': request.POST.get('item_text', ''), # supplies a default value, incase nothing provided
#     })
    

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
