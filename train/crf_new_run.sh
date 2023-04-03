#!/bin/bash

TOOLS=/home/reza_rec/crfasrnn/caffe/build/tools
WEIGHTS=/home/reza_rec/crfasrnn/caffe/examples/Gambier/models/new_iter_10000.caffemodel
SOLVER=/home/reza_rec/crfasrnn/caffe/examples/Gambier/train/crf_new_solver.prototxt

$TOOLS/caffe train -solver $SOLVER -weights $WEIGHTS 

