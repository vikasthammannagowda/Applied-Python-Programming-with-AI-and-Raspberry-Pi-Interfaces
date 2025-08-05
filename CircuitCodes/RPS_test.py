from gpiozero import LED, Button
from time import sleep
import random

choice_leds = [LED(5), LED(6), LED(13)]

runner_leds = [LED(17), LED(27), LED(22)]

buttons = [Button(19, pull_up = True, bounce_time = 0.05),
           Button(26, pull_up = True, bounce_time = 0.05),
           Button(21, pull_up = True, bounce_time = 0.05)]

def get_user_choice():
    while True:
        for idx, btn in enumerate(buttons):
            if btn.is_pressed:
                return idx
        sleep(0.05)

def animate_slow_to(target):
    delay = 0.1
    steps = random.randint(15, 25)
    for i in range(step):
        idx = i%3
        runner_leds[idx].on()
        runner_leds[(idx-1)%3].off()
        sleep(delay)

    cur = steps % 3
    while cur!=target:
        cur = (cur + 1)%3
        runner_leds[cur].on()
        runner_leds[(cur-1)%3].off()
        sleep(delay)
        delay += 0.03
