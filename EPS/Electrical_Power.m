%Format Panes
format compact                                  %Compact the command line
clc                                             %Clear the command line
clear                                           %Clear the workspace                                   

%Function to calculate instantaneous power and reduce exceedance
function power = power_calc(voltage,current,voltage_max,current_max)
if voltage > voltage_max
    voltage = voltage_max;
end
if current > current_max
    current = current_max;
end
power = voltage*current;
end

%Function to calculate available energy
%input Power and Time
%output Energy
%Energy Storage = Power * Time
function energy = energy_calc(power,time)
energy = power*time;
end

%Parameter Definition
voltage_max = 28;                               %Maximum voltage in Volts
current_max = 10;                               %Maximum current in Amps
power_out_max = 280;                            %Maximum power out in Watts

%Test case
voltage = 15;                                   %Voltage in Volts
current = 12;                                   %Current in Amps
time = 7200;                                    %Time in Seconds

%Test instantaneous power calculation
power = power_calc(voltage,current,voltage_max,current_max);
disp("The power output is "+power+" Watts")

%Test available energy calculator
energy = energy_calc(power,time);
if energy >= 1000
    energy = energy/1000;
    if energy >= 1000
        energy = energy/1000;
        disp("You have "+energy+" Megajoules available for battery charging")
    else
        disp("You have "+energy+" Kilojoules available for battery charging")
    end
else
    disp("You have "+energy+" Joules available for battery charging")
end