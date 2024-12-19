# The following code segment is based off of the prompt in Microsoft Copilot to
#   "can you write an python script of command parsing and routing using the information above? (being table 7)",
#   "please allow it to read lowercase versions of the subsystems as well"

import re

def parse_command(command_str):
    # Define the command dictionary
    subsystems = {
        'RCS': ('Reaction Control Subsystem', {
            'CMD01': 'THRUST X',
            'CMD02': 'THRUST Y',
            'CMD03': 'THRUST Z',
            'CMD04': 'SAFE MODE'
        }),
        'TCS': ('Thermal Control Subsystem', {
            'CMD01': 'HEATER ON',
            'CMD02': 'HEATER OFF',
            'CMD03': 'VENT OPEN RADIATOR',
            'CMD04': 'TEMP SETPOINT'
        }),
        'ACS': ('Attitude Control Subsystem', {
            'CMD01': 'ROTATE X',
            'CMD02': 'ROTATE Y',
            'CMD03': 'ROTATE Z',
            'CMD04': 'SAFE MODE'
        }),
        'CDH': ('Command & Data Handling', {
            'CMD01': 'TRANSMIT HIGH',
            'CMD02': 'TRANSMIT LOW',
            'CMD03': 'RECEIVE MODE',
            'CMD04': 'SAFE MODE'
        }),
        'TTC': ('Telemetry, Tracking, & Command', {
            'CMD01': 'TRANSMIT MODE',
            'CMD02': 'RECEIVE MODE',
            'CMD03': 'TRACKING MODE',
            'CMD04': 'SAFE MODE'
        }),
        'EPS': ('Electrical Power Subsystem', {
            'CMD01': 'BATTERY CHARGE MODE',
            'CMD02': 'POWER ON MODULE',
            'CMD03': 'POWER OFF MODULE',
            'CMD04': 'VOLTAGE SETPOINT'
        }),
        'PL1': ('Payload System 1', {
            'CMD01': 'START DATA ACQUISITION',
            'CMD02': 'STOP DATA ACQUISITION',
            'CMD03': 'CALIBRATE SENSOR',
            'CMD04': 'SAFE MODE'
        }),
        'PL2': ('Payload System 2', {
            'CMD01': 'START DATA ACQUISITION',
            'CMD02': 'STOP DATA ACQUISITION',
            'CMD03': 'CALIBRATE SENSOR',
            'CMD04': 'SAFE MODE'
        })
    }

    try:
        # Verify the format of the command string
        pattern = r'^(RCS|TCS|ACS|CDH|TTC|EPS|PL1|PL2):(CMD\d{2}):(.+)$'
        match = re.match(pattern, command_str, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid command format. Expected format: SUBSYSTEM:COMMAND:PARAMETER")

        subsystem_code, command_code, parameter = match.groups()

        # Convert subsystem code to uppercase to match dictionary keys
        subsystem_code = subsystem_code.upper()

        # Verify the subsystem and command
        if subsystem_code not in subsystems:
            raise ValueError("Invalid subsystem code")
        if command_code not in subsystems[subsystem_code][1]:
            raise ValueError("Invalid command code")

        # Ensure parameter is numeric, including negatives and decimals
        try:
            parameter_value = float(parameter)
        except ValueError:
            raise ValueError("Parameter must be a numeric value")

        # Get the full subsystem name and command description
        subsystem_name = subsystems[subsystem_code][0]
        command_description = subsystems[subsystem_code][1][command_code]

        return subsystem_name, command_description, parameter_value

    except ValueError as e:
        print(f"Error processing command '{command_str}': {e}")
        return None

# Tested inputs for EPS, ACS, and RCS
print(parse_command('EPS:CMD01:0'))
print(parse_command('ACS:CMD04:-1'))
print(parse_command('RCS:INVALID:0'))

# Test with other subsystems
print(parse_command('ttc:CMD02:0'))
print(parse_command('TcS:CMD02:0'))
print(parse_command('PL1:CMD03:1'))
print(parse_command('PL2:CMD02:-5'))
print(parse_command('CDH:CMD02:1'))
