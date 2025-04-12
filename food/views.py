from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy



def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,
    }
    
    return render(request,'food/index.html',context)
    # return HttpResponse(template.render(context,request))
    # return HttpResponse(item_list)



class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'




def item(request):
    return HttpResponse('<h1>This is an item view<h1>')


# def detail(request,item_id):
#     return HttpResponse("This is item no/id: %s" % item_id)
    
    
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item':item,
    }
    
    return render(request,'food/detail.html',context) 
    # return HttpResponse("This is item no/id: %s" % item_id)
    
    
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

    
# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,'food/item-form.html',{'form':form})

class CreateItem(CreateView):
    model = Item;
    # fields = ['item_name','item_desc','item_price','item_image']
    fields = ['Name','Description','Price','Image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')  
    
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
    
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context ={
        'item':item,
        'form':form,
    }
    
    return render(request,'food/item-form.html',context)



class DeleteItem(DeleteView):
    model = Item
    template_name = 'food/item-delete.html'
    success_url = reverse_lazy('food:index')  


# def delete_item(request,id):
#     item = Item.objects.get(id=id)
#     if request.method == "POST":
#         item.delete()
#         return redirect('food:index')
#     # form = ItemForm(request.POST or None, instance=item)
#     # if form.is_valid():
#     #     form.save()
#     context ={
#         'item':item,
#     }
    
#     return render(request,'food/item-delete.html',context)  