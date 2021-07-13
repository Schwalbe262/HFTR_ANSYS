clear; clc;

data = readtable('Data_v1.csv');

%%

l1 = table2array(data(:,1)).*1e-3;
l2 = table2array(data(:,2)).*1e-3;
h1 = table2array(data(:,3)).*1e-3;
w1 = table2array(data(:,4)).*1e-3;

Lm_sim = table2array(data(:,5));
Lm_sim = table2array(data(:,5));

per = 3500;

%%

N1 = 4;

Req = (5.*l1+2.*l2+2.*h1)./(2.*l1.*w1)/per;
Lm_math = N1^2./Req;


%%

plot(Lm_sim,"LineWidth",3)
hold on;
grid on;
plot(Lm_math*1e-3,"LineWidth",3)

ylim([0 3])

legend("시뮬레이션","수식")

%%

plot(Lm_sim./(Lm_math*1e-3),"LineWidth",3)


%%

