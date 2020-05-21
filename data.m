AccXYZ = readmatrix('Accelerometer-Total.csv', 'HeaderLines',1);

t_AccX = AccXYZ(:,3);
t_AccY = AccXYZ(:,4);
t_AccZ = AccXYZ(:,5);
l = AccXYZ(:,6);

n = 6;
Wn = 0.3;

[b,a] = butter(n,Wn);

b_AccX = filter(b,a,t_AccX);
b_AccY = filter(b,a,t_AccY);
b_AccZ = filter(b,a,t_AccZ);


window = 128;
step = 64;

% sliding: M-mean, S-std,  A-skewness, E-kurtosis
[l_M, S, A, E] = slideStats(l, window, step);

[M_b_AccX, S_b_AccX, A_b_AccX, E_b_AccX] = slideStats(b_AccX, window, step);
[M_b_AccY, S_b_AccY, A_b_AccY, E_b_AccY] = slideStats(b_AccY, window, step);
[M_b_AccZ, S_b_AccZ, A_b_AccZ, E_b_AccZ] = slideStats(b_AccZ, window, step);

[M_t_AccX, S_t_AccX, A_t_AccX, E_t_AccX] = slideStats(t_AccX, window, step);
[M_t_AccY, S_t_AccY, A_t_AccY, E_t_AccY] = slideStats(t_AccY, window, step);
[M_t_AccZ, S_t_AccZ, A_t_AccZ, E_t_AccZ] = slideStats(t_AccZ, window, step);

writematrix([M_b_AccX S_b_AccX A_b_AccX E_b_AccX M_b_AccY S_b_AccY A_b_AccY E_b_AccY M_b_AccZ 
    S_b_AccZ A_b_AccZ E_b_AccZ M_t_AccX S_t_AccX A_t_AccX E_t_AccX M_t_AccY S_t_AccY A_t_AccY 
    E_t_AccY M_t_AccZ S_t_AccZ A_t_AccZ E_t_AccZ l_M],'data.csv')
