from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Member

# Create your views here.
#def members(request):
#    template = loader.get_template('members/myfirst.html')
#    return HttpResponse(template.render()) 

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members/all_members.html')
    context = {
                  'mymembers': mymembers
              }
    return HttpResponse(template.render(context, request))           


def details(request, id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template('members/details.html')
    context = {
                'mymember':mymember
    }    
    return HttpResponse(template.render(context, request))
    
def main(request):
    template = loader.get_template('members/main.html')
    return HttpResponse(template.render())    
    
    
def custom_404(request, exception):
    return render(request, 'members/404.html', status=404)

#def testing(request):
    #template = loader.get_template('members/template.html')
    #context = {
            #'fruits': ['Apple', 'Banana', 'Cherry']
    #}    
    #return HttpResponse(template.render(context, request))
    
#def testing(request):
    #mydata = Member.objects.all()
    #template = loader.get_template('members/template.html')
    #context = {
        #'mymembers':mydata
    #}
    #return HttpResponse(template.render(context, request))    
    
def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('members/template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))    