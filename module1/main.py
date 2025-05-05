import re
import json
from enum import Enum
from datetime import datetime


class Restaurant(Enum):
    MCDONALDS = "McDonald's"
    BURGER_KING = "Burger King"
    KFC = "KFC"
    SUBWAY = "Subway"
    STARBUCKS = "Starbucks"


class Event:
    def __init__(self, event_id, title, restaurant_name, date, time, duration, ticket_price):
        self.id = self.validate_int(event_id, "ID")
        self.title = self.validate_title(title)
        self.restaurant_name = self.validate_enum(restaurant_name)
        self.date = self.validate_date(date)
        self.time = self.validate_time(time)
        self.duration = self.validate_float(duration, "Duration")
        self.ticket_price = self.validate_float(ticket_price, "Ticket Price")

    @staticmethod
    def validate_int(value, field_name):
        if not str(value).isdigit():
            raise ValueError(f"{field_name} must be a number.")
        return int(value)

    @staticmethod
    def validate_float(value, field_name):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"{field_name} must be a valid number.")

    @staticmethod
    def validate_title(value):
        if not re.match(r"^[A-Za-z\s]+$", value):
            raise ValueError("Title must contain only letters and spaces.")
        return value

    @staticmethod
    def validate_enum(value):
        try:
            return Restaurant(value)
        except ValueError:
            raise ValueError(f"Invalid restaurant name. Choose from: {[e.value for e in Restaurant]}")

    @staticmethod
    def validate_date(value):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    @staticmethod
    def validate_time(value):
        try:
            return datetime.strptime(value, "%H:%M").time()
        except ValueError:
            raise ValueError("Time must be in HH:MM format.")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "restaurant_name": self.restaurant_name.value,
            "date": str(self.date),
            "time": self.time.strftime("%H:%M"),
            "duration": self.duration,
            "ticket_price": self.ticket_price
        }

    @staticmethod
    def from_dict(data):
        return Event(
            data["id"], data["title"], data["restaurant_name"],
            data["date"], data["time"], data["duration"], data["ticket_price"]
        )

    def __str__(self):
        return f"{self.id}: {self.title} at {self.restaurant_name.value} on {self.date} {self.time} - Duration: {self.duration}h, Price: ${self.ticket_price}"

    def __eq__(self, other):
        return isinstance(other, Event) and self.id == other.id


class EventCollection:
    def __init__(self, filename="events.json"):
        self.filename = filename
        self.events = []
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.events = [Event.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.events = []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([e.to_dict() for e in self.events], f, indent=4)

    def add_event(self, event):
        self.events.append(event)
        self.save()

    def delete_event(self, event_id):
        self.events = [e for e in self.events if e.id != event_id]
        self.save()

    def edit_event(self, event_id, **kwargs):
        for i, event in enumerate(self.events):
            if event.id == event_id:
                updated = event.to_dict()
                updated.update(kwargs)
                self.events[i] = Event.from_dict(updated)
                self.save()
                return True
        return False

    def search(self, query):
        results = []
        for event in self.events:
            if query.lower() in str(event).lower():
                results.append(event)
        return results

    def list_events(self):
        return self.events


def main_menu():
    collection = EventCollection()

    while True:
        print("\n--- Event Manager ---")
        print("1. Add Event")
        print("2. List Events")
        print("3. Search Events")
        print("4. Edit Event")
        print("5. Delete Event")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                id = input("ID: ")
                title = input("Title: ")
                rest = input(f"Restaurant ({', '.join([r.value for r in Restaurant])}): ")
                date = input("Date (YYYY-MM-DD): ")
                time = input("Time (HH:MM): ")
                duration = input("Duration (hours): ")
                price = input("Ticket Price: ")

                event = Event(id, title, rest, date, time, duration, price)
                collection.add_event(event)
                print("Event added.")

            elif choice == "2":
                for e in collection.list_events():
                    print(e)

            elif choice == "3":
                query = input("Search query: ")
                results = collection.search(query)
                for r in results:
                    print(r)

            elif choice == "4":
                event_id = int(input("Enter ID to edit: "))
                print("Leave blank to keep original value.")
                title = input("New Title: ") or None
                rest = input("New Restaurant: ") or None
                date = input("New Date: ") or None
                time = input("New Time: ") or None
                duration = input("New Duration: ") or None
                price = input("New Price: ") or None

                kwargs = {k: v for k, v in {
                    "title": title,
                    "restaurant_name": rest,
                    "date": date,
                    "time": time,
                    "duration": duration,
                    "ticket_price": price
                }.items() if v is not None}

                if collection.edit_event(event_id, **kwargs):
                    print("Event updated.")
                else:
                    print("Event not found.")

            elif choice == "5":
                event_id = int(input("Enter ID to delete: "))
                collection.delete_event(event_id)
                print("Event deleted.")

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main_menu()
