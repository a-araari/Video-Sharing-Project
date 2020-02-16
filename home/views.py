from django.shortcuts import render
from products.models import Product

def index(request):
	context = {}
	q = request.GET.get('q', (''))
	if q != '':
		search_products = Product.objects.filter(title__icontains=q)
		context['search_products'] = search_products
		context['search'] = q
	else:
		context['products'] = Product.objects.all()[:6]

	return render(request, 'home/index.html', context)