from collections import Counter


events = [
    {"customer_id": "C1", "event": "login"},
    {"customer_id": "C2", "event": "purchase"},
    {"customer_id": "C1", "event": "logout"},
    {"customer_id": "C1", "event": "purchase"},
]

counts = Counter(
    event["customer_id"] for event in events
)

print(dict(counts))