
import json
from tools import mock_searxng_search

def decide_topic(persona):
    if "finance" in persona.lower():
        return "stock market trends"
    return "AI advancements"

def web_search(topic):
    return mock_searxng_search(topic)

def generate_post(bot_id, persona):

    # Node 1
    topic = decide_topic(persona)

    # Node 2
    results = web_search(topic)

    # Node 3
    post = f"{persona} reacting strongly to: {results[0]}"

    return {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post[:280]
    }


if __name__ == "__main__":
    print(json.dumps(generate_post("bot_A", "AI maximalist"), indent=2))
