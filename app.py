import pickle as pk
import streamlit as st

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")

# Load datasets
movie_dataset = pk.load(open('movie_dataset.pkl', 'rb'))
similarity = pk.load(open('similarity.pkl', 'rb'))

# CSS styling
st.markdown("""
    <style>
        .header {
            font-size: 2.5em;
            color: #FF6347;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .selectbox-label {
            font-size: 1.2em;
            font-weight: bold;
            color: #4682B4;
            margin-top: 20px;
        }
        .recommend-button {
            background-color: #4CAF50;
            color: white;
            font-size: 1em;
            padding: 10px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }
        .recommend-button:hover {
            background-color: #45a049;
        }
        .recommendations {
            font-size: 1.1em;
            color: #2E8B57;
            margin-top: 20px;
        }
        .footer {
            font-size: 0.8em;
            color: #888;
            text-align: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Movie Recommendation System</div>', unsafe_allow_html=True)

def recommend_movie(movie_name):
    movie_index = movie_dataset[movie_dataset['title'] == movie_name].index[0]
    similar_movies = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda vector: vector[1])
    recommendations = []
    for i in similar_movies[1:6]:
        recommendations.append(movie_dataset.iloc[i[0]].title + ' with similarity of ' + str(round(i[1]*100, 2)))
    return recommendations

# Select movie
st.markdown('<div class="selectbox-label">Select Movie/TV Show</div>', unsafe_allow_html=True)
selected_movie = st.selectbox('', movie_dataset['title'])

# Recommend button
if st.button('Recommend', key='recommend_button'):
    result = recommend_movie(selected_movie)
    st.markdown('<div class="recommendations">', unsafe_allow_html=True)
    for recommendation in result:
        st.text(recommendation)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Movie Recommendation System</div>', unsafe_allow_html=True)
