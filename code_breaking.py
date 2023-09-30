from enigma import *

"""
Code 1
Code: DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ
Crib: SECRETS
Rotors: Beta Gamma V
Reflector: Unknown
Ring settings: 04 02 14
Starting positions: MJM
Plugboard pairs: KI XN FL
"""
def code1():
    reflectors = ["A","B","C"]
    for reflector in reflectors:
        enigmaMachine = EnigmaMachine.build_machine("Beta Gamma V", reflector, "04 02 14", "MJM", "KI XN FL")
        result = enigmaMachine.encode("DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ")
        if result.find("SECRETS")>-1:
            print("Code 1")
            print("Code: DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ")
            print("Crib: SECRETS")
            print("Rotors: Beta Gamma V")
            print("Reflector - " + reflector)
            print("Ring settings: 04 02 14")
            print("Starting positions: MJM")
            print("Plugboard pairs: KI XN FL")
            print("Decoded message - " + result)
            print("\n")
            break

        
"""
Code 2
Code: CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH
Crib: UNIVERSITY
Rotors: Beta I III
Reflector: B
Ring settings: 23 02 10
Starting positions: Unknown
Plugboard pairs: VH PT ZG BJ EY FS
"""

def code2():
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    startingPositionsList = [l1+l2+l3 for l1 in letters for l2 in letters for l3 in letters]

    for startingPositions in startingPositionsList:
        enigmaMachine = EnigmaMachine.build_machine("Beta I III", "B", "23 02 10", startingPositions, "VH PT ZG BJ EY FS")
        result = enigmaMachine.encode("CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH")
        if result.find("UNIVERSITY")>-1:
            print("Code 2")
            print("Code: CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH")
            print("Crib: UNIVERSITY")
            print("Rotors: Beta I III")
            print("Reflector: B")
            print("Ring settings: 23 02 10")
            print("Starting positions - " + startingPositions)
            print("Plugboard pairs: VH PT ZG BJ EY FS")
            print("Decoded message - " + result)
            print("\n")
            break
        
"""
Code 3
Code: ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY
Crib: THOUSANDS
Rotors: Unknown but restricted (see above)
Reflector: Unknown
Ring settings: Unknown but restricted (see above)
Starting positions: EMY
Plugboard pairs: FH TS BE UQ KD AL
"""

def code3():
    rotorsSource = ["II", "IV", "Beta", "Gamma"]
    rotorsList = [ro1+" "+ro2+" "+ro3 for ro1 in rotorsSource \
              for ro2 in rotorsSource for ro3 in rotorsSource if ro1!=ro2 and ro2!=ro3 and ro3!=ro1]

    ringSettingsSource = [r for r in range(1,27) if len([d for d in str(r) if int(d)%2==1])==0]
    ringSettingsList = [str(r1)+" "+str(r2)+" "+str(r3) for r1 in ringSettingsSource for r2 in ringSettingsSource for r3 in ringSettingsSource]

    reflectors = ["A","B","C"]

    for reflector in reflectors:
        for ringSettings in ringSettingsList:
                for rotors in rotorsList:
                    enigmaMachine = EnigmaMachine.build_machine(rotors, reflector, ringSettings, "EMY", "FH TS BE UQ KD AL")
                    result = enigmaMachine.encode("ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY")
                    if result.find("THOUSANDS")>-1:
                        print("Code 3")
                        print("Code: ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY")
                        print("Crib: THOUSANDS")
                        print("Rotors: " + rotors)
                        print("Reflector:" + reflector)
                        print("Ring settings: " + ringSettings)
                        print("Starting positions: EMY")
                        print("Plugboard pairs: FH TS BE UQ KD AL")
                        print("Decoded message - " + result)
                        print("\n")
                        break


"""
Code 4
Code: SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW
Crib: TUTOR
Rotors: V III IV
Reflector: A
Ring settings: 24 12 10
Starting positions: SWU
Plugboard pairs: WP RJ A? VF I? HN CG BS
"""

def code4():
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    plugboardPairsInitial = "WP RJ A?1 VF I?2 HN CG BS"
    exclusion = [li for li in plugboardPairsInitial if li!="?" and li!=" "]
    missing_letters = [(l1,l2) for l1 in letters for l2 in letters if l1 not in exclusion and l2 not in exclusion and l1!=l2]

    for missing_letter in missing_letters:
        enigmaMachine = EnigmaMachine.build_machine("V III IV", "A", "24 12 10", "SWU", "WP RJ A"+missing_letter[0]+" VF I"+missing_letter[1]+" HN CG BS")
        result = enigmaMachine.encode("SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW")
        if result.find("TUTOR")>-1 and result.find("THESEEXAMPLES")>-1:
            print("Code 4")
            print("Code: SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW")
            print("Crib: TUTOR")
            print("Rotors: V III IV")
            print("Reflector: A")
            print("Ring settings: 24 12 10")
            print("Starting positions: SWU")
            print("Plugboard pairs with unknowns: WP RJ A? VF I? HN CG BS")
            print("Plugboard pairs: WP RJ AT VF IK HN CG BS")
            print("first missing letter - " + missing_letter[0])
            print("second missing letter - " + missing_letter[1])
            print("Decoded message - " + result)
            print("\n")
        
     
    
"""
Code 5
Code: HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX
Crib: the name of a social media website/platform
Rotors: V II IV
Reflector: Unknown and non-standard (see above)
Ring settings: 06 18 07
Starting positions: AJL
Plugboard pairs: UG IE PO NX WT
"""
def code5():
    def swap_mapping(mapping, l1, l2):
        result = mapping.replace(l1, "1")
        result = result.replace(l2, "2")
        result = result.replace("1", l2)
        result = result.replace("2", l1)
        return result

    initial_reflectors = [Reflector.from_name("A"),Reflector.from_name("B"),Reflector.from_name("C")]
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for initial_reflector in initial_reflectors:
        mapping = initial_reflector.get_mapping()

        for swap in ((l1,l2,l3,l4) \
                 for l1 in letters for l2 in letters for l3 in letters for l4 in letters if len(set([l1,l2,l3,l4]))==4):
            #print(swap)
            #print(mapping)
            new_mapping = swap_mapping(mapping, swap[0],swap[1])
            new_mapping = swap_mapping(new_mapping, swap[2],swap[3])
            #print(new_mapping)
            enigmaMachine = EnigmaMachine.build_machine_with_custom_reflector("V II IV", new_mapping, "06 18 07", "AJL", "UG IE PO NX WT")
            result = enigmaMachine.encode("HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX")
            if result.find("thename".upper())>-1:
                print("Code 5")
                print("Code: HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX")
                print("Crib: the name of a social media website/platform")
                print("Rotors: V II IV")
                print("Original reflector - " + initial_reflector.get_mapping())
                print("Changed reflector - " + new_mapping)
                print("Ring settings: 06 18 07")
                print("Starting positions: AJL")
                print("Plugboard pairs: UG IE PO NX WT")
                print("Decoded message - " + result)
                print("\n")
                break
                
if __name__ == "__main__":
    code1()
    code2()
    code3()
    code4()
    #code5()
                    
