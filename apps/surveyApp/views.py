from django.shortcuts import render, HttpResponse, redirect

def index(request):
   
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['first_name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['text'] = request.POST['text']

        return render(request, 'result.html')
    else: 
        return redirect('/')

def goBack(request):
    return redirect('/')

   
