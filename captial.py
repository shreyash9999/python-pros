
def captial(f_name, l_name):
    first_name = f_name.title()
    # the title will convert any name or string to standrad formate like "Shreyash" means 1st letter capital and read small
    last_name = l_name.title()

    result = (f"{first_name} {last_name}")
    return result
standrad_form = captial("kaji", "rtanGA")
print (standrad_form)