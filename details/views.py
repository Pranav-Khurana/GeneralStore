from django.shortcuts import render
from django.views import generic
from .models import item
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator

# Create your views here.

'''
class list(generic.ListView):
    model = item
    context_object_name = 'item'
    template_name = 'index.html'

    # LIST ALL ITEMS IN SEARCH BAR
    def get_context_data(self, **kwargs):
        context = super(list, self).get_context_data(**kwargs)
        context['Search'] = item.objects.values(
            'name').distinct().order_by('name')
        return context

    # SEARCH BAR RESULTS
    def get_queryset(self):
        queryset = item.objects.all()
        search = self.request.GET.get('name' or None)

        if search:
            queryset = item.objects.filter(name__icontains=search)

        if self.request.is_ajax():
            html = render_to_string(
                template_name="list.html",
                context={"artists": queryset}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)

        return queryset
'''

def list(request):

    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        search = item.objects.filter(name__icontains=url_parameter)
    else:
        search = item.objects.all()

    context['item'] = search
    

    if request.is_ajax():
        html = render_to_string(
            template_name="list.html", 
            context={'item':search}
        )

        data_dict = {"search_result": html}
        

        return JsonResponse(data=data_dict, safe=False)
    
    return render(request, "index.html", context=context)
