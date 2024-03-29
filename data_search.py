from data_set import part_dictonary, material_dictonary, finishing_dictonary, exception_dict, heat_treat_dict



def material_flag(input, number):
    """
    uses part number to find part assembly number in material dictonary, returns material from corresponding flag.
    """
    tech_drawing_numbers = material_dictonary.keys()
    for drawing_numbers in tech_drawing_numbers:
        if drawing_numbers in input:
            selected_drawing = material_dictonary.get(drawing_numbers)
            selected_flag = selected_drawing.get(number)
            return (selected_flag)
        
def finishing_numbers(input, ex_val):
    """
    uses finishing code and if part is an exception part, returns finish instructions.
    """
        
    if ex_val != "":
        return finishing_dictonary.get(ex_val.get('Finish'))
    elif input == "MSI FAKE F-100" or input == "MSI FAKE F-05":
        return ""
    elif input != "MSI FAKE F-100" or input != "MSI FAKE F-05":
        return (f'{finishing_dictonary.get(input)} DATE COMPLETED:________________')
    else:
        return ""


def heat_treat_search(input, ex_val):
    """
    uses heat treat code and if part is an exception part, returns heat treat instructions.
    """
    keys = heat_treat_dict.keys()
    if ex_val != "":
        return ex_val.get("HEAT TREAT")
    elif ex_val == "":
        if input in keys:
            heat_treat = heat_treat_dict.get(input)
            return heat_treat
    
        
def form_tool_search(form, tool, mirror, num_mirror, part_number, machined, name):
    
        
    if machined == False:
        if form == True and tool == False and mirror == False:
            if name == "OUTSIDE":
                return "FORM PART PER FAKE SPECIFICATIONS DURING FAKE INSTALL"
            else:
                return "MAKE FAKE PART CORRECTLY"
        if form == True and tool == False and mirror == True:
            return "MAKE FAKE PART CORRECTLY"
        elif form == True and tool == True and mirror == False:
            return f"FORM FAKE PART WITH FAKE TOOL NUMBER {part_number}"
        elif form == True and tool == True and mirror == True:
            return f"FORM FAKE PART WITH FAKE TOOL NUMBER {part_number} (OPP- {num_mirror})"
        elif form == False:
            return ""
    elif machined == True:
        return "MACHINE FAKE PART WITH FAKE MACHINE"
    else:
        return ""

def fabricate(machined):
    if machined == False:
        return "FAB FAKE PART VERY WELL"
    else:
        return ""
    
def stamp(input):
    if input == "STAMP":
        return "STAMP FAKE PART"
    elif input == "OTHER":
        return "MARK OTHER FAKE PART IN FAKE WAY"
    else:
        return ""
    

def mirror_t_or_f(input):
    if input == True:
        return "MORE THAN ONE PART"
    elif input == False:
        return ""

def find_exception (part_number):
    part_info = part_dictonary.get(part_number)
    ex = exception_dict.keys()
    for key in ex:
        ex_part = exception_dict.get(key)
        if key in part_number and ex_part.get(part_info.get("Material")) != None:
            ex_val = ex_part.get(part_info.get("Material"))
        else:
            ex_val = ""
        return ex_val
    
#Initalize search
#print("search initalized")
#search_number = input("enter part number: ")

# Search for specific part, pull material and finishing information from related dictonaries
def find_part(part_number):
    if part_number in part_dictonary:
        part_info = part_dictonary.get(part_number)

        return part_info
    else:
        print(f"did not find {part_number}")

#find_part(search_number)

