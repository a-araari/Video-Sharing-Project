from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm


def product_list(request):
	context = {}
	q = request.GET.get('q', (''))
	if q != '':
		search_products = Product.objects.filter(title__contains=q, description__contains=q)
		context['product_list'] = search_products
		context['search'] = q
	else:
		context['product_list'] = Product.objects.all().order_by('-created_date')

	return render(request, 'products/product_list.html', context)



class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product


@login_required
def add(request):
	form = ProductForm
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid:
			product = form.save(commit=False)
			product.username = request.user.username
			product.save()
			return redirect('product_list')
	return render(request, 'products/add.html', {'form': form})


@login_required
def update(request, pk):
	product = Product.objects.get(id=pk)
	product_dict = model_to_dict(product)

	if product.username == request.user.username:

		if request.method == 'POST':
			form = ProductForm(request.POST)
			if form.is_valid:
				product.title = form['title'].value()
				product.description = form['description'].value()
				product.tuto_url = form['tuto_url'].value()

				product.save()
				return redirect('product_list')
			else:
				form = ProductForm(product_dict)
		else:
			form = ProductForm(product_dict)
	else:
		raise Http404
	
	return render(request, 'products/add.html', {'form': form})


@login_required
def delete(request, pk):
	product = Product.objects.get(id=pk)

	if product.username == request.user.username:
		product.delete()
	else:
		raise Http404
	
	return redirect('product_list')