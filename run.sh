#!/usr/bin/with-contenv bashio
set +e

while :
do
CONFIG_PATH=/data/options.json

sunsynk_user=""
sunsynk_pass=""
sunsynk_serial=""

sunsynk_user="$(bashio::config 'sunsynk_user')"
sunsynk_pass="$(bashio::config 'sunsynk_pass')"
sunsynk_serial="$(bashio::config 'sunsynk_serial')"
Refresh_rate="$(bashio::config 'Refresh_rate')"

VarCurrentDate=$(date +%Y-%m-%d)

clear

python3 /application.py



echo "All Done! Waiting " $Refresh_rate " seconds to rinse and repeat."
sleep $Refresh_rate
done
