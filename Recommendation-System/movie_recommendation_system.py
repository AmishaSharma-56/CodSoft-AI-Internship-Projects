import os
import re
import pandas as pd
from difflib import get_close_matches
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define dataset paths
base_path = r"C:\Users\Welcome\Desktop\My Projects\CodSoft-AI-Internship-Projects\Recommendation-System"
data_folder = os.path.join(base_path, "ml-latest-small")
movies_path = os.path.join(data_folder, "movies.csv")
ratings_path = os.path.join(data_folder, "ratings.csv")

# Load datasets
print("📥 Loading datasets...")
movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

# Preprocess movie data
print("🧹 Preprocessing movie data...")
movies['title'] = movies['title'].fillna('').str.lower().str.strip()
movies['genres'] = movies['genres'].fillna('').str.replace('|', ' ', regex=False).str.lower().str.strip()

# Clean title (remove year info)
movies['title_cleaned'] = movies['title'].str.replace(r"\(\d{4}\)", "", regex=True).str.strip()

# Create combined feature for TF-IDF
movies['combined_features'] = movies['title_cleaned'] + ' ' + movies['genres']

# Aggregate ratings: mean rating & count per movie
rating_summary = ratings.groupby('movieId')['rating'].agg(['mean', 'count']).reset_index()
rating_summary.columns = ['movieId', 'avg_rating', 'num_ratings']

# Merge ratings into movie data
movies = pd.merge(movies, rating_summary, on='movieId', how='left')
movies[['avg_rating', 'num_ratings']] = movies[['avg_rating', 'num_ratings']].fillna(0)

# TF-IDF Vectorization
print("🔧 Vectorizing text features...")
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix)

# Index mapping for cleaned titles (lowercase)
title_map = movies[['title_cleaned']].drop_duplicates().reset_index()
title_index_map = {title: idx for idx, title in enumerate(movies['title_cleaned'])}

# Recommendation function with fuzzy matching
def recommend_movies(title, num_recommendations=5):
    title_input = title.lower().strip()
    title_cleaned_input = re.sub(r"\(\d{4}\)", "", title_input).strip()

    # Fuzzy match title with dataset
    possible_matches = get_close_matches(title_cleaned_input, movies['title_cleaned'].unique(), n=1, cutoff=0.6)

    if not possible_matches:
        print(f"❌ Movie '{title}' not found in the dataset.")
        return

    best_match = possible_matches[0]
    idx_list = movies.index[movies['title_cleaned'] == best_match].tolist()

    if not idx_list:
        print(f"❌ Unable to resolve index for '{best_match}'.")
        return

    # Use the first matched index
    idx = idx_list[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 Top {num_recommendations} recommendations for '{movies.loc[idx, 'title'].title()}':\n")

    count = 0
    for i, score in sim_scores:
        if i == idx:
            continue  # Skip the input movie
        if i >= len(movies):
            continue  # Skip invalid index
        movie_info = movies.iloc[i]
        print(f"✅ {movie_info['title'].title()} ({movie_info['genres']})")
        print(f"   🧠 Similarity Score: {score:.3f} | ⭐ Avg Rating: {movie_info['avg_rating']:.2f} ({int(movie_info['num_ratings'])} ratings)\n")
        count += 1
        if count >= num_recommendations:
            break

# Run the system
if __name__ == "__main__":
    movie_name = input("Enter a movie title ➤ ")
    recommend_movies(movie_name, num_recommendations=5)
