# Inputs
name = input("What is your full name?: ")
weight = float(input("How much do you weigh (kg)?: "))
height = float(input("How tall are you (cm)?: "))
age = int(input("How old are you?: "))
print("Genders: M / F")
gender = input("Gender: ")
days_exercised = int(input("How many days did you exercise in the past 30 days?: "))
avg_duration = int(input("What was the average duration of your workouts (in minutes)?: "))
push_ups = int(input("How many push-ups can you do in one set?: "))
squats = int(input("How many squats can you do in one set?: "))
goal = int(input("Fitness goal (1=Weight loss, 2=Muscle gain, 3=General fitness): "))

# Calculations Required
bmi = weight / ((height / 100) ** 2)
is_male = gender.upper() == "M"
is_female = gender.upper() == "F"

bmr_male = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
bmr_female = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
bmr = (is_male * bmr_male) + (is_female * bmr_female)

se_tdee = bmr * 1.2
ac_tdee = bmr * 1.375

freq = (days_exercised / 30) * 100
total_min = days_exercised * avg_duration
score = push_ups * 2 + squats * 1.5

# Calorie targets by goal (using boolean arithmetic)
weight_loss_target = (goal == 1) * (ac_tdee - 500)
muscle_gain_target = (goal == 2) * (ac_tdee + 300)
maintenance_target = (goal == 3) * ac_tdee
calorie_target = weight_loss_target + muscle_gain_target + maintenance_target

# All displayed as True/False
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

# Output
print(f"\nFull name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")

print(f"\nWeight: {weight} kg")
print(f"Height: {height} cm")
print(f"Body Mass Index: {bmi:.2f}")
print(f"Sedentary TDEE: {se_tdee:.1f}")
print(f"Active TDEE: {ac_tdee:.1f}")

print(f"\nDays exercised (out of 30): {days_exercised}")
print(f"Exercise frequency percentage: {freq:.1f}")
print(f"Average duration per session: {avg_duration} min")
print(f"Total exercise minutes in month: {total_min} min")

print(f"\nPush-ups in one set: {push_ups}")
print(f"Squats in one set: {squats}")
print(f"Fitness score: {score:.1f}")

print(f"\nWeight loss target: {weight_loss_target:.1f}")
print(f"Muscle gain target: {muscle_gain_target:.1f}")
print(f"General fitness target: {maintenance_target:.1f}")
print(f"Selected calorie target: {calorie_target:.1f}")
print(f"Fitness goal selected (1, 2, or 3): {goal}")

print(f"\nBmi Reasonable: {bmi_ok}")
print(f"Exercise Frequency Good: {freq_good}")
print(f"Exercise Frequency Excellent: {freq_excellent}")
print(f"Exercise Duration Adequate: {duration_ok}")
print(f"Basic Pushup Strength: {push_basic}")
print(f"Basic Squat Strength: {squat_basic}")
print(f"Good Pushup Strength: {push_good}")
print(f"Good Squat Strength: {squat_good}")
print(f"Consistency Strong: {consistency_strong}")
print(f"Basic Strength Present: {basic_strength_present}")
print(f"Ready For Progression: {ready_for_progression}")