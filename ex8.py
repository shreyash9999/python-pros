formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "thee", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("You giving me million reasons",
                       "Just let you know",
                       "You giving me million reasons",
                       "Just let it be"))


#trying an example of formatter
Drills = "hello everyone Its me Shreyash U remember AAAAaaaa!!!!!, {}"
print(Drills.format("Come On!!!"))
