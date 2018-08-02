#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
NOFCPU=$(cat /proc/cpuinfo | grep processor | wc -l)
START='/sys/devices/system/cpu/cpu'
END='/cpufreq/scaling_governor'
declare -a ORIGOVS
for ((I=0;I < NOFCPU;I++))
{
	j=$START$I$END
	ORIGOVS[$I]=$(cat $j)
}
for ((I=0;I < NOFCPU;I++))
{
	j=$START$I$END
	echo performance > $j
}
python "$DIR/bomberman.py"
for ((I=0;I < NOFCPU;I++))
{
	j=$START$I$END
	echo ${ORIGOVS[$I]} > $j
}
