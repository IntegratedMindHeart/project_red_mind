from django.shortcuts import redirect, render
from django.views import View
import requests

# Create your views here.

KEY='ff5d4bbd48363bb3f65e4c34e204d94b'

def get_details(api_key,title):
    context={}
    try:
        r1=requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}')
        movie_details=r1.json()['results'][0]
        movie_id=movie_details['id']
        movie_title=movie_details['original_title']

        r2=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
        movie_details=r2.json()

        tagline=movie_details['tagline']
        imdb_id=movie_details['imdb_id']
        poster='https://image.tmdb.org/t/p/original'+movie_details['poster_path']
        overview=movie_details['overview']
        genres=movie_details['genres']
        rating=movie_details['vote_average']
        vote_count=movie_details['vote_count']
        release_date=movie_details['release_date']
        runtime=movie_details['runtime']
        status=movie_details['status']
        
        genre_list=[]
        for genre in genres:
            genre_list.append(genre['name'])

        context['movie_title']=movie_title
        context['tagline']=tagline
        context['imdb_id']=imdb_id
        context['poster']=poster
        context['overview']=overview
        context['genres']=genres
        context['rating']=rating
        context['vote_count']=vote_count
        context['release_date']=release_date
        context['runtime']=runtime
        context['status']=status
        context['genre_list']=genre_list
    
    except:
        context['sorry']='movie not found'

    return context

def get_similar_movies(movie_title):
    r=requests.get(f'https://hollywoodrcom.herokuapp.com/api/{movie_title}')
    return r.json()

class HomeView(View):
    def get(self,request,*args,**kwargs):
         return render(request,'core/index.html')

    def post(self,request,*args,**kwargs):
        title=request.POST.get('title')
        context=get_details(KEY,title)
        context.update(get_similar_movies(title))
        return render(request,'core/index.html',context)