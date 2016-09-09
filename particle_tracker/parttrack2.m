%% parttrack2.m

clear all;
close all;

delta_t = 0.01;
time = 10;
time_vec = (0:delta_t:time-delta_t);

part1 = struct( 'x',zeros(1,time/delta_t), ...
                'y',zeros(1,time/delta_t), ...
                'v',zeros(1,time/delta_t), ...
                'th',zeros(1,time/delta_t));

            
part1.x(1) = 0;
part1.y(1) = 0;
part1.v(1) = 0;
part1.th(1) = 0.78;

            
part1.ax(1) = 0;
part1.ay(1) = 0;
part1.vx(1) = 1;
part1.vy(1) = 0;


for ii = 2 : time/delta_t
    part1.ax(ii) = part1.ax(ii-1)*0.9;
%    part1.ay(ii) = part1.ay(ii-1)*0.9;
    part1.ay(ii) = sin(time_vec(ii));
   
    part1.vx(ii) = part1.vx(ii-1) + part1.ax(ii-1)*delta_t;
    part1.vy(ii) = part1.vy(ii-1) + part1.ay(ii-1)*delta_t;
    
    part1.x(ii) = part1.x(ii-1) + part1.vx(ii-1)*delta_t;
    part1.y(ii) = part1.y(ii-1) + part1.vy(ii-1)*delta_t;
end


figure(1); plot(part1.x,part1.y); xlabel('x'); ylabel('y'); axis([-15 15 -15 15]);
figure(2); plot(time_vec,part1.vx,'r'); xlabel('t'); ylabel('vx');
figure(3); plot(time_vec,part1.vy,'r'); xlabel('t'); ylabel('vy');
figure(4); plot(time_vec,part1.ax,'r'); xlabel('t'); ylabel('ax');
figure(5); plot(time_vec,part1.ay,'r'); xlabel('t'); ylabel('ay');


% figure(2); plot(part1.vx,time_vec,'r'); hold on;
% plot(part1.vy,time_vec,'g'); hold on;
% plot(part1.ax,time_vec); hold on;
% plot(part1.ay,time_vec); hold on;
