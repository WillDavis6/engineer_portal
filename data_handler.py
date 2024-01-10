from data_set import part_dictonary
from data_set import material_dictonary
from data_set import finishing_dictonary


#Class for handing the generation of traveler information
class Traveler:
    def __init__(self, part_info, part_number):
        self.part_info = part_info
        self.part_number = part_number

    #def __repr__():
     #   print("part_info")

    def material_flag(self):
        tech_draw_num = material_dictonary.keys()
        for draw_num in tech_draw_num:
            if draw_num in self.part_info:
                selected_draw = material_dictonary.get(draw_num)
                selected_flag = selected_draw.get(self.part_number)
                return (selected_flag)
        
    def finishing_code(self):
        finish = self.part_info.get("Finish")
        if finish == "MSI FAKE F-100" or input == "MSI FAKE F-05":
            return ""
        elif finish != "MSI FAKE F-100" or input != "MSI FAKE F-05":
            return (f"{finishing_dictonary.get(input)} PRODUCTION STAMP/DATE:____________")

    def heat_treat_search(self):
        heat_treat = self.part_info.get("Heat Treat")
        if heat_treat == "MSI FAKE T70":
            return ""
        
        elif heat_treat == "MSI FAKE S20":
            return "HEAT TREAT TO FAKE REG OF S20"
        
        elif input == 'None':
            return ""
        
        else:
            return ""
        
    def form_tool_search(self):
        form = self.part_info.get("Formed")
        tool = self.part_info.get("Tooling")
        mirror = self.part_info.get("Mirror Part")
        num_mirror = self.part_info.get("Mirror Part #")
        machined = self.part_info.get("Machined")
        
        if machined == False:
            if form == True and tool != True and mirror == False:
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

