from django.shortcuts import render
from django.views import View
from .forms import ContactForm,ContactEditForm
from .models import Contact
from django.http import JsonResponse
from django.template import loader

class Home(View):
    def get(self,request,*args,**kwargs):
        data = {}
        form = ContactForm()
        data['form'] = form
        data['contacts'] = Contact.objects.order_by('-id')
        return render(request,'home.html',data)
    
class Create_contact(View):
    def post(self,request,*args,**kwargs):
        number = request.POST.get('number',None)
        name = request.POST.get('name',None)
        data = {}
        try:
            Contact.objects.create(name=name,mobile=number)
            data['status'] = True
            template = loader.get_template('contact_list.html')
            contacts = Contact.objects.order_by('-id')
            context = {'contacts':contacts}
            html_response = template.render(context)
            data['template'] = html_response
        except:
            data['status'] = False
        return JsonResponse(data)

class Delete_contact(View):
    def get(self,request,*args,**kwargs):
        data = {}
        try:
            id = kwargs['id']
            obj = Contact.objects.get(id=id)
            obj.delete()
            data['status'] = True
            template = loader.get_template('contact_list.html')
            contacts = Contact.objects.order_by('-id')
            context = {'contacts':contacts}
            html_response = template.render(context)
            data['template'] = html_response
        except:
            data['status'] = False
        return JsonResponse(data)

class Edit_contact(View):
    def get(self,request,*args,**kwargs):
        data = {}
        context = {}
        try:
            id = kwargs['id']
            obj = Contact.objects.get(id=id)
            form = ContactEditForm(instance=obj)
            context['eform'] = form
            context['c_id'] = id
        except Exception as e:
            print("......",e)
            context['eform'] = ContactEditForm()
        template = loader.get_template('editform.html')
        html_res = template.render(context)
        data['template'] = html_res
        return JsonResponse(data)
    
    def post(self,request,*args,**kwargs):
        data = {}
        context={}
        try:
            id = kwargs['id']
            name = request.POST.get('name',None)
            mobile = request.POST.get('number',None)
            Contact.objects.filter(id=id).update(name=name,mobile=mobile)
            template = loader.get_template('contact_list.html')
            contacts = Contact.objects.order_by('-id')
            context = {'contacts':contacts}
            html_response = template.render(context)
            data['template'] = html_response
            data['status'] = True
        except Exception as e:
            print(".....",e)
            data['status'] = False
        return JsonResponse(data)
    
class ViewContact(View):
    def get(self,request,*args,**kwargs):
        data = {}
        context = {}
        try:
            id = kwargs['id']
            obj = Contact.objects.get(id=id)
            context['name'] = obj.name
            context['number'] = obj.mobile
            template = loader.get_template('detail_contact.html')
            html_response = template.render(context)
            data['template'] = html_response
            data['status'] = True
        except Exception as e:
            print("......",e)
            data['status'] = False
        return JsonResponse(data)