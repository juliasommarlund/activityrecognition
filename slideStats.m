function [M, S, A, E] = slideStats( x, window, step)
% sliding: M-mean, S-std,  A-skewness, E-kurtosis

n=fix((length(x)-window)/step+1);
M=zeros(n,1);
S=zeros(n,1);
E=zeros(n,1);
A=zeros(n,1);

sum=0;
mean=0;
mean2=0;
mean3=0;
mean4=0;

for i=1:window
    sum = x(i);
    mean = mean + sum;
    sum = sum * x(i);
    mean2 = mean2 + sum;
    sum = sum * x(i);
    mean3 = mean3 + sum;
    sum = sum * x(i);
    mean4 = mean4 + sum;
end
mean=mean/window;
mean2=mean2/window;
mean3=mean3/window;
mean4=mean4/window;

M(1)= mean;
S(1)= (mean2-mean*mean)^0.5;
A(1)= (mean3-3*mean2*mean+2*mean*mean*mean) /S(1)^3;
E(1)= (mean4-4*mean3*mean+6*mean2*mean*mean-3*mean*mean*mean*mean) /S(1)^4 -3;

for i=0:n-2
    for k=1:step
        stepInd = i*step;    
        first = stepInd+k;
        last = stepInd+k+window;

    % recalculating means without previous element
        sum = x(first)/window;
        mean  = mean - sum;
        sum = sum*x(first);
        mean2 = mean2 - sum;
        sum = sum*x(first);
        mean3 = mean3 - sum;
        sum = sum*x(first);
        mean4 = mean4 - sum;

    % recalculating means with next element
        sum = x(last)/window;
        mean = mean + sum;
        sum = sum * x(last);
        mean2 = mean2 + sum;
        sum = sum * x(last);
        mean3 = mean3 + sum;
        sum = sum * x(last);
        mean4 = mean4 + sum;
    end

    M(i+2)= mean;
    S(i+2)= (mean2-mean*mean)^0.5;
    A(i+2)= (mean3-3*mean2*mean+2*mean*mean*mean) /S(i+2)^3;
    E(i+2)= (mean4-4*mean3*mean+6*mean2*mean*mean-3*mean*mean*mean*mean) /S(i+2)^4 -3;
end

end