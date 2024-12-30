# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems
## Results and Responses at the Bottom of the Page

### Staut	Wright	Zolovick	Donnelly

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
Example of TCS check results labeled under TCS_example.png in the TCS file.\
For the test the current temperature was set to 30.0 and the target temperature was set to 25.0.

## Attitude Control Subsystem:
### Check Results:
Console outputs from the final rotation/iteration of each test orientation copied below:

Orientation-1: (100,200,300).\
Required orientation change is: x -0.13709187396308664, y -0.05393778647729164, z -0.07416445640626534.\
Current orientation is: x 100.13709187396309, y 200.0539377864773, z 300.07416445640627.\
New orientation is: x 99.99649485471485, y 199.9986209264452, z 299.9981037738621.

Orientation-2: (0,0,0).\
Required orientation change is: x 0.01163753616780372, y 0.14572219201423664, z 0.09917204734302265.\
Current orientation is: x -0.01163753616780372, y -0.14572219201423664, z -0.09917204734302265.\
New orientation is: x -0.00037988244060010654, y -0.004756788821427382, z -0.003237259059026984.

Orientation-3: (3,30,300).\
Required orientation change is: x -3.7297130154927345, y -1.8378296018370008, z 2.7026905909367542.\
Current orientation is: x 33.729713015492734, y 31.837829601837, z 297.29730940906325.\
New orientation is: x 29.938735329380137, y 29.969811611578617, z 300.044394688855.

### Check Plus Results:
Check plus requirements met and shown. Both original and v2 ofadc_script_CHECKPLUS utilized the calculate_rotation as a separate imported module.

## Command and Data Handling:
### Check Results: 
('Electrical Power Subsystem', 'BATTERY CHARGE MODE', 0.0).\
('Attitude Control Subsystem', 'SAFE MODE', -1.0).\
Error processing command 'RCS:INVALID:0': Invalid command format. Expected format: SUBSYSTEM:COMMAND:PARAMETER.

### Check Plus Results:
('Electrical Power Subsystem', 'BATTERY_CHARGE_MODE', 0).\
('Attitude Control Subsystem', 'SAFE_MODE', 1).\
Error processing command 'RCS:INVALID:0': Invalid command format. Expected format: SUBSYSTEM:COMMAND:PARAMETER.

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

Zolovick: Primary distribution was with each person leading up one section. Collaboration occured through a signal chat communicating sticking points and brainstorming solutions. Remote sensing was somewhat more difficult and we worked on that in a more collaborative setting, with different people making adjustments to the program on Github.

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

EPS: I used several MATLAB forums to figure our the best way to handle the check-plus tuples in MATLAB.

Payload: StackOverflow was used for examples on how to save image files and which libraries were required to do so. We ended up using PIL to enable image saving after having issues importing the cv2 library as some StackOverflow users suggested.

## Q5: Improvements for Future Iterations:

Recommend that future iterations integrate this style of project throughout the course. The "space application" of this assignment made the course feel very practical and it would have been interesting if the labs and final project were baked into a wholistic product. This could be done in the form of taking one of the subsections and making it a working code over the semster, each week adding a new functionality taught that week.

# Instructor Comments

### ADC
In your adc_script_CHECKPLUS.py, you might have been able to use the "tolerance_check(current_orientation, desired_orientation) == True" line as the condition of the While statement. In other words, instead of having to Break out of it when it was found to be true, placing that statement after the While at the top of the loop. You'd have to change the True/False output of the function to make it work, but it would be a bit more compact.

### C&DH
Interesting use of the regular expressions module to search for the subsystem type and commands. In your subsequent error checking in C&DH.py, you also could have streamlined things by having an if...elif...elif...else construction that checked the three parts of the command sequence against their respective error checking blocks.
Finally, just be careful with using special characters in script names. In this case, you would be unable to import the two scripts from this section as modules in other code, as each contains an ampersand "&" character. Windows doesn't care when you're just saving it as a file, but Python would were you to try and use it elsewhere.

### TCS
Some of the formatting of comments is a bit difficult to read - generally, you'd indent them at the same level as the code you are referencing as to make it easier to read. It also wasn't inserted into the thermal_control.py script as specified in the instructions, so I wasn't able to evaluate if your code worked in that setting.

### EPS
Very creative and interesting code. Particularly like the conversion to change SI units.

### RCS
Good inclusion of Matlab here - you might have been the only group to use Matlab on more than one subsystem. Your multiple if....end constructions could have been merged into one longer if..elseif...elseif...end, but that's trivial. The function itself is succinct, and your organization of the code is great even if Matlab isn't always as user friendly as Python.

### Payload
This one can definitely be tricky, but these types of operations are very common in image processing tasks like you may encounter in AI/ML projects. Cleaning up each image ( preprocessing) so that it matches the specifications is important to making sure that bad data doesn't get passed into the model.

### Github
Good collaboration in the repository; I'm just a bit worried that some of the pull requests didn't get completed and that there might be code you meant to have in the Main still waiting to be merged. It's good practice to close out branches completely before moving on. Great writeup and feedback; apprecaite the idea about including this project into earlier parts of the course. Also seems like while GenAI tools were helpful, you still ended up having to collaborate and troubleshoot as a group on the Payload task (which is great!)