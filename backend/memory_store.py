

# chatbot/backend/memory_store.py
class InMemoryStore:
    def __init__(self):
        self.sessions = {}

    def add_message(self, session_id, role, content):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append({"role": role, "content": content})

    def get_history(self, session_id):
        return self.sessions.get(session_id, [])

session_store = InMemoryStore()
