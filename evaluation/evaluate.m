function [precision, recall, accuracy] = evaluate(I, T)
%matlab function to computes precision, recall, accuracy
% input : I: image(output of neural network)
%input : T: ground truth(computed by g_t.m) 
[szx, szy] = size(I);

TP = 0;
for i = 1:szx-2
    for j = 1:szy-2
        if T(i,j) == 0 && T(i,j) == I(i,j)
            TP  = TP + 1;
        end
    end
end

FP = 0;
for i = 1:szx-2
    for j = 1:szy-2
        if T(i,j) == 0 && T(i,j) ~= I(i,j)
            FP  = FP + 1;
        end
    end
end

FN = 0;
for i = 1:szx-2
    for j = 1:szy-2
        if T(i,j) ~= 0 &&  I(i,j) == 0
            FN  = FN + 1;
        end
    end
end

TN = 0;
for i = 1:szx-2
    for j = 1:szy-2
        if T(i,j) ~= 0 &&  I(i,j) ~= 0
            TN  = TN + 1;
        end
    end
end

precision = TP / (TP+FP);
recall = TP / (TP+FN);
accuracy = (TP+TN) / (TP+TN+FP+FN);

