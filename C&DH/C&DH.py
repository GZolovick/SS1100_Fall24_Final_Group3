# The following code segment is based off of the prompt in Microsoft Copilot to
#   "can you write an python script of command parsing and routing using the information above? (being table 7)",
#   "please allow it to read lowercase versions of the subsystems as well"
#   "for this code, please have add a response for errors in the print:" for the a previous version where it gave error messages outside the print statement
#   and then under the framework for the tasks and eval, and then I had it integrate the dictionary written for this becasue I did not see it earlier. 

import re

def parse_command(command_str):
    # Define the command dictionary
    command_dict = {
        "Reaction Control Subsystem": {
            "Code": "RCS",
            "Commands": {"CMD01":['THRUST_X', range(0,60)],
                         "CMD02":['THRUST_Y', range(0,60)],
                         "CMD03":['THRUST_Z', range(0,60)],
                         "CMD04":['SAFE_MODE', {0, 1}]}
        },
        "Thermal Control Subsystem": {
            "Code": "TCS",
            "Commands": {"CMD01":['HEATER_ON', {0, 1}],
                         "CMD02":['HEATER_OFF', {0, 1}],
                         "CMD03":['VENT_OPEN_RADIATOR', {0, 1}],
                         "CMD04":['TEMP_SETPOINT', range(-30,60)]}
        },
        "Attitude Control Subsystem": {
            "Code": "ACS",
            "Commands": {"CMD01":['ROTATE_X', range(-360,360)],
                         "CMD02":['ROTATE_Y', range(-360,360)],
                         "CMD03":['ROTATE_Z', range(-360,360)],
                         "CMD04":['SAFE_MODE', {0, 1}]}
        },
        "Command & Data Handling": {
            "Code": "CDH",
            "Commands": {"CMD01":['TRANSMIT_HIGH', {0, 1}],
                         "CMD02":['TRANSMIT_LOW', {0, 1}],
                         "CMD03":['RECEIVE_MODE',{0, 1}],
                         "CMD04":['SAFE_MODE', {0,1}]}
        },
        "Telemetry, Tracking, & Command": {
            "Code": "TTC",
            "Commands": {"CMD01":['TRANSMIT_MODE', {0,1}],
                         "CMD02":['RECEIVE_MODE', {0,1}],
                         "CMD03":['TRACKING_MODE', {0,1}],
                         "CMD04":['SAFE_MODE', {0,1}]}
        },
        "Electrical Power Subsystem": {
            "Code": "EPS",
            "Commands": {"CMD01":['BATTERY_CHARGE_MODE', {0,1}],
                         "CMD02":['POWER_ON_MODULE', {0,1,2,3,4}],
                         "CMD03":['POWER_OFF_MODULE', {0,1,2,3,4}],
                         "CMD04":['VOLTAGE_SETPOINT', range(0,120)]}
        },
        "Payload System 1": {
            "Code": "PL1",
            "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                         "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                         "CMD03":['CALIBRATE_SENSOR', {0,1}],
                         "CMD04":['SAFE_MODE', {0,1}]}
        },
        "Payload System 2": {
            "Code": "PL2",
            "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                         "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                         "CMD03":['CALIBRATE_SENSOR', {0,1}],
                         "CMD04":['SAFE_MODE', {0,1}]}
        }
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
        for subsystem, details in command_dict.items():
            if subsystem_code == details['Code']:
                commands = details['Commands']
                if command_code not in commands:
                    raise ValueError("Invalid command code")
                
                # Validate parameter
                command_detail = commands[command_code]
                if isinstance(command_detail[1], set):
                    if int(parameter) not in command_detail[1]:
                        raise ValueError(f"Parameter must be one of {command_detail[1]}")
                elif isinstance(command_detail[1], range):
                    if int(parameter) not in command_detail[1]:
                        raise ValueError(f"Parameter must be in range {command_detail[1]}")
                
                # Get the full subsystem name and command description
                subsystem_name = subsystem
                command_description = command_detail[0]

                return subsystem_name, command_description, int(parameter)

        raise ValueError("Invalid subsystem code")
    
    except ValueError as e:
        print(f"Error processing command '{command_str}': {e}")
        return None

# Tested inputs for various subsystems
print(parse_command('EPS:CMD01:0'))
print(parse_command('ACS:CMD04:-1'))
print(parse_command('RCS:INVALID:0'))
print(parse_command('ttc:CMD02:0'))
print(parse_command('TcS:CMD02:0'))
print(parse_command('PL1:CMD03:1'))
print(parse_command('PL2:CMD02:-5'))
print(parse_command('CDH:CMD02:1'))
print(parse_command('CDH:CMD03:1'))
