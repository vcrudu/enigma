# Enigma Machine Simulator

## Overview
This project is a Python-based simulation of the **Enigma Machine**, the cipher device used during World War II for encrypting and decrypting secret messages. The implementation includes classes for the various components of the Enigma Machine, including **Plugboard, Rotor, Reflector, and RotorsUnit**.

## Features
- **Plugboard Implementation**: Allows letter substitutions before and after passing through the rotors.
- **Rotors Implementation**: Supports rotor encryption logic, rotation mechanism, and ring settings.
- **Reflector Implementation**: Implements reflector wiring for bidirectional signal transformation.
- **Custom Rotor and Reflector Configuration**: Load rotor configurations from a CSV file.
- **Enigma Machine Simulation**: Simulates full Enigma encoding/decoding process.

## Prerequisites
- Python 3.x
- CSV file containing rotor configurations (e.g., `rotor_settings.csv`)

## Installation
Clone the repository and ensure Python 3.x is installed on your machine.
```bash
# Clone repository
git clone <repository_url>
cd <repository_directory>
```

## Usage
### Creating an Enigma Machine
You can create an **EnigmaMachine** instance using preconfigured rotors, reflector, and plugboard settings:
```python
from enigma_machine import EnigmaMachine

# Define the settings for the Enigma Machine
enigma = EnigmaMachine.build_machine(
    rotors="I II III",
    reflector="B",
    ringSettings="1 1 1",
    startingPositions="A A A",
    plugboardPairs="AB CD EF"
)

# Encrypt a message
message = "HELLO"
ciphertext = enigma.encode(message)
print("Encrypted Message:", ciphertext)
```
### Creating an Enigma Machine with a Custom Reflector
```python
enigma_custom = EnigmaMachine.build_machine_with_custom_reflector(
    rotors="I II III",
    reflector_mapping="YRUHQSLDPXNGOKMIEBFZCWVJAT",
    ringSettings="1 1 1",
    startingPositions="A A A",
    plugboardPairs="AB CD EF"
)
```

## Class Descriptions
### PlugLead
Handles individual plugboard connections.
```python
PlugLead(mapping: str)
PlugLead.encode(letter: str) -> str
```

### Plugboard
Manages multiple plug leads.
```python
Plugboard.add(plug_lead: PlugLead)
Plugboard.encode(letter: str) -> str
```

### Rotor
Handles rotor encryption and stepping mechanism.
```python
Rotor.from_name(name: str) -> Rotor
Rotor.rotate()
Rotor.encode_right_to_left(letter: str) -> str
Rotor.encode_left_to_right(letter: str) -> str
```

### Reflector
Implements reflector wiring for the Enigma machine.
```python
Reflector.from_name(name: str) -> Reflector
Reflector.from_mapping(mapping: str) -> Reflector
Reflector.encode(letter: str) -> str
```

### RotorsUnit
Combines all rotors into a single encoding unit.
```python
RotorsUnit.encode(letter: str) -> str
```

### EnigmaMachine
Encapsulates all components of the Enigma Machine.
```python
EnigmaMachine.build_machine(rotors, reflector, ringSettings, startingPositions, plugboardPairs)
EnigmaMachine.build_machine_with_custom_reflector(rotors, reflector_mapping, ringSettings, startingPositions, plugboardPairs)
```

## Exception Handling
The implementation includes custom exceptions for invalid inputs:
- **InvalidMapping**: Raised when incorrect plugboard mappings are used.
- **InvalidInput**: Raised when invalid characters or incorrect configurations are provided.

## CSV Configuration File
The `rotor_settings.csv` file should have rotor configurations in the following format:
```
Label,A,B,C,D,...,Z,Notch
I,E,K,M,F,L,G,D,Q,V,Z,N,T,O,W,Y,H,X,U,S,P,A,I,B,R,C,J
II,A,J,D,K,S,I,R,U,X,B,L,H,W,T,M,C,Q,G,Z,N,P,Y,F,V,O,E
...
```

## License
This project is open-source and available under the MIT License.

## Acknowledgments
This project is inspired by the historical **Enigma Machine** and its role in cryptography during WWII.

