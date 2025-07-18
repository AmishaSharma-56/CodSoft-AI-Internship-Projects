# 🎬 Movie Recommendation System

This project is a **content-based movie recommender** built using Python, TF-IDF vectorization, and cosine similarity. It takes a movie title as input and returns a list of similar movies based on title and genre similarity.

---

### ⚙️ Features

- Text preprocessing and cleaning of movie titles and genres  
- Combines title and genre into unified feature vectors  
- Uses **TF-IDF** to represent movie content  
- Computes **cosine similarity** between movies  
- Fuzzy title matching with `difflib.get_close_matches`  
- Outputs movie title, genre, similarity score, and rating summary  

---

### 🧠 Tech Stack

- **Python 3**
- **pandas** for data handling  
- **scikit-learn** for TF-IDF & cosine similarity  
- **difflib** for fuzzy matching  

---

### 💻 How to Run

```bash
python recommend.py
```

Then enter a movie title (e.g. `Toy Story`) and get top 5 similar suggestions with scores.

> Make sure you have the `ml-latest-small` dataset from [MovieLens](https://grouplens.org/datasets/movielens/latest/) placed in the specified `data_folder`.

---

### 🗂️ Folder Structure

```bash
Recommendation-System/
│
├── movie_recommendation_system.py       # Main Python script
└── ml-latest-small/                     # MovieLens dataset folder
    ├── movies.csv
    └── ratings.csv
```

---

This project is a great way to get hands-on experience with **recommender systems**, **NLP**, and **machine learning pipelines** for real-world applications.

---

## 🧾 License

This project is licensed under the MIT License.  
You're welcome to use, modify, and distribute it with proper credit.  
See the [LICENSE](LICENSE) file for full terms.
