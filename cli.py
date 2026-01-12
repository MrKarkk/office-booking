import argparse
import logging
from models import add_booking, check_room_booking

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="Office Room Booking CLI")
    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("check", help="Check room booking")
    check_parser.add_argument("room_number", type=int, help="Room number to check")
    check_parser.add_argument("start_time", type=str, help="Start time of the booking")
    check_parser.add_argument("end_time", type=str, help="End time of the booking")

    add_parser = subparsers.add_parser("add", help="Add a new booking")
    add_parser.add_argument("full_name", type=str, help="Full name of the person booking")
    add_parser.add_argument("phone", type=str, help="Phone number of the person booking")
    add_parser.add_argument("start_time", type=str, help="Start time of the booking")
    add_parser.add_argument("end_time", type=str, help="End time of the booking")
    add_parser.add_argument("room_number", type=int, help="Room number to book")

    args = parser.parse_args()

    if args.command == "check":
        result = check_room_booking(args.room_number, args.start_time, args.end_time)
        if result:
            logging.info(
                f"Room {args.room_number} is booked by {result['full_name']} "
                f"until {result['end_time']}."
            )
        else:
            logging.info(f"Room {args.room_number} is available from {args.start_time} to {args.end_time}.")

    elif args.command == "add":
        success = add_booking(
            args.full_name,
            args.phone,
            args.start_time,
            args.end_time,
            args.room_number
        )
        if success:
            logging.info(f"Booking successfully added for {args.full_name}.")
        else:
            logging.info(f"Failed to add booking: Room {args.room_number} is already booked.")


if __name__ == "__main__":
    main()