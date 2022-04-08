from array import array
from pickle import OBJ
from typing import List

from django.template import Library


def reverseList(A, start, end):
    while start < end:
        # if(A[end] != ',' and A[start] !=','):
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A

str = [1, 2, 3, 4, 5, 6]
# str =list(input('enter a input List here:'))
print(type(str))
print(str)
print("Reversed list is")
print(reverseList(str, 0, 5))   