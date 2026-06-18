class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 1. Minute hand moves 360 degrees / 60 minutes = 6 degrees per minute
        minute_angle = minutes * 6.0
        
        # 2. Hour hand moves 360 degrees / 12 hours = 30 degrees per hour
        # It also drifts 30 degrees / 60 minutes = 0.5 degrees per minute
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        
        # 3. Find the absolute difference between both angles
        diff = abs(hour_angle - minute_angle)
        
        # 4. Return the smaller angle (the inner angle instead of the reflex angle)
        return min(diff, 360.0 - diff)
