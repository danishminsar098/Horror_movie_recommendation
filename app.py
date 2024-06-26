import pickle
import streamlit as st
import requests
import pandas as pd
import streamlit as st


import streamlit as st
import base64

# Function to get the base64 string of the image
def get_base64_from_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return b64_string

# Function to set the background image and text color
def set_background_and_text(image_path):
    bin_str = get_base64_from_image(image_path)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .stApp, .css-10trblm, .css-16huue1 {{
        color: white;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Specify the path to your horror background image
image_path = "C:\\Users\\DELL\\Downloads\\pumpkin.jpg" # Replace with the actual path to your image

# Set the background and text color
set_background_and_text(image_path)







def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]: 
        # fetch the movie poster
        id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].original_title)

    return recommended_movie_names,recommended_movie_posters



st.header('Horror Movie Recommendation')
movies = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl', 'rb'))


movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Select Movie",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
     # Define a function to display posters in a grid
    def display_posters_in_grid(names, posters, num_cols=5):
        num_recs = len(names)
        rows = (num_recs + num_cols - 1) // num_cols  # Calculate the number of rows required

        for row in range(rows):
            cols = st.columns(num_cols)  
            for col in range(num_cols):
                idx = row * num_cols + col
                if idx < num_recs:
                    with cols[col]:
                        st.image(posters[idx], use_column_width='always')
                        st.text(names[idx])

    # Call the function to display posters
    display_posters_in_grid(recommended_movie_names, recommended_movie_posters)