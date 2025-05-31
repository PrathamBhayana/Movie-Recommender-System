import pickle
import requests
import pandas as pd
from flask import Flask, render_template, request
import time

app = Flask(__name__)


def fetch_poster(movie_id, retries=6, delay=0.5):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            break  # No poster, don't retry
        except requests.exceptions.RequestException:
            time.sleep(delay)  # Wait before retrying
    return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:  # Get exactly 6 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_list = movies['title'].values
    recommendations = []
    posters = []
    selected_movie = None
    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            recommendations, posters = recommend(selected_movie)
    return render_template(
        'index.html',
        movie_list=movie_list,
        recommendations=list(zip(recommendations, posters)),
        selected_movie=selected_movie
    )

if __name__ == '__main__':
    app.run(debug=True)