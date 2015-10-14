from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext, loader
from django.views import generic
from .models import Product,Ingredient
from django.core.urlresolvers import reverse
# Create your views here.

# def index(request):
# 	latest_product_list = Product.objects.order_by('-pdate')[:5]
# 	context = {'latest_product_list': latest_product_list}
# 	return render(request, 'products/index.html', context)
	# template = loader.get_template('products/index.html')
	# context = RequestContext(request, {
	# 	'latest_product_list': latest_product_list
	# 	})
	# return HttpResponse(template.render(context))

# def detail(request, product_id):
# 	product = get_object_or_404(Product, pk=product_id)
# 	return render(request, 'products/detail.html',{'product': product}) 
	# try:
	# 	product = Product.objects.get(pk=product_id)
	# except Product.DoesNotExist:
	# 	raise Http404("product does not exist")
	# return render(request, 'products/detail.html',{'product': product})

def ingredient_get(request, product_id):
	response = "You're looking at ingredients of product %s."
	return HttpResponse(response % product_id)

def ingredient_pick(request, product_id):
	p = get_object_or_404(Product, pk=product_id)
	try:
		selected_ingredient = p.ingredient_set.get(pk=request.POST['ingredient'])
	except (KeyError, Ingredient.DoesNotExist):
		return render(request, 'products/detail.html',{
			'question' :p,
			'error_message': "You didn't select a ingredient."
			})
	else:
		selected_ingredient.save()
		return HttpResponseRedirect( reverse('products:results',args=(p.id,)))

# def results(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'products/results.html', {'product': product})

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-pdate')[:5]


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'


class ResultsView(generic.DetailView):
    model = Product
    template_name = 'products/results.html'

