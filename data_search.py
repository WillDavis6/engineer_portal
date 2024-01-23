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
        
def finishing_code(input, ex_val):
    """
    uses finishing code and if part is an exception part, returns finish instructions.
    """
        
    if ex_val != "":
        return finishing_dictonary.get(ex_val.get('Finish'))
    elif input == "MSI FAKE F-100" or input == "MSI FAKE F-05":
        return ""
    elif input != "MSI FAKE F-100" or input != "MSI FAKE F-05":
        return (f'{finishing_dictonary.get(input)}' DATE COMPLETED:________________)
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
            

*******************************************************************************************************

        elif form == True and tool != True and mirror == False:
            return "For part to Fake spec 123ABC:____________"
        elif form == True and tool == True and mirror == False:
            return f"Form part to fake spec using tool T-{self.part_number}"
        elif form == True and tool == True and mirror == True:
            return f"Form part to fake spec using tool T-{self.part_number} (OPP - T-{num_mirror})"
        elif form == False:
            return ""
        else:
            return "Machine Fake part to fake specifications:___________________"
        

    def compile_traveler(self):
        stock = self.part_info.get("Stock Size")
        heat_treat_search(self.part_info)


#Initalize search
print("search initalized")
#search_number = input("enter part number: ")

# Search for specific part, pull material and finishing information from related dictonaries
def find_part(part_number):
    if part_number in part_dictonary:
        part_info = part_dictonary.get(part_number)

        print(part_info)
        return Traveler(part_info, part_number)
    else:
        print(f"did not find {search_number}")

#find_part(search_number)

