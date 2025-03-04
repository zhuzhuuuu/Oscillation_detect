function perturb_Pfsqr(t)
global Source_V Amplitude_V Frequency_V ...
       Source_P1 Amplitude_P1 Frequency_P1 pm01 ...
       Exc vref0 intstep VP_nos VQ_nos tcorr ...
       P0 Q0 PQ_std PQ Syn 

     Syn.pm0(Source_P1) = pm01*(1 + Amplitude_P1*sin(Frequency_P1*2*pi*t));
end