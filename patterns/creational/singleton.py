"""
Singleton Pattern:

Ensures a class has only one shared instance and provides a global access point to it.

Common uses: application configuration, logging, caching, connection pools, or any shared resource where multiple instances
could cause inconsistent state or wasted resources.
"""

from datetime import datetime


class EventLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._logs = []
        return cls._instance

    def log_event(self, event: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self._logs.append(f"{timestamp}: {event}")

    def get_logs(self) -> list[str]:
        return list(self._logs)


if __name__ == "__main__":
    
    logger1 = EventLogger()
    logger1.log_event("Application started")
    logger1.log_event("Creating product event")

    logger2 = EventLogger()
    logger2.log_event("Update product event")

    logger3 = EventLogger()
    for log in logger3.get_logs():
        print(log)
