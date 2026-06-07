from winotify import Notification, audio

def show_light(digest):
    levels = {
        "high":   ("🔴 Inbox needs you", audio.Mail),
        "medium": ("🟡 A few things to handle", audio.Default),
        "low":    ("🟢 Inbox is calm", None),
    }
    title, sound = levels[digest.urgency_level]

    toast = Notification(
        app_id="Check Email Light",
        title=title,
    )
    if sound:
        toast.set_audio(sound, loop=False)
    toast.show()