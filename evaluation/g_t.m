function [GT] = g_t(T, th)
   T(T > th) = 255;
   T(T ~= 255) = 0; 
   GT = T;
end