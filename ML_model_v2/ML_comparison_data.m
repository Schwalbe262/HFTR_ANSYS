%% 2021 07 13
% from about 1000 ML data
% comparison with pass 10 HFSS simulation data (random parameter)
clear; clc;

LineWidth = 3;

%%
data1 = readtable('solution_v1');
data2 = readtable('solution_v2');

%%


% data sequence : Lmt, Lmr, Llk, Rt, Rr

ML_data1 = table2array(data1(:,2:6));
ML_data2 = table2array(data2(:,2:6));



%% Lmt

plot(ML_data1(:,1),"LineWidth",LineWidth)
hold on;
grid on;
plot(ML_data2(:,1),"LineWidth",LineWidth)
legend("ML1","ML2")

ylabel("L_m [mH]")


%% Llk

plot(ML_data1(:,3),"LineWidth",LineWidth)
hold on;
grid on;
plot(ML_data2(:,3),"LineWidth",LineWidth)
legend("ML1","ML2")

ylabel("L_{lk} [uH]")

