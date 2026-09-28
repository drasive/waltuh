import soco


def main():
    speakers = list(soco.discover())
    if not speakers:
        raise SystemExit("No Sonos speakers found on the network.")

    print("Speakers:")
    for s in sorted(speakers, key=lambda s: s.player_name):
        print(f"  {s.player_name} ({s.ip_address})")

    print("\nGroups (playing any member plays the whole group):")
    for group in speakers[0].all_groups:
        coordinator = group.coordinator.player_name
        others = sorted(m.player_name for m in group.members if m != group.coordinator)
        members = ", ".join([f"{coordinator} (coordinator)"] + others)
        print(f"  {members}")


if __name__ == "__main__":
    main()
