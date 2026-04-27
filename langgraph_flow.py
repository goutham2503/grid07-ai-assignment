import json
from tools import mock_searxng_search

def generate_post(bot_id, persona):

    # Node 1: Decide topic
    topic = "AI advancements"

    # Node 2: Search
    results = mock_searxng_search(topic)

    # Node 3: Draft
    post = f"{persona[:50]}... reacting to: {results[0]}"

    output = {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post[:280]
    }

    return json.dumps(output, indent=2)
