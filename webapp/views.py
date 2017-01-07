from django.shortcuts import render

def index(request):
	return render(request, 'webapp/about.html')


def contact(request):
	return render(request, 'webapp/contact.html',{'content':['if you would like to contact me for any collaborations, email me','xyz@abc.com']})
