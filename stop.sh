#!/bin/sh -x
echo STOPPING....
echo Stoping All Python processes...;
top -b -n1 | grep python3;
top -b -n1| grep python3 | grep -v "grep python3" | awk '{print $1}' | sudo xargs kill -9;

echo ✓;
sleep 2;
echo Stoping Node Server...;
top -b -n1| grep node;
top -b -n1| grep node | grep -v "grep node" | awk '{print $1}' | sudo xargs kill -9;
echo ✓;
sleep 2;
