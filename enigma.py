import csv

# The exception class for the case when the argument that contains mapping letters
# is not a string or does not contain the needed number of letters
class InvalidMapping(Exception):
    def __init__(self, message):
        super().__init__(message)
        
# The exception class for the case when a argument value is invalid
class InvalidInput(Exception):
    def __init__(self, message):
        super().__init__(message)

class PlugLead:
    def __init__(self, mapping):
        if type(mapping) is not str:
            raise InvalidMapping("Mapping should be string")
        mapping_letters = {c.upper() for c in mapping if c.upper() >="A" and c.upper()<="Z"}
        
        if len(mapping_letters)!=2:
            raise InvalidMapping("Mapping should consist of 2 letters.")
        
        (self.__first, self.__second) = [c.upper() for c in mapping]
        
    def get_first(self):
        return self.__first
    
    def get_second(self):
        return self.__second

    def encode(self, inpt):
        inpt_validation = {c.upper() for c in inpt if c.upper() >="A" and c.upper()<="Z"}
        if len(inpt_validation)!=1 or len(inpt)>1:
            raise InvalidInput("Input should be a single letter.")
        if inpt.upper()==self.__first:
            return self.__second
        if inpt.upper()==self.__second:
            return self.__first
        return inpt

class Plugboard:
    def __init__(self):
        self.__plug_leads = []
        self.__mapped_letters_set = set()
        
    #The class method that connects plugleads 
    def add(self, plug_lead):
        if type(plug_lead) is not PlugLead:
            raise InvalidInput("Argument should be a pluglead")
        
        if plug_lead.get_first() in self.__mapped_letters_set \
            or plug_lead.get_second() in self.__mapped_letters_set:
            raise InvalidInput("The PlugLead tries to connect already connected letter")

        self.__plug_leads.append(plug_lead)
        self.__mapped_letters_set.add(plug_lead.get_first())
        self.__mapped_letters_set.add(plug_lead.get_second())
        
    def encode(self, c):
        for plug_lead in self.__plug_leads:
            result = plug_lead.encode(c)
            if result!=c:
                return result
        return c
    
# Class that implements the Rotor 
class Rotor:
    def __init__(self, name, labels, mapping, notch):
        labels_set = {l for l in labels if l.upper()>="A" and l.upper()<="Z"}
        mapping_set = {m for m in labels if m.upper()>="A" and m.upper()<="Z"}
        if len(labels_set)!=26:
            raise InvalidInput("Labels data is invalid.")
        if len(mapping_set)!=26:
            raise InvalidInput("Mapping data is invalid.")
            
        self.__name = name
        self.__labels = "".join(labels)
        self.__mapping = "".join(mapping)
        self.__rotor_position = 0
        self.__ring_offset = 0
        self.__notch = notch.upper() if notch in labels_set else None
       
    #The class method that increments the rotor position to simulate the rotor rotation step 
    def rotate(self):
        self.__rotor_position = (self.__rotor_position + 1)%26
        
    #The class method used to set the ring settings offset
    def set_ring_offset(self, offset):
        if offset<1 or offset>26:
            raise InvalidInput("ring offset should be between 1 and 26")
        self.__ring_offset = offset-1
    
    #The class method used to set the rotor initial position
    def set_initial_position(self, position):
        if type(position) is not str or position.upper()<"A" or position.upper()>"Z":
            raise InvalidInput("Invalid position")
        self.__rotor_position = self.__labels.index(position)
      
    #The class method for swaping the letter when passing the rotor from right to left
    def encode_right_to_left(self, c):
        shift = (self.__rotor_position - self.__ring_offset)%26
        rotated_input_index = (self.__labels.index(c) + shift)%26
     
        relative_result = self.__mapping[rotated_input_index]

        result_index = (self.__labels.index(relative_result) - shift)%26
        
        result = self.__labels[result_index]
        return result
    
    #The class method for swaping the letter when passing the rotor from left to right
    def encode_left_to_right(self, c):
        shift = (self.__rotor_position - self.__ring_offset)%26
        
        rotated_input_index = (self.__labels.index(c) + shift)%26
        input_char=self.__labels[rotated_input_index]
        
        mapping_index = self.__mapping.index(input_char)
        relative_result = self.__labels[mapping_index]
        result_index = (self.__labels.index(relative_result) - shift)%26
        return self.__labels[result_index]
        
    
    def is_at_notch(self):
        return self.__notch is not None and self.__rotor_position==self.__labels.index(self.__notch)
            
    #The static method that builds a rotor according to the corresponding row in the settings of the csv file
    @staticmethod    
    def from_name(name):
        with open("rotor_settings.csv") as rotor_settings_csvfile:
            rotor_settings = csv.reader(rotor_settings_csvfile)
            settings = {row[0]:row[1:] for row in rotor_settings if row[0]==name or row[0]=="Label"}
            #print(settings[name])
            if len(settings)!=2:
                raise InvalidInput("Rotor name is invalid.")
            return Rotor(name, settings["Label"][0:26], settings[name][0:26], settings[name][-1])
            
