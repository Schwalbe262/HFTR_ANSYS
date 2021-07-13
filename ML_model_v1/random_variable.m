l1 = random_variable(10,50);
l2 = random_variable(50,100);
h1 = random_variable(50,150);
w = random_variable(30,200);

round([l1,l2,h1,w])


%%

function value = random_variable(min,max)

    value = (max-min)*rand()+min;

end