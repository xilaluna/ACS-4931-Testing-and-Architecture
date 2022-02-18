# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


class Steak_State:
    def __init__(self, time, temp, pressure, desired_state) -> None:
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired_state = desired_state

    def get_cooking_progress(self):
        return self.time * self.temp * self.pressure * COOKED_CONSTANT

    def is_well_done(self):
        return self.desired_state == 'well-done' and self.get_cooking_progress() >= WELL_DONE

    def is_medium(self):
        return self.desired_state == 'medium' and self.get_cooking_progress() >= MEDIUM

    def is_cookeding_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()

    def check_cooked(self):
        if self.is_cookeding_criteria_satisfied():
            print('cooking is done.')
        else:
            print('ongoing cooking.')


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]
desired_state = 'well-done'

steak = Steak_State(time, temp, pressure, desired_state)

steak.check_cooked()
