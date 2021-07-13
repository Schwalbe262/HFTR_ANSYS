for i = 1:100
    
    [N1(i),N2(i),space1(i),space2(i),l1(i),l2(i),h1(i),w1(i)] = random_pick();
    
end


M = horzcat(N1.',N2.',space1.',space2.',l1.',l2.',h1.',w1.');
M = round(M);

csvwrite('input_parameter_v1.csv',M)
    
    
    
    
    



%%

function value = random_variable(min,max)

    value = (max-min)*rand()+min;

end


function [N1,N2,space1,space2,l1,l2,h1,w1] = random_pick()

   
    d1 = 6.54;
    move_tx = d1 + 3;
    
    

    N1 = random_variable(1,9);
    N2 = random_variable(1,9);
    N = max(N1,N2);
    l1 = random_variable(5,50);
    space2 = random_variable(20,60);
    space1 = random_variable(5,ceil(space2-d1-2));
    l2 = random_variable(space2+20,100);
    h1 = random_variable(ceil((N-1)*move_tx+2*d1),200);
    w1 = random_variable(30,200);

%     output = round([N1,N2,space1,space2,l1,l2,h1,w1]);

end