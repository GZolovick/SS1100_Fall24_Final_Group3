# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems
## Results and Responses at the Bottom of the Page

### Assignment
- **Instructions**: Work in groups of four to complete the steps outlined in the project instructions.
- **Submission**: All of your submission will go here in this repository, to include this README file to hold your writeup.

### Procedure
#### Preparation
- Employ programming skills to solve problems related to spacecraft subsystems.
- Develop code and responses to tasks in various sections.
- Experience working with code and collaborating on a coding project.

#### Requirements
1. Complete all tasks listed in each section, paying attention to the Evaluation subsections.
2. Use MatLab to complete at least one of the tasks.
3. Submit the project using GitHub, replacing the content of this README file with your writeup and presentation of the work.

#### Subsystems and Tasks
Reaction Control Subsystem (RCS): Malfunction detection and velocity change calculation.\
Thermal Control Subsystem (TCS): Temperature control function.\
Attitude Control Subsystem (ACS): Attitude determination and rotation calculations.\
Command and Data Handling (C&DH): Command parsing and routing.\
Electrical Power Subsystem (EPS): Power budget analysis and battery charging calculations.\
Remote Sensing Payload: Data ingestion, radiance to reflectance conversion, and image rescaling.


# Results:
## Reaction Control Subsystem:
### Check Results:
Firing a Thruster for 5 seconds with flow rate of 0.02 kg/s and exhaust velocity of 1000 m/s.\
Thruster 1 is within limits.\
Velocity change is 0.2 m/s.

Firing a Thruster for 3 seconds with flow rate of 0.06 kg/s and exhaust velocity of 1000 m/s.\
Thruster 2 exceeded Flow Rate by 0.01 kg/s.\
Velocity change is 0.36 m/s.

Firing a Thruster for 10 seconds with flow rate of 0.05 kg/s and exhaust velocity of 2000 m/s.\
Thruster 3 is within limits.\
Velocity change is 2 m/s.

### Check Plus Results:
Thruster 1 is within limits.\
Thruster 2 is within limits.\
Thruster 3 is within limits.\
Velocity change is 2.4 m/s in the X direction, 0.48 m/s in the Y direction, and 0.12 m/s in the Z direction.

## Thermal Control Subsystem:
### Check Results:
Example of TCS check results labeled under TCS_example.png in the TCS file. For the test the current temperature was set to 30.0 and the target temperature was set to 25.0.

### Check Plus Results:

## Attitude Control Subsystem:
### Check Results:
Console outputs from the final rotation/iteration of each test orientation copied below:

Orientation-1: (100,200,300)
Required orientation change is: x -0.13709187396308664, y -0.05393778647729164, z -0.07416445640626534
Current orientation is: x 100.13709187396309, y 200.0539377864773, z 300.07416445640627
New orientation is: x 99.99649485471485, y 199.9986209264452, z 299.9981037738621

Orientation-2: (0,0,0)
Required orientation change is: x 0.01163753616780372, y 0.14572219201423664, z 0.09917204734302265
Current orientation is: x -0.01163753616780372, y -0.14572219201423664, z -0.09917204734302265
New orientation is: x -0.00037988244060010654, y -0.004756788821427382, z -0.003237259059026984

Orientation-3: (3,30,300)
Required orientation change is: x -3.7297130154927345, y -1.8378296018370008, z 2.7026905909367542
Current orientation is: x 33.729713015492734, y 31.837829601837, z 297.29730940906325
New orientation is: x 29.938735329380137, y 29.969811611578617, z 300.044394688855

### Check Plus Results:
Check plus requirements met and shown. Both original and v2 ofadc_script_CHECKPLUS utilized the calculate_rotation as a separate imported module.

## Command and Data Handling:
### Check Results: 
('Electrical Power Subsystem', 'BATTERY CHARGE MODE', 0.0)
('Attitude Control Subsystem', 'SAFE MODE', -1.0)
Error processing command 'RCS:INVALID:0': Invalid command format. Expected format: SUBSYSTEM:COMMAND:PARAMETER

