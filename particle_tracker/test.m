%%
clear all;
close all;

th = 0 * pi/180;
r = 10;
x0 = -1;
y0 = -1;

x = ([x0:(r*cos(th)-x0)/10:10])
y = ([y0:(r*sin(th)-y0)/10:10])
% x = ([x0:(r*cos(th)-x0)/10:r*cos(th)])
% y = ([y0:(r*sin(th)-y0)/10:r*sin(th)])

plot(x(1:10),y(1:10)); axis([-4 4 -3.5 3.5]);

%%
clear all;
close all;
th = 360 * pi/180;
r = 0:1:5;

[x,y] = pol2cart(th,r);

plot(x,y); axis([-4 4 -3.5 3.5]);

%%

clear all;
close all;
clc;

fig = figure;
x = 0;
y = 0;

plot(x,y,'xr'); axis([-4 4 -4 4]);
hold on;

fig;
for ii=0.0:0.1:4.0
    plot(ii,ii,'xr');
    drawnow;
    pause(1/20);
end


%%
clear all;
close all;
clc;

dt = 0.1;
tgt = init_tgt();
msl1 = init_msl();

fig = figure; axis([-1 15 -1 15]); hold on;

for t=1:dt:10
    tgt = update_tgt(tgt, t, dt);
    %msl1 = update_msl1(msl1,tgt,dt);
    %clf(fig);
    plot(tgt.x, tgt.y,'.r');
    drawnow;
    pause(1/20);
end


