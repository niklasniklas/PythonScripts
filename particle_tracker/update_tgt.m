function [ tgt1 ] = update_tgt( tgt0, t, dt )
%UPDATE_TGT Summary of this function goes here
%   Detailed explanation goes here
%   index "i" - inertial coordinates

    [ax_i, ay_i] = getmanoeuvre(tgt0, t,dt);
    
    vx_i = ax_i*dt;
    vy_i = ay_i*dt;
    
    v = sqrt(vy_i*vy_i + vx_i*vx_i)
    % - kolla att v inte �r �ver vmax
    % ber�kna vx_e o vx_e utifr�n v o th
    % ber�kna x_e och y_e utifr�n x,y(old) o dt
    % ber�kna ny th utifr�n ny x_e o y_e
    % - se till s� att th �r inom 0 < th < 2pi
    
    tgt.x = ;
    tgt.y = ;
    tgt.th = ;
    tgt.v  = ;
    tgt.ax = ;
    tgt.ay = ;
    

    
    
    
    
%     tgt1 = tgt0;
%     tgt1.ax = tgt0.ax;
%     tgt1.ay = tgt0.ay;
%     tgt1.vx = tgt0.vx + tgt0.ax*dt;
%     tgt1.vy = tgt0.vy + tgt0.ay*dt;
%     tgt1.x = tgt0.x + tgt0.vx*dt;
%     tgt1.y = tgt0.y + tgt0.vy*dt;
    


end