class Reflector:
    def __init__(self, name, labels, mapping):
        labels_set = {l for l in labels if l.upper()>="A" and l.upper()<="Z"}
        mapping_set = {m for m in labels if m.upper()>="A" and m.upper()<="Z"}
        if len(labels_set)!=26:
            raise InvalidInput("Invalid labels data.")
        if len(mapping_set)!=26:
            raise InvalidInput("Invalid mapping data.")
            
        self.__name = name
        self.__labels = "".join(labels)
        self.__mapping = "".join(mapping)
        
    def encode(self, c):
        mapping_index = self.__labels.index(c)
        return self.__mapping[mapping_index]
        
    def get_name(self):
        return self.__name

    def get_mapping(self):
        return self.__mapping
            
    #The static method that builds a reflector according to the corresponding row in the settings of the csv file
    @staticmethod    
    def from_name(name):
        with open("rotor_settings.csv") as rotor_settings_csvfile:
            rotor_settings = csv.reader(rotor_settings_csvfile)
            settings = {row[0]:row[1:] for row in rotor_settings if row[0]==name or row[0]=="Label"}
            #print(settings[name])
            if len(settings)!=2:
                raise InvalidInput("Reflector name is invalid.")
            return Reflector(name, settings["Label"][0:26], settings[name][0:26])
    
    #The static method that build a reflector according to provided lettter mapping as argument 
    @staticmethod    
    def from_mapping(mapping):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        return Reflector("custom", letters, mapping)

# You will need to write more classes, which can be done here or in separate files, you choose.

# The class that abstracts the Rotors unit assembling all the rottors together
class RotorsUnit:
    def __init__(self, rightmostRotor, middleRotor, leftRotor, reflector, leftmostRotor=None):
        self.__rightmostRotor = rightmostRotor
        self.__middleRotor = middleRotor
        self.__leftRotor = leftRotor
        self.__leftmostRotor = leftmostRotor
        self.__reflector = reflector
    
    #The class method that swaps the letters passing through all the rotors.
    # It implements the rotors movement logic too.
    def encode(self, c):
        middle_rotated=False
        if self.__middleRotor.is_at_notch():
            self.__leftRotor.rotate()
            self.__middleRotor.rotate()
            middle_rotated=True
            
        if self.__rightmostRotor.is_at_notch() and not middle_rotated:
            self.__middleRotor.rotate()
            
        self.__rightmostRotor.rotate()
        
        result = self.__rightmostRotor.encode_right_to_left(c)
        
        result = self.__middleRotor.encode_right_to_left(result)
        result = self.__leftRotor.encode_right_to_left(result)
        if self.__leftmostRotor is not None:
            result = self.__leftmostRotor.encode_right_to_left(result)
        
        result = self.__reflector.encode(result)
        
        if self.__leftmostRotor is not None:
            result = self.__leftmostRotor.encode_left_to_right(result)
        
        result = self.__leftRotor.encode_left_to_right(result)
        result = self.__middleRotor.encode_left_to_right(result)
        result = self.__rightmostRotor.encode_left_to_right(result)
        
        return result
    
    
