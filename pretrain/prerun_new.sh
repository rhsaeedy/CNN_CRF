#!/bin/bash

TOOLS=/home/reza_rec/crfasrnn/caffe/build/tools
#WEIGHTS=/home/reza_rec/crfasrnn/caffe/examples/Gambier/models/convnet_iter_847.caffemodel
SOLVER=/home/reza_rec/crfasrnn/caffe/examples/Gambier/pretrain/solver_new.prototxt

$TOOLS/caffe train -solver $SOLVER #-weights $WEIGHTS 

