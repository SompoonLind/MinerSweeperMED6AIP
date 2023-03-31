class Statemachine

    def state_one(self):            ### "<" less then ### ### ">" greater then ###
                                    #receive variable chromosome from genetice_algo() and check what float is genereated
        if child <= 0.49:
            return #moveblankdown
        elif child < 0.5:
            return #moveblankright

    def state_two(self):

        if child <= 0.32:
            return #moveblankdown
        elif 0.33 >= child <= 0.65:
            return #moveblankleft
        elif child >= 0.66:
            return #moveblankright

    def state_three(self):

        if child <= 0.49:
            return #moveblankdown
        elif child >= 0.50:
            return #moveblankleft

    def state_four(self):
        if child <= 0.32:
            return #moveblankup
        elif 0.33 >= child <= 0.65:
            return #moveblankdown
        elif child >= 0.66:
            return #moveblankright

    def state_five(self):
        if child <= 0.24:
            return #moveblankup
        elif 0.25 >= child >= 0.49:
            return #moveblankdown
        elif 0.50 >= child >= 0.74:
            return #moveblankleft
        elif child >= 0.75:
            return #moveblankright

    def state_six(self):
        if child <= 0.32:
            return #moveblankup
        elif 0.33 <= child >= 0.65:
            return #moveblankdown
        elif child >= 0.66:
            return #moveblanright

    def state_seven(self):
        if child >= 0.49:
            return #moveblankup
        elif child <= 0.50:
            return #movechilddown

    def state_eight(self):
        if child >= 0.32:
            return #moveblankup
        elif 0.33 <= child >= 0.65:
            return #moveblankdown
        elif child <= 0.66:
            return #moveblankright

    def state_nine(self):
        if child >= 0.49:
            return #moveblankup
        elif child <= 0.50:
            return #moveblankleft
