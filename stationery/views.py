from django.shortcuts import render

def main(request):
    return  render(request, 'main.html')

def stationery(request):
    return render(request, 'shop.html')

def info(request):
    return render(request, 'Artyom_Kisel.html')