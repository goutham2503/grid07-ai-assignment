from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Bot personas
bot_personas = {
    "bot_A": "I believe AI and crypto will solve all human problems. I love Elon Musk and space.",
    "bot_B": "I think tech monopolies are dangerous. I value privacy, nature, and criticize AI.",
    "bot_C": "I care only about markets, trading, ROI, and finance."
}

# Prepare data
texts = list(bot_personas.values())
metadatas = [{"bot_id": k} for k in bot_personas.keys()]

# Create FAISS vector store
vectorstore = FAISS.from_texts(texts, embedding_model, metadatas=metadatas)


def route_post_to_bots(post_content, threshold=0.5):
    results = vectorstore.similarity_search_with_score(post_content)

    matched = []
    for doc, score in results:
        # Convert FAISS distance → similarity
        similarity = 1 / (1 + score)

        if similarity > threshold:
            matched.append({
                "bot_id": doc.metadata["bot_id"],
                "similarity": round(similarity, 3)
            })

    return matched


if __name__ == "__main__":
    post = "OpenAI released a new AI model that may replace developers"
    print("Input:", post)
    print("Matched Bots:", route_post_to_bots(post))
