    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
    input_list = []
    for x in input:
        input_list.append(x)
    
    #length/size of the list
    s = len(input_list)
    
    if input_list[s-1] == "y" or input_list[s-1] == "Y":
        if input_list[s-2] == "p" or input_list[s-2] == "P":
            return True
        else:
            return False
    else: 
        return False

    