

sams_age = 16
too_young = sams_age < 17
car_driver = sams_age== 17

print(f"Is Sam too young to drive? {too_young}")
print(f"Can Same drive a car? {car_driver}")

age = 15
adult_ticket = age >= 12
print(f"Buy one adult ticket: {adult_ticket}")

age =75
if age >= 55:
    print("Discount applied")

score =51
pass_grade = score > 50
if pass_grade:
    print("passed!")

old_password = "hello123"
new_password = "goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "goodbye321" == new_password

print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced")