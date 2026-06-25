from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = {
    "What is Artificial Intelligence?":
    "Artificial Intelligence is the simulation of human intelligence by machines.",

    "What is Machine Learning?":
    "Machine Learning is a subset of AI that learns patterns from data.",

    "What is Deep Learning?":
    "Deep Learning is a subset of Machine Learning based on neural networks.",

    "What is Python?":
    "Python is a high-level programming language widely used in AI and data science.",

    "What is a neural network?":
    "A neural network is a computational model inspired by the human brain.",

    "What is data science?":
    "Data science is the field of extracting insights and knowledge from data.",

    "What is NLP?":
    "Natural Language Processing enables computers to understand human language.",

    "What is computer vision?":
    "Computer Vision allows computers to interpret and understand images and videos.",

    "What is supervised learning?":
    "Supervised learning trains models using labeled data.",

    "What is unsupervised learning?":
    "Unsupervised learning finds patterns in unlabeled data."
}

questions = list(faqs.keys())

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(questions)

print("FAQ Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:

    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_question])

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_score = similarities.max()

    best_match_index = similarities.argmax()

    if best_score < 0.3:
        print("Bot: Sorry, I don't have an answer for that.\n")
        continue

    best_question = questions[best_match_index]

    answer = faqs[best_question]

    print(f"Bot: {answer}")
    print(f"(Similarity Score: {best_score:.2f})\n")