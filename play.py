import argparse
import socket
from pathlib import Path

import soco

RESOURCES = Path(__file__).parent / "resources"


def local_ip():
    """Best-effort LAN IP of this machine (used in the URL Sonos fetches)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()


def main():
    parser = argparse.ArgumentParser(description="Play an audio file on a Sonos speaker.")
    parser.add_argument("file", help="audio filename inside the resources/ folder")
    parser.add_argument("--speaker", help="speaker name (defaults to first found)")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--volume", type=int, default=25)
    args = parser.parse_args()

    speakers = list(soco.discover())
    if not speakers:
        raise SystemExit("No Sonos speakers found on the network.")

    for s in speakers:
        print(s.player_name, s.ip_address)

    speaker = soco.discovery.by_name(args.speaker) if args.speaker else speakers[0]
    if speaker is None:
        raise SystemExit(f"Speaker {args.speaker!r} not found.")

    path = RESOURCES / args.file
    if not path.is_file():
        raise SystemExit(f"Audio file not found: {path}")

    url = f"http://{local_ip()}:{args.port}/{path.name}"
    print(f"Playing {url} on {speaker.player_name}")
    speaker.play_uri(url)
    speaker.volume = args.volume


if __name__ == "__main__":
    main()
