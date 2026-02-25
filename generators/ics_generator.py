import datetime
from pathlib import Path

from icalendar import Alarm, Calendar, Event

from scraper.base import DeprecationEntry


def generate_ics(entries: list[DeprecationEntry]) -> str:
    cal = Calendar()
    cal.add("prodid", "-//ModelDeprecationTracker//EN")
    cal.add("version", "2.0")
    cal.add("x-wr-calname", "Model Deprecations")

    for entry in entries:
        if not entry.has_shutdown_date():
            continue

        event = Event()
        event.add("summary", f"[{entry.provider}] Model deprecation: {entry.model_name}")

        description_parts = [f"Model: {entry.model_name}"]
        if entry.model_id:
            description_parts.append(f"Model ID: {entry.model_id}")
        if entry.replacement:
            description_parts.append(f"Replacement: {entry.replacement}")
        description_parts.append(f"Status: {entry.status}")
        event.add("description", "\n".join(description_parts))

        event.add("dtstart", entry.shutdown_date)
        event.add("dtend", entry.shutdown_date + datetime.timedelta(days=1))

        alarm_7d = Alarm()
        alarm_7d.add("action", "DISPLAY")
        alarm_7d.add("description", f"{entry.model_name} shutdown in 7 days")
        alarm_7d.add("trigger", datetime.timedelta(days=-7))
        event.add_component(alarm_7d)

        alarm_30d = Alarm()
        alarm_30d.add("action", "DISPLAY")
        alarm_30d.add("description", f"{entry.model_name} shutdown in 30 days")
        alarm_30d.add("trigger", datetime.timedelta(days=-30))
        event.add_component(alarm_30d)

        cal.add_component(event)

    return cal.to_ical().decode("utf-8")


def write_ics(entries: list[DeprecationEntry], path: str) -> None:
    ics_content = generate_ics(entries)
    Path(path).write_text(ics_content)
