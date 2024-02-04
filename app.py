import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Recommender System ", page_icon='cinema.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
# movies_list = movies_list['title'].values

st.title('Movie Recommender by Dewansh')

selected_movie_name = st.selectbox(
    'Search for movie',
    movies['title'].values
)

if st.button('Recommend'):
    results = recommend(selected_movie_name)
    for i in results:
        st.write(i)
