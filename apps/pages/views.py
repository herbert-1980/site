from django.shortcuts import render
#from django.contrib import messages

# Create your views here.
def index(request):
    """messages.debug(request, 'Esta é uma mensagem de Debug!')
    messages.info(request, 'Esta é uma mensagem de info!')
    messages.success(request, 'Esta é uma mensagem de sucesso!')
    messages.warning(request, 'Esta é uma mensagem de warning!')
    messages.error(request, 'Esta é uma mensagem de error!')"""
    
    return render(request, 'index.html')