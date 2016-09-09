function [ tgt ] = init_tgt( )
%TGT1 Summary of this function goes here
%   Detailed explanation goes here
% public:
%    earth coord
    tgt.x = 0;
    tgt.y = 0;
    
% private:
%   earth coord
    tgt.th = 0;
    tgt.v  = 10;
%   inertial coord        >--->- ->x ^y
    tgt.ax = 0.2;
    tgt.ay = 0.2;
    
    tgt.v_max = 10;
    tgt.ax_max = 5;
    tgt.ay_max = 2;

end

