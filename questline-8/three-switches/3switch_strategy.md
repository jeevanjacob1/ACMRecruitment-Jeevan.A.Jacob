# Strategy:

> Turn Switch 1 ON and leave it on for some long time.
> After 5 minutes, turn Switch 1 OFF.
> Immediately turn Switch 2 ON.
> Now enter the room.

# Logic for identifying the controlling switch:

> If the bulb is on, then Switch 2 controls the bulb (since it is currently ON).
> If the bulb is off but warm to the touch, then Switch 1 controls the bulb (because it was on long enough to heat the bulb before being turned off).
> If the bulb is off and cold, then Switch 3 controls the bulb (it was never turned on).