# The class that assemplies all Enigma components 
class EnigmaMachine:
    def __init__(self, plugboard, rotorsUnit):
        self.__plugboard = plugboard
        self.__rotorsUnit = rotorsUnit
        
    def encode(self, string):
        result = []
        for ch in string:
            result_char = self.__plugboard.encode(ch)
            result_char = self.__rotorsUnit.encode(result_char)
            result_char = self.__plugboard.encode(result_char)
            result.append(result_char)
            
        return "".join(result)
    
    #Static class method that creates an enigma machine with the specified rotors, reflector, 
    # ring settings starting positions and plugboard connected letter pairs
    @staticmethod    
    def build_machine(rotors, reflector, ringSettings, startingPositions, plugboardPairs):
        rotor_names_list = rotors.split()
        ring_settings_list = ringSettings.split()
        plugboard_pairs_list = plugboardPairs.split()
        
        leftRotor = Rotor.from_name(rotor_names_list[0])
        leftRotor.set_ring_offset(int(ring_settings_list[0]))
        leftRotor.set_initial_position(startingPositions[0])

        middleRotor = Rotor.from_name(rotor_names_list[1])
        middleRotor.set_ring_offset(int(ring_settings_list[1]))
        middleRotor.set_initial_position(startingPositions[1])

        rightRotor = Rotor.from_name(rotor_names_list[2])
        rightRotor.set_ring_offset(int(ring_settings_list[2]))
        rightRotor.set_initial_position(startingPositions[2])
        
        reflector = Reflector.from_name(reflector)
       
        plugboard = Plugboard()
        
        for plugboard_pair in plugboard_pairs_list:    
            plugboard.add(PlugLead(plugboard_pair))

        rotorsUnit=RotorsUnit(rightRotor, middleRotor, leftRotor, reflector)
        enigmaMachine = EnigmaMachine(plugboard, rotorsUnit)
        return enigmaMachine
    
    #Static class method that creates an enigma machine like build_machine method 
    #but the reflector is created with the reflector custom letters mapping specified using reflector_mapping
    #This is needed for creating custom reflector when the wires mapping is changed.
    @staticmethod    
    def build_machine_with_custom_reflector(rotors, reflector_mapping, ringSettings, startingPositions, plugboardPairs):
        rotor_names_list = rotors.split()
        ring_settings_list = ringSettings.split()
        plugboard_pairs_list = plugboardPairs.split()
        
        leftRotor = Rotor.from_name(rotor_names_list[0])
        leftRotor.set_ring_offset(int(ring_settings_list[0]))
        leftRotor.set_initial_position(startingPositions[0])

        middleRotor = Rotor.from_name(rotor_names_list[1])
        middleRotor.set_ring_offset(int(ring_settings_list[1]))
        middleRotor.set_initial_position(startingPositions[1])

        rightRotor = Rotor.from_name(rotor_names_list[2])
        rightRotor.set_ring_offset(int(ring_settings_list[2]))
        rightRotor.set_initial_position(startingPositions[2])
        
        reflector = Reflector.from_mapping(reflector_mapping)
       
        plugboard = Plugboard()
        
        for plugboard_pair in plugboard_pairs_list:    
            plugboard.add(PlugLead(plugboard_pair))

        rotorsUnit=RotorsUnit(rightRotor, middleRotor, leftRotor, reflector)
        enigmaMachine = EnigmaMachine(plugboard, rotorsUnit)
        return enigmaMachine


if __name__ == "__main__":
    pass
