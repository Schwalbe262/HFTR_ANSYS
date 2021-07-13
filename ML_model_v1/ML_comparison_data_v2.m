%% 2021 07 13
% from about 1000 ML data
% comparison with pass 10 HFSS simulation data (random parameter)
clear; clc;

LineWidth = 3;

%%
data = readtable('ML_comparison_data_v2.csv');

% data sequence : Lmt, Lmr, Llk, Rt, Rr

ML_data = table2array(data(:,5:9));
HFSS_data = table2array(data(:,10:14));



%% Lmt

plot(ML_data(:,1),"LineWidth",LineWidth)
hold on;
grid on;
plot(HFSS_data(:,1),"LineWidth",LineWidth)
legend("ML","HFSS")

ylabel("L_m [mH]")


%% Llk

plot(ML_data(:,3),"LineWidth",LineWidth)
hold on;
grid on;
plot(HFSS_data(:,3),"LineWidth",LineWidth)
legend("ML","HFSS")
ylabel("L_{lk} [uH]")

