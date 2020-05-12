"""
Functions for converting speed percentage to other useful information and vice-versa
"""

# Define lower and upper bounds
# For a stepper motor speed is determined by the time between steps
# and is the delay between switching the step pin high to low: stepdelay variable
# These values were found empirically

upp_stepdelay = 0.003  # Highest speed
low_stepdelay = 0.02  # Slowest speed


# This type of scaling is imperfect but best I can do without any accurate speed measurements

def stepdelay_to_percent(stepdelay):
    if upp_stepdelay <= stepdelay <= low_stepdelay:
        return 100 - (((stepdelay - upp_stepdelay) * 100) / (low_stepdelay - upp_stepdelay))
    else:
        return None


def percentage_to_step_delay(percent):
    if 0 <= percent <= 100:
        return (((100-percent)*(low_stepdelay-upp_stepdelay))/100) + upp_stepdelay
    else:
        return None


if __name__ == '__main__':
    stepdelays = [0.02, 0.01, 0.0075, 0.005, 0.004, 0.003]
    speed_percentage = []
    for i in stepdelays:
        speed_percentage.append(stepdelay_to_percent(i))
        print(f'The percentage of speed for a stepdelay of {i:.3f}s is {speed_percentage[-1]:.2f}%')

    for i in speed_percentage:
        rev_stepdelay = percentage_to_step_delay(round(i))
        print(f'Using the inverse function the stepdelay value from a speed percentage of {round(i):.2f}% is '
              f'{rev_stepdelay:.6f}s')
