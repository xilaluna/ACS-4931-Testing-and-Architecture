# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
def if_normal_cholestrol(total_cholostrol, triglyceride):
    return total_cholostrol < 200 and ldl < 100 and triglyceride < 150


def if_high_cholestrol(total_cholostrol, triglyceride):
    return 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200


def if_tlc_diet(total_cholostrol, triglyceride, ldl):
    return 200 < total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200


total_cholostrol = 70
ldl = 30
triglyceride = 120

if if_normal_cholestrol(total_cholostrol, triglyceride):
    # good level
    print('*** Good level of cholestrol ***')
elif if_high_cholestrol(total_cholostrol, triglyceride):
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif if_tlc_diet(total_cholostrol, triglyceride, ldl):
    # TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')
