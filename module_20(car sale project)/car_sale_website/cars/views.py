from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from . models import CarModel, PurchaseModel
from . forms import CommentForm
from django.contrib import messages
# Create your views here.


class DetailPostView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
        
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comment = self.get_object() 
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comment.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

def purchase_car(request, id):
    if not request.user.is_authenticated:
        return redirect('register')
    
    car = CarModel.objects.get(pk=id)
    if request.method == "POST":
        if car.buy_car():
            messages.success(request, 'Car purchase successful')
            PurchaseModel.objects.create(user=request.user, car=car)
            return redirect('detail_view', id=car.id)  # Redirect to car detail page or any other page
        else:
            messages.warning(request, 'Car is out of stock')
    return redirect('detail_view', id=car.id)  # Redirect back to car detail page if purchase fails


def profile(request):
    if not request.user.is_authenticated:
        return redirect('register')
    purchased_cars = PurchaseModel.objects.filter(user=request.user)
    return render(request, 'profile.html', {'purchased_cars': purchased_cars})


