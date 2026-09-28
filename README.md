# waltuh

Play an audio file on Sonos speakers on the local network.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Use

Put the audio file in `resources/`, then serve that folder:

```powershell
cd resources
python -m http.server 8080
```

In another terminal, play it on a speaker:

```powershell
python play.py song.mp3
```

Options: `--speaker "Living Room"`, `--port 8080`, `--volume 25`.
