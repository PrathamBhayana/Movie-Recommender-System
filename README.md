# 🎬Movie-Recommender-System
![image](https://github.com/user-attachments/assets/9426e944-d8d8-4cf2-a236-7ebf3a00dbc0)

This is a content-based movie recommender system built with Python, Pandas, Scikit-learn, and Flask. It suggests similar movies based on the input provided by the user, leveraging movie metadata and cosine similarity.
## 🔧Features
- Recommends top 6 similar movies based on content features.
- Fetches movie posters using TMDB API.
- Simple and intuitive Streamlit-based web interface.
## 🚀How to Run
- Clone this repository
```
git clone https://github.com/PrathamBhayana/Movie-Recommender-System.git
cd Movie-Recommender-System
```
- Install the required packages:
```
pip install -r requirements.txt
```
- Download similarity.pkl:
> Note: The similarity.pkl file exceeds GitHub’s 100MB file limit, so it is not included in this repository.
Run the provided Jupyter Notebook (Movie_Recommender_System.ipynb) to generate and save the similarity.pkl file in your local environment.
- Run the Flask app:
```
python app.py
```
- Enjoy exploring movie recommendations! 🎥
## 📁Files and Structure
├── app.py # Main Flask application

├── Movie_Recommender_System.ipynb # Jupyter Notebook to preprocess and generate similarity matrix

├── movie_list.pkl # Contains movie metadata used for suggestions

├── similarity.pkl # Cosine similarity matrix (must be generated or downloaded separately)

├── requirements.txt # List of required Python packages

├── static/ # Static assets (CSS,images)

├── templates/ # HTML templates (index.html)
