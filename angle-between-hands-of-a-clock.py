class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        deg_per_min = 360 / 60
        deg_per_hr = 360 / 12
        min_angle = deg_per_min * minutes
        hour_angle = (deg_per_hr * (hour % 12)) + (deg_per_hr / 60 * minutes)
        angle = abs(hour_angle - min_angle)

        return min(angle, abs(360 - angle))
