"""
Day 18 - Pomodoro Timer (CLI)
Author: Momina Raheel

Simple command-line Pomodoro timer:
- Set work minutes and break minutes
- Set number of cycles (work+break)
- Shows live mm:ss countdown in terminal
- Prints progress and a small bell sound when a session ends

Run: python pomodoro_day18.py
"""

import time

def get_positive_int(prompt, default):
    """Ask user for a positive integer; return default if Enter pressed."""
    while True:
        s = input(f"{prompt} (default {default}): ").strip()
        if s == "":
            return default
        if s.isdigit() and int(s) > 0:
            return int(s)
        print("Please enter a positive number or press Enter for default.")

def countdown(seconds, label="Timer"):
    """
    Countdown from seconds to 0, printing mm:ss on one line.
    Uses carriage return to overwrite the same line.
    """
    try:
        while seconds >= 0:
            mins = seconds // 60
            secs = seconds % 60
            print(f"{label} — {mins:02d}:{secs:02d}", end="\r", flush=True)
            time.sleep(1)
            seconds -= 1
    except KeyboardInterrupt:
        # Allow the user to interrupt the countdown with Ctrl+C
        print("\nTimer interrupted by user.")
        raise

def beep():
    """Play a simple terminal bell sound (works on many terminals)."""
    print('\a', end='', flush=True)

def main():
    print("=== Day 18: Pomodoro Timer ===")
    print("A focused work/break timer. Press Ctrl+C to stop at any time.\n")

    # Get user settings (with sensible defaults)
    work_min = get_positive_int("Work minutes", default=25)
    break_min = get_positive_int("Break minutes", default=5)
    cycles = get_positive_int("Number of cycles (work+break pairs)", default=4)

    total_sessions = cycles * 2  # work + break counts separately
    session_num = 0

    try:
        for cycle in range(1, cycles + 1):
            # Work session
            session_num += 1
            print(f"\nCycle {cycle} — Work session ({session_num}/{total_sessions})")
            countdown(work_min * 60, label="Work")
            beep()
            print("Work session complete! Take a short break.           ")

            # Break session
            session_num += 1
            print(f"\nCycle {cycle} — Break session ({session_num}/{total_sessions})")
            countdown(break_min * 60, label="Break")
            beep()
            print("Break complete! Get ready for the next work session. ")

        print("\n🎉 All cycles finished. Great job!")
    except KeyboardInterrupt:
        # Graceful exit on user interruption
        print("\n\nPomodoro stopped. See you next time!")

if __name__ == "__main__":
    main()
