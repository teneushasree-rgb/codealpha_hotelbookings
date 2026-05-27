import json
from datetime import datetime

class HotelSystem:

    def __init__(self):

        self.rooms = [
            {"room_no": 101, "type": "Standard", "price": 2000, "available": True},
            {"room_no": 102, "type": "Standard", "price": 2000, "available": True},
            {"room_no": 201, "type": "Deluxe", "price": 4000, "available": True},
            {"room_no": 202, "type": "Deluxe", "price": 4000, "available": True},
            {"room_no": 301, "type": "Suite", "price": 7000, "available": True}
        ]

        self.file = "bookings.json"

        try:
            with open(self.file, "r") as f:
                self.bookings = json.load(f)
        except:
            self.bookings = []

            with open(self.file, "w") as f:
                json.dump(self.bookings, f)

        self.update_room_status()

    # SAVE BOOKINGS
    def save_bookings(self):

        with open(self.file, "w") as f:
            json.dump(self.bookings, f, indent=4)

    # UPDATE ROOM STATUS
    def update_room_status(self):

        booked_rooms = [booking["room_no"] for booking in self.bookings]

        for room in self.rooms:

            if room["room_no"] in booked_rooms:
                room["available"] = False
            else:
                room["available"] = True

    # GET ALL ROOMS
    def get_rooms(self):
        return self.rooms

    # SEARCH ROOMS
    def search_rooms(self, room_type):

        return [
            room for room in self.rooms
            if room["type"] == room_type and room["available"]
        ]

    # BOOK ROOM
    def book_room(self, name, room_no):

        booking = {
            "customer_name": name,
            "room_no": room_no,
            "booking_time": str(datetime.now())
        }

        self.bookings.append(booking)

        self.save_bookings()

        self.update_room_status()

        return booking

    # CANCEL BOOKING
    def cancel_booking(self, room_no):

        for booking in self.bookings:

            if booking["room_no"] == room_no:

                self.bookings.remove(booking)

                self.save_bookings()

                self.update_room_status()

                return True

        return False

    # VIEW BOOKINGS
    def view_bookings(self):
        return self.bookings