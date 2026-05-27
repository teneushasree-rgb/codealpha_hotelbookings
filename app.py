import streamlit as st
from hotel import HotelSystem

hotel = HotelSystem()

st.set_page_config(page_title="Hotel Reservation System", layout="centered")

st.title("🏨 Hotel Reservation System")

menu = st.sidebar.selectbox(
    "Menu",
    ["View Rooms", "Book Room", "Cancel Booking", "View Bookings"]
)

# VIEW ROOMS
if menu == "View Rooms":
    st.header("Available Rooms")

    rooms = hotel.get_rooms()

    for room in rooms:
        status = "Available" if room["available"] else "Booked"

        st.subheader(f"Room {room['room_no']} - {room['type']}")
        st.write(f"Price: ₹{room['price']}")
        st.write(f"Status: {status}")
        st.write("---")

# BOOK ROOM
elif menu == "Book Room":
    st.header("Book a Room")

    name = st.text_input("Enter Your Name")

    room_type = st.selectbox(
        "Select Room Type",
        ["Standard", "Deluxe", "Suite"]
    )

    if st.button("Search Available Rooms"):

        available_rooms = hotel.search_rooms(room_type)

        if available_rooms:
            st.success("Rooms Available")

            room_numbers = [room["room_no"] for room in available_rooms]

            selected_room = st.selectbox(
                "Choose Room",
                room_numbers
            )

            if st.button("Proceed to Payment"):

                st.info("Payment Successful ✅")

                booking = hotel.book_room(name, selected_room)

                st.success("Room Booked Successfully!")

                st.write("### Booking Details")
                st.json(booking)

        else:
            st.error("No Rooms Available")

# CANCEL BOOKING
elif menu == "Cancel Booking":
    st.header("Cancel Reservation")

    room_no = st.number_input(
        "Enter Room Number",
        min_value=1,
        step=1
    )

    if st.button("Cancel Booking"):

        result = hotel.cancel_booking(room_no)

        if result:
            st.success("Booking Cancelled Successfully")
        else:
            st.error("No Booking Found")

# VIEW BOOKINGS
elif menu == "View Bookings":
    st.header("All Bookings")

    bookings = hotel.view_bookings()

    if bookings:
        for booking in bookings:
            st.write(booking)
    else:
        st.info("No Bookings Available")