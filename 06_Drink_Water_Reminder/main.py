import time
from plyer import notification
from datetime import datetime


def send_notification():
    notification.notify(
        title="💧 Drink Water Reminder",
        message="Time to drink water and stay hydrated Tanzim.",
        timeout=10
    )


def water_reminder(interval_minutes=15):
    interval_seconds = interval_minutes * 60

    print("=" * 40)
    print("Water Drinking Reminder Started")
    print(f"Notification Interval: {interval_minutes} minutes")
    print("Press CTRL + C to stop the reminder.")
    print("=" * 40)

    try:
        while True:
            time.sleep(interval_seconds)
            send_notification()
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Notification Sent")

    except KeyboardInterrupt:
        print("\nWater Reminder Stopped Successfully.")


if __name__ == "__main__":
    water_reminder(15)