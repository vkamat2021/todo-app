from bonus.convertUsMetric_func_parse import parse
from bonus.convertUsMetric_func_convert import convert

feet_inches = input("Enter feet and inches separated by a space: ")

f, i = parse(feet_inches)
result = convert(f, i)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use this slide.")
