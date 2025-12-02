from collections import deque
from typing import List, Dict, Any
from datetime import datetime
import json

class CalculatorHistory:
    def __init__(self, max_size: int = 100):
        self.history = deque(maxlen=max_size)

    def add_entry(self, expression: str, result: float, timestamp: str = None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "expression": expression,
            "result": result
        }
        self.history.append(entry)

    def get_history(self) -> List[Dict[str, Any]]:
        return list(self.history)

    def clear_history(self):
        self.history.clear()

    def get_last_entry(self) -> Dict[str, Any] or None:
        return self.history[-1] if self.history else None

    def __len__(self):
        return len(self.history)

    def __str__(self):
        return json.dumps(list(self.history), indent=2)
