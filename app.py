import streamlit as st
import pickle
import pandas as pd

# load CSS
with open("style.css","r") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def recommend(movie):
    movie_index = Movies[Movies["title"] == movie].index[0]
    similar_movies = similarity[movie_index]

    recommended_movies = []
    for movie_data in similar_movies:
        movie_index = movie_data[0]
        recommended_movies.append(Movies.iloc[movie_index]["title"])
    return recommended_movies

Movies_dict = pickle.load(open('Movies_dict.pkl', 'rb'))
Movies = pd.DataFrame(Movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.markdown('<h1 class="movie-title">Movie Recommendation System</h1>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
'Select a Movie',
Movies['title'].values)

if st.button('Recommend'):
    st.subheader(f"Because you liked {selected_movie_name}.\n Similarly movies are.")
    recommendations = recommend(selected_movie_name)
    for number, movie in enumerate(recommendations, 1):
        st.write(f"{number}. {movie}")