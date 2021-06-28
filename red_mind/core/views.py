from django.shortcuts import redirect, render
from django.views import View
from .call import KEY,get_details,get_similar_movies,get_reviews,get_movie_posters,get_individual_cast

# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
         return render(request,'core/index.html')

    def post(self,request,*args,**kwargs):
        title=request.POST.get('title')
        context=get_details(KEY,title)
        if 'movie_id' in context.keys():
            context.update(get_similar_movies(title,context['movie_id'],KEY))
        if 'imdb_id' in context.keys():
            context['reviews']=get_reviews(context['imdb_id'])
        if 'similar_movies' in context.keys():
            context.update(get_movie_posters(KEY,context['similar_movies']))
        return render(request,'core/index.html',context)

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'core/home.html')

    def post(self,request,*args,**kwargs):
        title=request.POST.get('title')
        context=get_details(KEY,title)
        if 'movie_id' in context.keys():
            context.update(get_similar_movies(title,context['movie_id'],KEY))
        if 'imdb_id' in context.keys():
            context['reviews']=get_reviews(context['imdb_id'])
        if 'similar_movies' in context.keys():
            context.update(get_movie_posters(KEY,context['similar_movies']))
        return render(request,'core/home.html',context)

class CastView(View):
    def get(self,request,*args,**kwargs):
        context=get_individual_cast(KEY,kwargs['cast_id'])
        return render(request,'core/cast.html',context)