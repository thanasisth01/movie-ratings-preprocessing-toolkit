# 🎬 Movie Ratings Preprocessing & Similarity Calculation

This project consists of three Python scripts that perform **data filtering**, **ratings normalization**, and **movie similarity calculation** based on user ratings. It processes a movie ratings dataset to prepare it for further analysis or recommendation tasks.

---

## 📁 Project Structure

/prefiltering.py ← Filters movies/users based on number of ratings
/new_ratings.py ← Normalizes ratings and splits into training/testing sets
/pearson.py ← Calculates Pearson similarity between movies
/output/ ← Contains the generated CSVs from each step
README.md ← This file

---

## 1️⃣ `prefiltering.py`

**Purpose:**  
Filters the dataset to keep only:
- Movies with **at least 5 ratings**
- Users who have given **5 or more ratings**

**What it does:**
- Reads the raw ratings file (CSV format)
- Filters out low-interaction movies and users
- Saves a new filtered CSV file containing:
  - Only movies with ≥ 5 ratings
  - Only users with ≥ 5 ratings
- Outputs:
  - 610 users (each with ≥ 5 ratings)
  - 3650 movies (out of original 9724)

**Output file:**  
`filtered_ratings.csv` (used as input for the next script)

---

## 2️⃣ `new_ratings.py`

**Purpose:**  
Normalizes each user's ratings by subtracting their **average rating** from each of their given ratings. Also splits the dataset into **training and testing** sets.

**What it does:**
- Loads the `filtered_ratings.csv` file
- Computes the average rating for each user
- Subtracts the average rating from each user’s individual ratings
- Splits data into:
  - Training set
  - Testing set
- Saves a new file with normalized ratings containing:
  - `userId`, `movieId`, `new_rating`

**Output file:**  
`normalized_ratings.csv`

---

## 3️⃣ `pearson.py`

**Purpose:**  
Calculates **Pearson correlation similarity** between every pair of movies.

**What it does:**
- Computes similarity between every unique pair of movies using user ratings
- Avoids redundant computations (A vs. B is the same as B vs. A)
- Due to the high computational cost, the final output file is not included, but the script is prepared to generate it

**Note:**  
Running this script on a large dataset may take a significant amount of time due to the number of pairwise comparisons.

---

## 🛠 Technologies Used

- Python 3
- `pandas` for data handling
- `numpy` for mathematical operations
