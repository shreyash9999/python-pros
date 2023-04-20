script , user_name = argv
#We have assigned value for prompt
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you few questions.")
print(f"Do you like me {user_name}?")
#The assigned value of prompt will be diplayed first and then you will be asked to give some input.
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")
