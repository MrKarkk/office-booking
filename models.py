import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

connected = sqlite3.connect('office.db')

def check_room_booking(room_number, start_time, end_time):
    cursor = connected.cursor()

    query = """
    SELECT full_name, end_time
    FROM bookings
    WHERE room_number = ?
    AND start_time < ?
    AND end_time > ?
    ORDER BY end_time DESC
    LIMIT 1
    """

    cursor.execute(query, (room_number, end_time, start_time))
    result = cursor.fetchone()
    connected.close()

    if result:
        full_name, booked_end_time = result
        logging.info(
            f"Room {room_number} is already booked by {full_name} until {booked_end_time}."
        )
        return {
            "full_name": full_name,
            "end_time": booked_end_time
        }

    return None

def add_booking(full_name, phone, start_time, end_time, room_number):
    booking_info = check_room_booking(room_number, start_time, end_time)

    if booking_info:
        return False

    cursor = connected.cursor()

    query = """
    INSERT INTO bookings (full_name, phone, start_time, end_time, room_number)
    VALUES (?, ?, ?, ?, ?)
    """

    cursor.execute(
        query,
        (full_name, phone, start_time, end_time, room_number)
    )
    connected.commit()
    connected.close()

    logging.info(
        f"Booking added for {full_name} in room {room_number} "
        f"from {start_time} to {end_time}."
    )
    return True