# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def output_answer(mean, sd):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


def get_inputs(num_student):
    grade_list = []
    for _ in range(num_student):
        grade_list.append(int(input('Enter a number: ')))

    return grade_list


def calc_mean(grade_list):
    grade_total = 0
    for grade in grade_list:
        grade_total += grade
    mean = grade_total / len(grade_list)
    return mean


def calc_stand_dev(mean, grade_list):
    sd = 0  # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd


def print_stat():
    n_student = 5
    grade_list = get_inputs(n_student)
    mean = calc_mean(grade_list)
    sd = calc_stand_dev(mean, grade_list)
    # print out the mean and standard deviation in a nice format.
    output_answer(mean, sd)


print_stat()
