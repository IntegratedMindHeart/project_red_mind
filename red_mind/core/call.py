import requests
import bs4 as bs

KEY='ff5d4bbd48363bb3f65e4c34e204d94b'

def get_movie_cast(api_key,movie_id):
    try:
        casts=[]
        r=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}')
        for i in r.json()['cast'][:11]:
            cast={}
            if i['profile_path']:
                cast['cast_id']=i['id']
                cast['original_name']=i['original_name']
                cast['character']=i['character']
                cast['image']='https://image.tmdb.org/t/p/original'+i['profile_path']
            else:
                continue
            casts.append(cast)
        return casts
    except:
        return

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
        casts=get_movie_cast(KEY,movie_id)
        
        genre_list=[]
        for genre in genres:
            genre_list.append(genre['name'])

        context['movie_id']=movie_id
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
        context['casts']=casts
    
    except:
        context['sorry']='movie not found'

    return context

def get_similar_movies(movie_title,movie_id,api_key):
    try:
        r=requests.get(f'http://127.0.0.1:5000/api/recommendation/{movie_title}')
        return r.json()
    except:
        r=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={api_key}&language=en-US&page=1')
        results=r.json()['results']
        similar_movies=[]
        for result in results:
            similar_movies.append(result['title'])
        return {'similar_movies':similar_movies}
         
def get_movie_posters(api_key,similar_movies):
    posters=[]
    try:
        for movie in similar_movies:
            r=requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie}')
            poster_path=r.json()['results'][0]['poster_path']
            posters.append((movie,f'https://image.tmdb.org/t/p/original{poster_path}'))
        return {'movie_posters':posters}
    except:
        pass

def get_individual_cast(api_key,cast_id):
    try:
        details={}
        r=requests.get(f'https://api.themoviedb.org/3/person/{cast_id}?api_key={api_key}')
        cast=r.json()
        details['biography']=cast['biography']
        details['birthday']=cast['birthday']
        details['deathday']=cast['deathday']
        details['profession']=cast['known_for_department']
        details['name']=cast['name']
        details['place_of_birth']=cast['place_of_birth']
        details['profile_path']='https://image.tmdb.org/t/p/original'+cast['profile_path']
        return details
    except:
        return {'sorry':'details not found'}

def get_sentiment(review):
    r=requests.get(f'http://127.0.0.1:5000/api/review/{review}')
    return r.json()['result']

def get_reviews(imdb_id):
    sauce=requests.get('https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt'.format(imdb_id)).text
    soup=bs.BeautifulSoup(sauce,"html.parser")
    soup_result=soup.find_all("div",{"class":"text show-more__control"})
    reviews=[]
    for review in soup_result:
        if review.string:
            temp={}
            try:
                temp['pred']=get_sentiment(review.string)
                temp['review']=review.string
            except:
                continue
            reviews.append(temp)
    return reviews