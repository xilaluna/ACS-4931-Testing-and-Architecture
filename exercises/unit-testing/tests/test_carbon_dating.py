import pytest
import math
from carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.


def test_age_carbon_14_dating():
    ratio = 0.35
    exprected_result = 8680.34

    # if ratio <= 0:
    #     with pytest.raises(TypeError):
    #         get_age_carbon_14_dating(ratio)

    assert math.isclose(get_age_carbon_14_dating(ratio),
                        exprected_result, abs_tol=0.5)
