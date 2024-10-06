import streamlit as st
import pandas as pd
import numpy as np
import pickle
import math
import random
import os

port = os.environ.get('PORT', 8501)  # Default is 8501 for Streamlit
st.set_option('server.port', port)


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)), reverse=True,  key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'How would you like to search?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)