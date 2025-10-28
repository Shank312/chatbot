

# chatbot/backend/rag_agent.py

def _stream_tokens(session_id, query):
    """Generator version: yields partial tokens (mock example)."""
    for token in ["Thinking...", "Analyzing...", f"Done processing '{query}'"]:
        yield token


def generate_response(session_id, query, stream=False):
    """
    - stream=False → returns a full string response.
    - stream=True  → returns a generator that yields tokens progressively.
    """
    if stream:
        return _stream_tokens(session_id, query)
    else:
        # Simple mock non-stream reply
        return f"Bot: I received your query '{query}'. (mock reply)"
