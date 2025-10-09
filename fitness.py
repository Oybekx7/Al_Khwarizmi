#     INPUTS
name = input("Whats is your full name?: ")
age = int(input("How old are you?: "))
weight = float(input("How much do you weight(kg)?: "))
height = float(input("How tall are you(cm)?: "))

print(" Genders: M / F")
gender = input("Gender: ").upper()

is_male = gender.upper() == "M"
is_female = gender.upper() == "F"
bmr_male = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
bmr_female = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
bmr = (is_male * bmr_male) + (is_female * bmr_female)
# if gender == "M":
#     bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
# else gender == "F":
#     bmr =  447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
# else :
#     print ("You can choos only M or F!")
#     print(" Genders: M / F")
#     gender = input("Gender: ").strip().upper()
#     if gender == "M":
#      bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
#     elif gender == "F":
#      bmr =  447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
#     else :
#      print ("You can choos only M or F!")

days_exercised = int(input("How many days did you exercise in the past 30 days?: "))
avg_duration = int(input("What was the average duration of your workouts (in minutes)?: "))
push_ups = int(input("How much did you can push-ups in one set?: "))
squats = int(input("How much did you can squats in one set?: "))
goal = int(input("Fitness goal (1=Weight loss, 2=Muscle gain, 3=General fitness): "))

bmi = weight / (height ** 2)
se_tdee = bmr * 1.2
ac_tdee = bmr * 1.375
freq = (days_exercised / 30) * 100
total_min = days_exercised * avg_duration
score = push_ups * 2 + squats * 1.5

# if goal == 1 :
#     weight_loss_target = ac_tdee - 500

# elif goal == 2 :
#     muscle_gain_targe = ac_tdee + 300

# elif goal == 3 :
#     maintenance_target = ac_tdee

# else:
#     print("You can only choos 1 or 2 or 3")

# Calorie targets by goal
weight_loss_target = ac_tdee - 500
muscle_gain_targe = ac_tdee + 300
maintenance_target = ac_tdee

bmi_ok = 18.5 <= bmi < 30
freq_good = freq >= 60
freq_excellent = freq >= 80
duration_ok = avg_duration >= 30

push_basic = push_ups >= 5
squat_basic = squats >= 10
push_good = push_ups >= 10
squat_good = squats >= 20

consistency_strong = (freq >= 70) and (avg_duration >= 30)
basic_strength_present = (push_ups >= 5) and (squats >= 10)
ready_for_progression = consistency_strong and basic_strength_present

# TABLE
print (f"Full name: {name}")
print (f"Gender: {gender}")
print (f"Age: {age}")

print (f"Weight: {weight}")
print (f"Height: {height}")
print (f"Body Mass Index: {bmi:.4f}")
print (f"Sedentary TDEE: {se_tdee:.1f}")
print (f"Active TDEE: {ac_tdee:.1f}")

print (f"Days exercised (out of 30): {days_exercised}")
print (f"Exercise frequency percentage: {freq:.1f}")
print (f"Average duration per session: {avg_duration}")
print (f"Total exercise minutes in month: {total_min}")

print (f"Push-ups in one set: {push_ups}")
print (f"Squats in one set: {squats}")
print (f"Fitness score: {score}")

print (f"Weight loss target: {weight_loss_target:.1f}")
print (f"Muscle gain target: {muscle_gain_targe:.1f}")
print (f"General fitness targete: {maintenance_target:.1f}")
print (f"Fitness goal selected (1, 2, or 3): {goal}")

print (f"Bmi Reasonable: {bmi_ok}")
print (f"Exercise Frequency Good: {freq_good}")
print (f"Exercise Frequency Excellent: {freq_excellent}")
print (f"Exercise Duration Adequate: {duration_ok}")
print (f"Basic Pushup Strength: {push_basic}")
print (f"Basic Squat Strength: {squat_basic}")
print (f"Good Pushup Strength: {push_good}")
print (f"Good Squat Strength: {squat_good}")
print (f"Consistency Strong: {consistency_strong}")
print (f"Basic Strength Present: {basic_strength_present}")
print (f"Ready For Progression: {ready_for_progression}")