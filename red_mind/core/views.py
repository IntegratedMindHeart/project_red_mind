from django.shortcuts import redirect, render
from django.views import View
from .models import MovieRecord
from .forms import MovieRecordForm
from .call import KEY,get_details,get_similar_movies,get_reviews,get_movie_posters,get_individual_cast

# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        fm=MovieRecordForm()
        context={
            'home_active':'active',
            'home_disabled':'disabled',
            'form':fm
        }
        return render(request,'core/home.html',context)

    def post(self,request,*args,**kwargs):
        fm=MovieRecordForm(request.POST)
        title=''
        if fm.is_valid():
            title=fm.cleaned_data['movie_name'].lower()
            rec=MovieRecord(movie_name=title)
            rec.save()
        fm=MovieRecordForm()
        context=get_details(KEY,title)
        if 'movie_id' in context.keys():
            context.update(get_similar_movies(title,context['movie_id'],KEY))
        if 'imdb_id' in context.keys():
            context['reviews']=get_reviews(context['imdb_id'])
        if 'similar_movies' in context.keys():
            context.update(get_movie_posters(KEY,context['similar_movies']))
        context['home_active']='active'
        context['home_disabled']='disabled'
        context['form']=fm
        return render(request,'core/home.html',context)

class CastView(View):
    def get(self,request,*args,**kwargs):
        context=get_individual_cast(KEY,kwargs['cast_id'])
        if not context:
            return redirect('home')
        context['cast_active']='active'
        context['cast_disabled']='disabled'
        return render(request,'core/cast.html',context)

class AboutView(View):
    def get(self,request,*args,**kwargs):
        context={
            'about_active':'active',
            'about_disabled':'disabled'
        }
        return render(request,'core/about.html',context)