from django.shortcuts import render, redirect
from .forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm


def register(request):
	if request.user.is_authenticated:
		next_ = request.GET.get('next', '')
		if not next_:
			return redirect('/')
		return redirect(f'/{next_}/')

	form = RegisterForm()

	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('login')

	context = {
		'form': form
	}

	return render(request, 'registration/register.html', context)