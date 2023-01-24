import streamlit as st
import pickle
import pandas as pd
import requests

movie_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)
movie_title = movies['title'].values
movie_similarity = pickle.load(open('movie_similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=93ce05335f335da8287b0dc42c5d7389&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def movie_suggestion(movie_name):
    movie_index = movies[movies['title']==movie_name].index[0]
    distances = movie_similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    suggested_movies = []
    suggested_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        suggested_movie_posters.append(fetch_poster(movie_id))
        suggested_movies.append(movies.iloc[i[0]].title)
        
    
    return suggested_movies, suggested_movie_posters


# website title
st.title('Movie Sugggestion System')
input_movie_title = st.selectbox("Type a movie title to get simillar movie suggestions", movie_title)

if st.button('Suggest'):
    suggested_movies, suggested_movie_posters = movie_suggestion(input_movie_title)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(suggested_movie_posters[0])
        st.text(suggested_movies[0])
    with col2:
        st.image(suggested_movie_posters[1])
        st.text(suggested_movies[1])

    with col3:
        st.image(suggested_movie_posters[2])
        st.text(suggested_movies[2])
    with col4:
        st.image(suggested_movie_posters[3])
        st.text(suggested_movies[3])
    with col5:
        st.image(suggested_movie_posters[4])
        st.text(suggested_movies[4])

st.write('This system is developed by _Syed Shaeduzzaman Noor_ :sunglasses:')