clear all
%matlab script to evaluate the performance of trained
%model against ground truth
D = './castle_gt';
O1 = './castle_cnn';
O2 = './castle_crf';
SD = dir(fullfile(D,'*.png')); 
SO1 = dir(fullfile(O1,'*.png'));
SO2 = dir(fullfile(O2,'*.png'));
th = 120;

cnn_Precision = zeros(1,numel(SD));
cnn_Recall = zeros(1,numel(SD));
cnn_Accuracy = zeros(1,numel(SD));

crf_Precision = zeros(1,numel(SD));
crf_Recall = zeros(1,numel(SD));
crf_Accuracy = zeros(1,numel(SD));

for k = 1:numel(SD)
    F1 = fullfile(D,SD(k).name);
    F2 = fullfile(O1,SO1(k).name);
    F3 = fullfile(O2,SO2(k).name);
    I = imread(F1);
    [szx, szy, ~] = size(I);
    I = I(2:szx-1, 2:szy-1);
    I = im2uint8(I);
    T_cnn = imread(F2);
    T_crf = imread(F3);
    T_cnn = g_t(T_cnn, th);
    T_crf = g_t(T_crf, th);
    [p1, r1, a1] = evaluate(I,T_cnn);
    [p2, r2, a2] = evaluate(I,T_crf);
    cnn_Precision(k) = p1;
    cnn_Recall(k) = r1;
    cnn_Accuracy(k) = a1;
    crf_Precision(k) = p2;
    crf_Recall(k) = r2;
    crf_Accuracy(k) = a2;
end


acc_cnn = mean(cnn_Accuracy);
pre_cnn = mean(cnn_Precision);   
rec_cnn = mean(cnn_Recall);

acc_crf = mean(crf_Accuracy);
pre_crf = mean(crf_Precision);   
rec_crf = mean(crf_Recall);


