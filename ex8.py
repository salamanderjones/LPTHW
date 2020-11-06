formatter = "{} {} {} {}" #this variable equals four format strings?

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Sandwich time",
        "was last week",
        "Butter boy time",
        "Is right around the corner"
))