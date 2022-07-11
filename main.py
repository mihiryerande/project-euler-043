# Problem 43:
#     Sub-string Divisibility
#
# Description:
#     The number, 1406357289, is a 0 to 9 pandigital number because
#       it is made up of each of the digits 0 to 9 in some order,
#       but it also has a rather interesting sub-string divisibility property.
#
#     Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on.
#     In this way, we note the following:
#         d_2 d_3 d_4  = 406 is divisible by 2
#         d_3 d_4 d_5  = 063 is divisible by 3
#         d_4 d_5 d_6  = 635 is divisible by 5
#         d_5 d_6 d_7  = 357 is divisible by 7
#         d_6 d_7 d_8  = 572 is divisible by 11
#         d_7 d_8 d_9  = 728 is divisible by 13
#         d_8 d_9 d_10 = 289 is divisible by 17
#
#     Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations
from typing import List, Tuple


def main() -> Tuple[List[int], int]:
    """
    Returns a list of all 0-to-9 pandigital numbers having the 'sub-string divisibility' property,
      as well as the sum of those numbers.

    Returns:
        (Tuple[List[int], int]):
            Tuple of ...
              * List of 0-to-9 pandigitals which are sub-string divisible
              * Sum of those
    """
    divisors = [2, 3, 5, 7, 11, 13, 17]
    digits = '0123456789'

    # Iterate through all possible 0-to-9 pandigitals
    nums = []
    total = 0
    for s in permutations(digits):
        # Skip numbers where '0' is the first digit, as these aren't 0-to-9 pandigital
        if s[0] == '0':
            continue
        else:
            s = ''.join(s)

        # Check for sub-string divisibility property
        if all(map(lambda i: int(s[i+1:i+4]) % divisors[i] == 0, range(len(divisors)))):
            num = int(s)
            nums.append(num)
            total += num
    return nums, total


if __name__ == '__main__':
    divisible_pandigitals, divisible_pandigitals_sum = main()
    print('0-to-9 pandigital numbers having sub-string divisibility property:')
    for divisible_pandigital in divisible_pandigitals:
        print('  {}'.format(divisible_pandigital))
    print('Sum of those:')
    print('  {}'.format(divisible_pandigitals_sum))
