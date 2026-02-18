from patterns.creational.singleton import EventLogger


def test_singleton_returns_same_instance():
    a = EventLogger()
    b = EventLogger()
    assert a is b


def test_singleton_shares_state():
    a = EventLogger()
    a.log_event("event-1")

    b = EventLogger()
    logs = b.get_logs()

    assert any("event-1" in line for line in logs)
