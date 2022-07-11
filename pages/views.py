from django.shortcuts import render, HttpResponse



def homePageView(request):
	return render(request, 'index.html')

# about page


def aboutPageView(request):
	return render(request, 'about.html')