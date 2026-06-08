#!/usr/bin/env python3
"""Windows GS CAN example for the MeatPi USB CAN firmware.

Install:
    pip install "python-can[gs-usb]"

Make sure the device uses a libusb-compatible Windows driver such as `libusbK`.

Example:
    python windows_gs_can_example.py --channel 0 --bitrate 500000 --can-id 0x123 --data 11223344
"""

from __future__ import annotations

import argparse
import sys

try:
    import can
except ImportError as exc:
    raise SystemExit('Missing dependency. Install with: pip install "python-can[gs-usb]"') from exc


def parse_can_id(value: str) -> int:
    return int(value, 0)


def parse_data(value: str) -> bytes:
    cleaned = value.replace(" ", "").replace("_", "").replace("-", "")
    if len(cleaned) % 2 != 0:
        raise ValueError("CAN data must contain an even number of hex digits.")
    return bytes.fromhex(cleaned)


def format_message(message: can.Message) -> str:
    flags = ["EXT" if message.is_extended_id else "STD"]
    if message.is_remote_frame:
        flags.append("RTR")
    if message.is_error_frame:
        flags.append("ERR")
    data_hex = message.data.hex().upper() if message.data else "-"
    return f"id=0x{message.arbitration_id:X} dlc={message.dlc} data={data_hex} flags={','.join(flags)}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Send one CAN frame through the Windows gs_usb backend.")
    parser.add_argument("--channel", type=int, default=0, help="GS USB channel number.")
    parser.add_argument("--device-index", type=int, default=0, help="USB device index when multiple devices exist.")
    parser.add_argument("--bitrate", type=int, default=500000, help="CAN bitrate in bit/s.")
    parser.add_argument("--can-id", type=parse_can_id, default=0x123, help="Arbitration ID, for example 0x123.")
    parser.add_argument("--data", default="11223344", help="CAN payload as hex bytes.")
    parser.add_argument("--extended", action="store_true", help="Send an extended-ID frame.")
    parser.add_argument("--timeout", type=float, default=5.0, help="Receive timeout in seconds.")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        payload = parse_data(args.data)
    except ValueError as exc:
        print(f"Invalid --data value: {exc}", file=sys.stderr)
        return 1

    bus = can.Bus(
        interface="gs_usb",
        channel=args.channel,
        index=args.device_index,
        bitrate=args.bitrate,
    )

    try:
        message = can.Message(
            arbitration_id=args.can_id,
            data=payload,
            is_extended_id=args.extended,
        )
        bus.send(message)
        print(f"Opened gs_usb channel {args.channel} at {args.bitrate} bit/s")
        print(f"Sent:     {format_message(message)}")

        received = bus.recv(args.timeout)
        if received is None:
            print(f"No CAN frame received within {args.timeout:.1f}s.")
            return 0

        print(f"Received: {format_message(received)}")
        return 0
    finally:
        bus.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())