### Check Plus Results:
('Electrical Power Subsystem', 'BATTERY_CHARGE_MODE', 0)
('Attitude Control Subsystem', 'SAFE_MODE', 1)
Error processing command 'RCS:INVALID:0': Invalid command format. Expected format: SUBSYSTEM:COMMAND:PARAMETER

## Electrical Power Subsystem:
### Check Results:
Voltage = 25V, Current = 10A, Time = 3600s.\
The power output is 250 Watts.\
You have 900 Kilojoules available for battery charging.

Voltage = 30V, Current = 8A, Time = 1800s.\
The power output is 224 Watts.\
You have 403.2 Kilojoules available for battery charging.

Voltage = 15V, Current = 12A, Time = 7200s.\
The power output is 150 Watts.\
You have 1.08 Megajoules available for battery charging.

### Check Plus Results:
[(22,7,300), (40,7,60), (25,10,200), (10,4,600)].\
You have 131.96 Kilojoules available for battery charging.

[(0,7,300), (30,10,60), (28,10,200), (10,10,10)].\
You have 73.8 Kilojoules available for battery charging.

## Remote Sensing Payload:
### Check Results:
Image files saved in the Payload folder titled RGB_output.jpg and RGB_output_CHECK.png.

### Check Plus Results:
Image file saved in the Payload folder titled RGB_converted_CHECKPLUS.png. Console output messages are shown in the screenshot titled Payload_CHECKPLUS_Console_Output.jpg.

# Questions for Writeup:

## Q1: Experience collaborating:
Wright: It was very helpful to be able to distribute the load of each section, and the range of experience is helpful but I feel abashed about my lack of experience. 

Staut: Having multiple people work asynchronously was helpful in getting a fresh set of eyes on particular problems that I'd hit a wall on and needed to come back to. Other group members were able to jump in and help continue the efforts where I had gotten stuck.

## Q2: Most Challanging Section:
Wright: Payload seems to have taken up all group member's bandwidth trying to convert the data to meet the stipulations.

Staut: Concur with payload as the hardest section. Took me several tries to get a good method, and then still took ChatGPT to help me through error troubleshooting.

## Q3: Generative AI:
ACS: after making a functioning code framework that met project requirements, ChatGPT 4o suggestions were used to create a singular function that could be used as a console command to change the satellite orientation rather than making in-line changes to the code itself. Full details and prompt given to ChatGPT notated at the beginning of adc_script_CHECKPLUS_v2.

TCS: After writing the code, trying to run it, and getting several errors, I put it into ChatGPT with the prompt “Find the errors in this Python code”. I had to input the code into ChatGPT several times with the same prompt due to it not finding all the errors the first time or creating new errors. Once the code was working, I would put in back into ChatGPT to fix the errors I made while attempting to add more stuff to the code. 

C&DH: After trying to put the information into a format I could read and coming up with constant errors, Copilot helped organize the information and give the required and run through a few times to get to something that could work. I tried to think of different things a person may make mistakes on and added those stipulations in, like casing or misspelling. It expedited the process of trial and error to an astounding level.

Payload: ChatCPT 4o was utilized as an error handling/troubleshooting aid, which enabled the successful completion of CheckPlus requirements after the group had collective difficulty in formatting the image data and successfully saving the output image. Full details are notated within the code payload_CHECKPLUS.py.

## Q4: Other Resources Used: 
TCS: I used Stack Overflow to learn how to create floats and to make sure I was doing the while loop correctly. I also used it to correct the errors in my f" string.

Payload: StackOverflow was used for examples on how to save image files and which libraries were required to do so. We ended up using PIL to enable image saving after having issues importing the cv2 library as some StackOverflow users suggested.

## Q5: Improvements for Future Iterations:

Staut: Can't think of any, but we should put at least one item here...
