# family_names = ["Jane", "Win", "Best", "Kevin", "Champ", "Liu", "John", "Brown", "Green"]
# num_attendees = [3, 6, 5, 1, 3, 4, 5, 7, 3]
# adult_attendees = [3, 4, 5, 1, 1, 2, 5, 6, 3]
# child_attendees = [1, 2, 3, 0, 1, 0, 0, 1, 0]
# priority = 3


class Party:
    def __init__(self):
        self.info_attendees = {}
        self.detailed_info_attendees = {}

    def add_attendees(self, family_name, number_of_attendees):
        self.info_attendees[family_name] = number_of_attendees

    def detailed_attendees(self):
        for num in range(0, len(family_names)):
            temp_list = [adult_attendees[num], child_attendees[num]]
            self.detailed_info_attendees[family_names[num]] = temp_list
        # print(self.detailed_info_attendees)  # for checking

    def check_and_resolve(self):
        # print(self.info_attendees)  # for checking the info_attendees
        for n in family_names:
            if self.info_attendees[n] != self.detailed_info_attendees[n][0] + self.detailed_info_attendees[n][1]:
                self.info_attendees[n] = self.detailed_info_attendees[n][0] + self.detailed_info_attendees[n][1]
        # print(self.info_attendees)  # for checking after resolving

    def get_total_attendees(self):
        global total_num_attendees
        total_num_attendees = 0
        for num1, num2 in zip(adult_attendees, child_attendees):
            total_num_attendees += num1 + num2
        # print(total_num_attendees)  # for checking the number of attendees
        return total_num_attendees

    def filter_attendees(self):
        global filter_names
        filter_names = []
        for name in family_names:
            if self.info_attendees[name] > 2:
                filter_names.append(name)
            elif self.detailed_info_attendees[name][1] > 0:
                filter_names.append(name)
        # print(filter_names)  # for checking the names
        return filter_names

    def covid_changes(self):
        for name in filter_names:
            print(name, ":plz bring only up to 2 adults and no children")

    def include_priority(self):
        for name in family_names:
            if self.detailed_info_attendees[name][0] < 3:
                if self.detailed_info_attendees[name][1] == 0:
                    self.detailed_info_attendees[name].append(0)
                else:
                    self.detailed_info_attendees[name].append(1)
            elif self.detailed_info_attendees[name][0] < 5:
                if self.detailed_info_attendees[name][1] == 0:
                    self.detailed_info_attendees[name].append(2)
                else:
                    self.detailed_info_attendees[name].append(3)
            else:
                if self.detailed_info_attendees[name][1] == 0:
                    self.detailed_info_attendees[name].append(4)
                else:
                    self.detailed_info_attendees[name].append(5)
        # print(self.detailed_info_attendees)  # for checking the priority

    def filter_priorities(self, p):
        global filter_names_priority
        filter_names_priority = []
        for name in family_names:
            if self.detailed_info_attendees[name][2] <= p:
                filter_names_priority.append(name)
        # print(filter_names_priority)  # for checking the name
        return filter_names_priority


# t = Party()
# for numb in range(0, len(family_names)):
#     t.add_attendees(family_names[numb], num_attendees[numb])
# t.detailed_attendees()
# t.check_and_resolve()
# t.get_total_attendees()
# t.filter_attendees()
# t.covid_changes()
# t.include_priority()
# t.filter_priorities(priority)

def exercise_2(inputs): # DO NOT CHANGE THIS LINE
    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.

    Output should be the name of the class.
    """
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
