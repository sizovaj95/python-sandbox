"""Given the time of the day (hours, minutes) return the angle between the hands on a clock
Assumptions:
- consider only absolute angle between hands
- 12-hour format
- realistic_clock: hour hand moves between hours with minute hand"""
from typing import Optional


def find_angle_from_noon(minutes: int) -> float:
    """Find angle between a hand and 12.00"""
    return minutes * (360 / 60)


def convert_angle_to_degrees_and_minutes(angle: float) -> tuple[int, int]:
    """Convert 35.5° to 35°30'"""
    full_angle = angle.__floor__()
    minutes = ((angle - full_angle) * 60).__floor__()
    return full_angle, minutes


def adjust_hours_hand(time: tuple[int, int]):
    """Move hours hand in the clockwise direction proportionally to minutes hand move"""
    ratio = time[1] / 60
    hour_in_minutes = time[0] * 5 + ratio * 5
    return hour_in_minutes


def find_angle_between_hands(time: tuple[int, int], realistic_clock: bool = True) -> \
        tuple[Optional[int], Optional[int]]:
    hour = time[0]
    minute = time[1]
    try:
        assert 1 <= hour <= 12, "Hours can only be between 0 and 11"
        assert 0 <= minute <= 59, "Minutes can only be between 0 and 59"
    except AssertionError:
        return None, None

    if realistic_clock:
        hour_in_minutes = adjust_hours_hand(time)
    else:
        hour_in_minutes = hour * 5
    if hour_in_minutes >= 60:
        hour_in_minutes -= 60

    hour_angle = find_angle_from_noon(hour_in_minutes)
    minutes_angle = find_angle_from_noon(minute)

    angle_between = abs(hour_angle - minutes_angle)
    angle_between = convert_angle_to_degrees_and_minutes(angle_between)
    return angle_between


def main():
    time = (0, 30)
    angle = find_angle_between_hands(time)
    print(f"Angle between {time[0]} hour(s) hand and {time[1]} minute(s) hand is {angle[0]}°{angle[1]}'")


if __name__ == "__main__":
    main()
