%% Format Panes
format compact                                  %Compact the command line
clc                                             %Clear the command line
clear                                           %Clear the workspace                                   

%% Function to calculate instantaneous power and reduce exceedance
function power = power_calc(voltage,current,voltage_max,current_max)
if voltage > voltage_max
    voltage = voltage_max;
end
if current > current_max
    current = current_max;
end
power = voltage*current;
end

%% Function to calculate available energy
function energy = energy_calc(power,time)
energy = power*time;
end

%% Parameter Definition
voltage_max = 28;                               %Maximum voltage in Volts
current_max = 10;                               %Maximum current in Amps
power_out_max = 280;                            %Maximum power out in Watts

%% Test case
%input = [22,7,300; 40,7,60; 25,10,200; 10,4,600];
input = [0,7,300; 30,10,60; 28,10,200; 10,10,10];

%% Test instantaneous power calculation
power = zeros(length(input),1);
for i=1:length(input)
    power(i) = power_calc(input(i,1),input(i,2),voltage_max,current_max);
    %disp("The power output is "+power+" Watts")
end

%Test available energy calculator
energy_total = 0;
for i=1:length(input)
    energy = energy_calc(power(i),input(i,3));
    energy_total = energy_total + energy;
end

%% Energy Simplification
if energy_total >= 1000
    energy_total = energy_total/1000;
    if energy_total >= 1000
        energy_total = energy_total/1000;
        disp("You have "+energy_total+" Megajoules available for battery charging")
    else
        disp("You have "+energy_total+" Kilojoules available for battery charging")
    end
else
    disp("You have "+energy_total+" Joules available for battery charging")
end