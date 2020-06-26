#!/usr/bin/env bash
for i in `adb devices | grep "devices" |awk `{print $1}``;
do
   echo "执行{$i}设备"
   uuid=$i
   pytest test_appiu_grid.py &
done
