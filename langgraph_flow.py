import json
from tools import mock_searxng_search


def decide_topic(persona):
    if "finance" in persona.lower():
        return "stock market trends"
    elif "ai" in persona.lower():
        return "AI advancements"
    else:
        return "technology news"


def web_search(topic):
    return mock_searxng_search(topic)


def draft_post(persona, search_results):
    return f"{persona} strongly reacts: {search_results[0]}"


def generate_post(bot_id, persona):
    # Node 1: Decide topic
    topic = decide_topic(persona)

    # Node 2: Search
    results = web_search(topic)

    # Node 3: Draft post
    post = draft_post(persona, results)

    output = {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post[:280]
    }

    return output


if __name__ == "__main__":
    print(json.dumps(generate_post("bot_A", "AI maximalist"), indent=2))
