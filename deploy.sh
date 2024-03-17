#! /bin/bash

set -x

ROBOT_SSH_TARGET="robot@ev3dev.local"

mkdir -p ~/mnt/ev3home
sshfs "$ROBOT_SSH_TARGET:/home/robot" ~/mnt/ev3home
trap "fusermount -u ~/mnt/ev3home" EXIT

rsync -a --filter ':- .gitignore' ./ ~/mnt/ev3home/robotics/
ssh "$ROBOT_SSH_TARGET" "cd /home/robot/robotics && brickrun -r -- pybricks-micropython main.py"

