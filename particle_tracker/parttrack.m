%%

clear all;
close all;

delta_t = 0.01;
time = 40;
time_vec = (0:delta_t:time-delta_t);

part1 = struct( 'x',zeros(1,time/delta_t), ...
                'y',zeros(1,time/delta_t), ...
                'v',zeros(1,time/delta_t), ...
                'th',zeros(1,time/delta_t), ...
                'ath',zeros(1,time/delta_t), ...
                'vx',zeros(1,time/delta_t), ...
                'vy',zeros(1,time/delta_t), ...
                'ax',zeros(1,time/delta_t), ...
                'ay',zeros(1,time/delta_t));

msl = part1;            
            
part1.x(1) = 0;
part1.y(1) = 0;
part1.v(1) = 1.5;
part1.th(1) = 0.78;
part1.ath(1) = 0.5;

msl.x(1) = -5;
msl.y(1) = -5;
msl.v(1) = 1.4;
msl.th(1) = get_th(msl.x(1),part1.x(1),msl.y(1),part1.y(1));
msl.ath(1) = 0;

% part1.vx(1) = 1;
% part1.vy(1) = 0;
% part1.ax(1) = 0;
% part1.ay(1) = 0;



for ii = 1 : (time/delta_t)
    if(part1.th(ii)>2*pi)
        part1.th(ii) = part1.th(ii)-2*pi;
    elseif(part1.th(ii)<0)
        part1.th(ii) = part1.th(ii)+2*pi;
    end
    
    if(msl.th(ii)>2*pi)
        msl.th(ii) = msl.th(ii)-2*pi;
    elseif(msl.th(ii)<0)
        msl.th(ii) = msl.th(ii)+2*pi;
    end
        
    
    part1.ax(ii) = part1.ath(ii)*cos(part1.th(ii)+pi/2);
    part1.ay(ii) = part1.ath(ii)*sin(part1.th(ii)+pi/2);
    part1.vx(ii) = part1.v(ii)*cos(part1.th(ii));
    part1.vy(ii) = part1.v(ii)*sin(part1.th(ii));

    msl.ax(ii) = msl.ath(ii)*cos(msl.th(ii)+pi/2);
    msl.ay(ii) = msl.ath(ii)*sin(msl.th(ii)+pi/2);
    msl.vx(ii) = msl.v(ii)*cos(msl.th(ii));
    msl.vy(ii) = msl.v(ii)*sin(msl.th(ii));
    
% ---    
    if(ii ~= time/delta_t)
        part1.v(ii+1)   = part1.v(ii);
        part1.ath(ii+1) = 0; %part1.ath(ii)*0.9999;       
        part1.th(ii+1)  = sin(ii*delta_t/3)%part1.th(ii) + asin((part1.ath(ii)*delta_t)/part1.v(ii));

        msl.v(ii+1)   = msl.v(ii);
        msl.ath(ii+1) = msl.ath(ii);       
        msl.th(ii+1)  = get_th(msl.x(ii),part1.x(ii),msl.y(ii),part1.y(ii));
        
       % fprintf('%g, x1= %g, x2= %g, y1= %g, y2= %g\n',msl.th(ii+1)*180/pi, msl.x(ii), part1.x(ii), msl.y(ii), part1.y(ii));

        part1.vx(ii+1) = part1.vx(ii) + part1.ax(ii)*delta_t;
        part1.vy(ii+1) = part1.vy(ii) + part1.ay(ii)*delta_t;
        part1.x(ii+1) = part1.x(ii) + part1.vx(ii)*delta_t;
        part1.y(ii+1) = part1.y(ii) + part1.vy(ii)*delta_t;

        msl.vx(ii+1) = msl.vx(ii) + msl.ax(ii)*delta_t;
        msl.vy(ii+1) = msl.vy(ii) + msl.ay(ii)*delta_t;
        msl.x(ii+1) = msl.x(ii) + msl.vx(ii)*delta_t;
        msl.y(ii+1) = msl.y(ii) + msl.vy(ii)*delta_t;

    end
    
    if(mod(ii,10) == 0)
         figure(100); axis([-15 100 -15 15]); hold on; 
         plot(part1.x(ii),part1.y(ii),'b'); 
         plot(msl.x(ii),msl.y(ii),'r');
        % -- plot angle to tgt --
%         figure(100);  
%         plot(part1.x(ii),part1.y(ii),'bo'); axis([-15 15 -15 15]); hold on;
%         ang = msl.th(ii);
%         rho = 0:0.1:sqrt((part1.x(ii)-msl.x(ii))^2+(part1.y(ii)-msl.y(ii))^2);
%         [xx,yy] = pol2cart(ang,rho);
%         plot(xx+msl.x(1),yy+msl.y(1),'r'); hold off;
    end

end


figure(1); plot(part1.x,part1.y,'b'); hold on; plot(msl.x,msl.y,'r'); xlabel('x'); ylabel('y'); axis([-15 40 -15 15]);
figure(2); plot(time_vec,part1.vx,'r'); xlabel('t'); ylabel('vx');
figure(3); plot(time_vec,part1.vy,'r'); xlabel('t'); ylabel('vy');
figure(4); plot(time_vec,part1.ax,'r'); xlabel('t'); ylabel('ax');
figure(5); plot(time_vec,part1.ay,'r'); xlabel('t'); ylabel('ay');

figure(6); 
subplot(3,1,1); plot(time_vec,part1.ath,'b'); xlabel('t'); ylabel('ath');
subplot(3,1,2); plot(time_vec,part1.th,'r'); xlabel('t'); ylabel('th');
subplot(3,1,3); plot(time_vec,part1.v,'k'); xlabel('t'); ylabel('v');

figure(7);
vv = sqrt(part1.vx.^2+part1.vy.^2);
aa = sqrt(part1.ax.^2+part1.ay.^2);
subplot(2,1,1); plot(time_vec,vv,'b'); xlabel('t'); ylabel('v - calc');
subplot(2,1,2); plot(time_vec,aa,'b'); xlabel('t'); ylabel('a - calc');


 
% figure(2); plot(part1.vx,time_vec,'r'); hold on;
% plot(part1.vy,time_vec,'g'); hold on;
% plot(part1.ax,time_vec); hold on;
% plot(part1.ay,time_vec); hold on;
