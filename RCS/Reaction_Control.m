%Format Panes
format compact                                  %Compact the command line
clc                                             %Clear the command line
clear                                           %Clear the workspace                                   

%Function to check if thruster limits are exceeded
function [thruster_name, exceeded_parameter,exceedence] = ...
    limit_verification(thruster_name,flow_rate,exhaust_velocity,...
    thrust_max,flow_rate_max,exhaust_velocity_max)

    exceeded_parameter = "none";
    
    thrust = flow_rate * exhaust_velocity;

    if thrust > thrust_max
        exceeded_parameter = "Thrust";
        exceedence = thrust - thrust_max;
        disp(thruster_name+" exceeded "+exceeded_parameter+" by "+exceedence+" N");
    end
    if flow_rate > flow_rate_max
        exceeded_parameter = "Flow Rate";
        exceedence = flow_rate - flow_rate_max;
        disp(thruster_name+" exceeded "+exceeded_parameter+" by "+exceedence+" kg/s");
    end
    if exhaust_velocity > exhaust_velocity_max
        exceeded_parameter = "Exhaust Velocity";
        exceedence = exhaust_velocity - exhaust_velocity_max;
        disp(thruster_name+" exceeded "+exceeded_parameter+" by "+exceedence+" m/s");
    end
    if exceeded_parameter == "none"
        exceedence = 0;
        disp(thruster_name+" is within limits")
    end
end

%Function to calculate change in velocity
%Input mass flow rate, effective exhaust velocity, time
%Output change in velocity

function velocity_change = maneuver_event(flow_rate, exhaust_velocity,time,mass_spacecraft)
    thrust = flow_rate * exhaust_velocity;
    velocity_change = thrust * time / mass_spacecraft;
    disp("Velocity change is "+velocity_change+" m/s")
end

%Parameter Definition
thrust_max = 100;                               %Maximum thrust in Newtons
flow_rate_max = 0.05;                           %Maximum flow rate in Kilograms/Second
exhaust_velocity_max = 2000;                    %Maximum exhaust velocity in Meters/Second
mass_spacecraft = 500;                          %Mass of spacecraft in Kilograms

%Test case
thruster_name = "Thruster 3";                  %Name of thruster
flow_rate = .05;                               %Thruster flow rate in Kilograms/Second
exhaust_velocity = 2000;                       %Thruster exhaust velocity in Meters/Second
time = 10;                                      %Time of thrust in Seconds

%Test limit verification
[thruster_name, exceeded_parameter,exceedence] = ...
    limit_verification(thruster_name,flow_rate,exhaust_velocity,...
    thrust_max,flow_rate_max,exhaust_velocity_max);

%Test maneuver event calculation
velocity_change = maneuver_event(flow_rate, exhaust_velocity,time,mass_spacecraft);