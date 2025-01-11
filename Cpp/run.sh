#!/bin/bash

# Compile
cmake -S . -B build
cmake --build build

# Run
PROGRAM_NAME=$1
./build/$PROGRAM_NAME
