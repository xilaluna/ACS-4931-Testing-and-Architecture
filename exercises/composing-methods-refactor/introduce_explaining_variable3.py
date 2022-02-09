# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05


def cooking_calculations(time, temp, pressure):
    return time * temp * pressure * COOKED_CONSTANT


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if desired_state == 'well-done' and cooking_calculations(time, temperature, pressure) >= WELL_DONE:
        return True
    if desired_state == 'medium' and cooking_calculations(time, temperature, pressure) >= MEDIUM:
        return True
    return False
