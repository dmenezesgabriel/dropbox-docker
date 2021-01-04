import os
import time

import dropbox
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
PATTERNS = "*"
IGNORE_PATTERNS = ""
IGNORE_DIRECTORIES = False
CASE_SENSITIVE = True
PATH = "/dropbox"
GO_RECURSIVELY = True


dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

print(dbx.users_get_current_account())


def on_created(event):
    print(f"File {event.src_path} created")


def on_deleted(event):
    print(f"File {event.src_path} deleted")


def on_modified(event):
    print(f"File {event.src_path} modified")


def on_moved(event):
    print(f"File {event.src_path} moved")


event_handler = PatternMatchingEventHandler(
    PATTERNS,
    IGNORE_PATTERNS,
    IGNORE_DIRECTORIES,
    CASE_SENSITIVE,
)

event_handler.on_created = on_created
event_handler.on_deleted = on_deleted
event_handler.on_modified = on_modified
event_handler.on_moved = on_moved

observer = Observer()

observer.schedule(event_handler, PATH, recursive=GO_RECURSIVELY)

if __name__ == "__main__":
    print("start")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("exception")
        observer.stop()
        observer.join()
