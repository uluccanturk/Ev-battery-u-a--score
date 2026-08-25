


# ============================================================
# VEHICLE DATA (collected from the user via input())
# ============================================================
vehicle_id = input("Vehicle ID: ")

charge_cycle_count = int(input("Number of charge cycles (how many full charges): "))
battery_age_months = int(input("Battery age (months): "))
fast_charge_ratio_percent = float(input("Fast (DC) charging ratio (percent): "))
avg_charging_temp_c = float(input("Average charging temperature (Celsius): "))

harsh_braking_per_1000km = float(input("Harsh braking events per 1000 km: "))
rapid_accel_per_1000km = float(input("Rapid acceleration events per 1000 km: "))
high_speed_ratio_percent = float(input("High-speed driving ratio (percent): "))


# ============================================================
# 1) BATTERY SCORE — starts at 100, points deducted for 4 reasons
# ============================================================

# a) charge cycle penalty (max 25 points)
cycle_penalty = charge_cycle_count / 30
if cycle_penalty > 25:
    cycle_penalty = 25

# b) battery age penalty (max 15 points)
age_penalty = battery_age_months / 6
if age_penalty > 15:
    age_penalty = 15

# c) fast charging penalty (max 15 points)
fast_charge_penalty = fast_charge_ratio_percent / 100 * 15

# d) temperature penalty (for every degree above 25C, max 15 points)
temp_difference = avg_charging_temp_c - 25
if temp_difference < 0:
    temp_difference = 0
temp_penalty = temp_difference * 0.6
if temp_penalty > 15:
    temp_penalty = 15

battery_score = 100 - cycle_penalty - age_penalty - fast_charge_penalty - temp_penalty
if battery_score < 0:
    battery_score = 0


# ============================================================
# 2) USAGE SCORE — starts at 100, points deducted for 3 reasons
# ============================================================

# a) harsh braking penalty (max 30 points)
braking_penalty = harsh_braking_per_1000km * 1.2
if braking_penalty > 30:
    braking_penalty = 30

# b) rapid acceleration penalty (max 30 points)
accel_penalty = rapid_accel_per_1000km * 1.2
if accel_penalty > 30:
    accel_penalty = 30

# c) high-speed driving penalty (max 20 points)
speed_penalty = high_speed_ratio_percent / 100 * 20

usage_score = 100 - braking_penalty - accel_penalty - speed_penalty
if usage_score < 0:
    usage_score = 0


# ============================================================
# 3) COMBINED SCORE (60% battery + 40% usage)
# ============================================================
combined_score = battery_score * 0.6 + usage_score * 0.4


# ============================================================
# 4) FIND THE BIGGEST PENALTY — by comparing all 7 one by one
# ============================================================
biggest_penalty = cycle_penalty
biggest_reason = "high number of charge cycles"

if age_penalty > biggest_penalty:
    biggest_penalty = age_penalty
    biggest_reason = "the battery being old"

if fast_charge_penalty > biggest_penalty:
    biggest_penalty = fast_charge_penalty
    biggest_reason = "frequent fast charging"

if temp_penalty > biggest_penalty:
    biggest_penalty = temp_penalty
    biggest_reason = "charging at high temperatures"

if braking_penalty > biggest_penalty:
    biggest_penalty = braking_penalty
    biggest_reason = "frequent harsh braking"

if accel_penalty > biggest_penalty:
    biggest_penalty = accel_penalty
    biggest_reason = "frequent rapid acceleration"

if speed_penalty > biggest_penalty:
    biggest_penalty = speed_penalty
    biggest_reason = "high-speed-driving"
# 5) RISK LEVEL

if combined_score >= 80:
    risk_level = "low"
elif combined_score >= 60:
    risk_level = "medium"
else:
    risk_level = "high"



6)PRINT 

print()
print("Vehicle:", vehicle_id)
print("Battery Score:", round(battery_score, 1), "/ 100")
print("Usage Score:", round(usage_score, 1), "/ 100")
print("Combined Score:", round(combined_score, 1), "/ 100")
print("Risk Level:", risk_level)
print()
print("Comment: This driver's", biggest_reason, "is causing the battery to wear out faster than normal.")
print()
print("Used-Car Buyer Note: Battery + usage score", round(combined_score), "/ 100 (", risk_level, "risk )")
print("Insurance Company Note: Usage score", round(usage_score), "/ 100, can be used as an additional risk parameter.")
print("Rental Company Note: Risk level at drop-off:", risk_level)
