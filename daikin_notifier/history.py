import os
from pathlib import Path

HISTORY_FILE = Path(__file__).parents[1] / "history.txt"


def already_notified():
    return os.path.exists(HISTORY_FILE)


def save_history():
    with open(HISTORY_FILE, "w") as fp:
        fp.write("")


def delete_history():
    if already_notified():
        os.remove(HISTORY_FILE)
