def mock_searxng_search(query: str):
    if "crypto" in query.lower():
        return ["Bitcoin hits new all-time high"]
    elif "ai" in query.lower():
        return ["OpenAI releases GPT-5"]
    else:
        return ["Global markets show mixed signals"]
