import math
from calculate_grades import calculate_stat


def test_calculate_grades():
    mean_answer = 69.5
    sd_answer = 22.299
    grades = [88, 34, 67, 89]
    mean, sd = calculate_stat(grades)
    assert math.isclose(mean, mean_answer, abs_tol=0.05)
    assert math.isclose(sd, sd_answer, abs_tol=0.05)
