function [ th ] = get_th( x1, x2, y1, y2 )
%GET_TH Summary of this function goes here
%   Detailed explanation goes here
    if(y2>=y1)&&(x2>=x1)
        th = atan((y2-y1)/(x2-x1));         %fprintf('I   : ');
    elseif(y2<=y1)&&(x2>=x1)
        th = 2*pi-atan((y1-y2)/(x2-x1));    %fprintf('II  : ');
    elseif(y2>=y1)&&(x2<=x1)
        th = pi - atan((y2-y1)/(x1-x2));    %fprintf('III : ');
    else
        th = pi + atan((y1-y2)/(x1-x2));    %fprintf('IIII: ');
    end
end

%
%       _________
%      /    |    \
%     / III |  I  \
%     |_____|_____|
%     |     |     |
%     \ IIII|  II /
%      \    |    /
%       ---------
