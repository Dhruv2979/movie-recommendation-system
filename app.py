import streamlit as st
import pickle
import pandas as pd

# load CSS
with open("style.css","r") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def recommend(movie):
    movie_index = Movies[Movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(Movies.iloc[i[0]].title)
    return recommended_movies

Movies_dict = pickle.load(open('Movies_dict.pkl', 'rb'))
Movies = pd.DataFrame(Movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select a Movie',
Movies['title'].values)

if st.button('Recommend'):
    st.subheader(f"Because you liked {selected_movie_name} top 5 movies similarly to {selected_movie_name} are recommended.")
    recommendations = recommend(selected_movie_name)
    for number, movie in enumerate(recommendations, 1):
        st.write(f"{number}. {movie}")