import sqlite3
import logging

logging.basicConfig(level=logging.INFO)


def check_room_booking(room_number, start_time, end_time):
    connected = sqlite3.connect('office.db')
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
        return {
            "full_name": full_name,
            "end_time": booked_end_time
        }

    return None


def add_booking(full_name, phone, start_time, end_time, room_number):
    booking_info = check_room_booking(room_number, start_time, end_time)

    if booking_info:
        return False

    connected = sqlite3.connect('office.db')
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
    return True

