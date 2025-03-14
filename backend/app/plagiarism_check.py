from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(vectorizer)
    return similarity_matrix[0, 1]  # Similarity score (0 to 1)
