import joblib
from sentence_transformers import SentenceTransformer

transformer_model = SentenceTransformer("all-MiniLM-L6-v2")

model_classifier = joblib.load("models/log_classifier.joblib")

def classify_with_bert(log_message):

    embeddings = transformer_model.encode(log_message)

    probabilities = model_classifier.predict_proba([embeddings])[0]

    predicted_class = "Unknown"

    if(max(probabilities) > 0.5):
        predicted_class = model_classifier.predict([embeddings])[0]

    return predicted_class

if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey, how are you?",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]

    for log in logs:
        print(log, " ->" ,classify_with_bert(log))
