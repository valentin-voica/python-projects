from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

nose = LEDBoard(25, pwm=True)
eyes = LEDBoard(23, 24, pwm=True)
body = LEDBoard(7, 8, 9, 17, 18, 22, pwm=True)

for led in nose:
  led.blink(on_time=3, fade_out_time=1)

for led in eyes:
  led.blink(on_time=1, off_time=0.5, fade_in_time=0.2, fade_out_time=0.5, background=True)

for led in body:
  led.source_delay = 0.2
  led.source = random_values()

pause()
