# --- Day 4: Secure Container ---
#
# You arrive at the Venus fuel depot only to discover it's protected by a password.
# The Elves had written the password on a sticky note, but someone threw it out.
#
# However, they do remember a few key facts about the password:
#
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#
# Other than the range rule, the following are true:
#
# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
#
# How many different passwords within the range given in your puzzle input meet these criteria?
#
# Your puzzle input is 402328-864247.

# 6 digit
# two adjacent digits are the same
# increasing numbers

input_start = 402328
input_end = 864247
max_len = 6
num_poss = 0
passwords = []


def is_increasing(number):
    passw = str(number)
    check = False
    high_num = int(passw[0])
    for j in range(1, len(passw)):
        current_n = int(passw[j])
        if current_n >= high_num:
            check = True
            high_num = current_n
        else:
            check = False
            break
    return check


# def is_doubles(number):
#     passw = str(number)
#     check = False
#     last_num = int(passw[0])
#     for j in range(1, len(passw)):
#         current_n = int(passw[j])
#         if current_n == last_num:
#             check = True
#             break
#         last_num = current_n
#     return check


def is_doubles(number):
    passw = str(number)
    d_count = 1
    prev_num = int(passw[0])
    for j in range(1, len(passw)):
        current_n = int(passw[j])
        if current_n == prev_num:
            d_count += 1
        else:
            if d_count == 2:
                return True
            d_count = 1
        prev_num = current_n
    return d_count == 2


for i in range(input_start, input_end + 1):
    check_increase = is_increasing(i)
    check_doubles = is_doubles(i)
    if check_increase and check_doubles:
        num_poss += 1

print(num_poss, " Possible passwords")
