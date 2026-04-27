from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

bot_personas = {
    "bot_A": "I believe AI and crypto will solve all human problems...",
    "bot_B": "I believe late-stage capitalism and tech monopolies...",
    "bot_C": "I strictly care about markets, interest rates..."
}

persona_embeddings = {
    bot: model.encode(text) for bot, text in bot_personas.items()
}

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def route_post_to_bots(post_content, threshold=0.5):
    post_embedding = model.encode(post_content)
    matched_bots = []

    for bot, emb in persona_embeddings.items():
        sim = cosine_similarity(post_embedding, emb)
        if sim > threshold:
            matched_bots.append((bot, sim))

    return matched_bots


# Test
if __name__ == "__main__":
    post = "OpenAI released a new AI model"
    print(route_post_to_bots(post))
