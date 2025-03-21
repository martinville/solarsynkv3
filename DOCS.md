![](https://github.com/martinville/solarsynkv3/blob/main/logo.png?raw=true)

## How It Works
SolarSynk retrieves solar system data from the cloud, where it's uploaded via your Sunsynk dongle. It has no direct physical connection to your inverter. 

*Please note that this add-on only provides sensor data, it does not include pre-built home assistant  cards to display the information.

## Getting Started
This add-on publishes sensor values to Home Assistant entities using the local API, requiring a long-lived access token.

### Creating a Long-Lived Access Token
Click your profile picture in the bottom left of the HA interface. Scroll down to the bottom and generate a long-lived token. The name isn't important for SolarSynk, but the token key is—be sure to copy and save it for later use.

![](https://github.com/martinville/solarsynkv3/blob/main/longlivetoken.png?raw=true)

### Add this respository to your Home Assistant add-on store
From the "Settings" menu item in Home Asstant's UI go to "Add-ons". In the bottom right-hand corner click "ADD-ON STORE". The in the right-hand top corner click the three dots and select "Repositories".
Paste the following repository link and click add then close https://github.com/martinville/solarsynkv3

![](https://github.com/martinville/solarsynkv3/blob/main/addrepo.png?raw=true)

Refresh the browser. Right at the bottom you should now see the "SolarSynk" add-on. Click it to open the into page, then click the "Install" button.

![](https://github.com/martinville/solarsynkv3/blob/main/addonavail.png?raw=true)

### Provide your Sunsynk.net credentials
After installing this add-on make sure you enter all the required information on the configuration page. Note if your intentions are to update a Home Assistant installtion with a different IP than the one where this addon is installed, you need to generate the long live token on the Home Assistant instance where entities will be updated. 
*NOTE: In some cases special characters in the password field may cause authentication issues. Also SolarSynk will not be able to connect to your sunsynk profile with MFA enabled.

*DO NOT USE localhost or 127.0.0.1 in the IP field, either use the actual IP or hostname. If you implemented a SSL certificate , its mandatory to use the hostname assigned to the certificate and not the IP. 
(This addon runs in a docker and cannot reach your home assistant network on the local loopback name or ip)

![](https://github.com/martinville/solarsynkv3/blob/main/settings.png)

In case you are unsure what your Sunsynk inverter's serial number is. Log into the synsynk.net portal and copy the serial number from the "Inverter" menu item.
For multiple inverters seperate the inverter serial numbers with a semi colon ; Example 123456;7890123

![](https://github.com/martinville/solarsynkv3/blob/main/sunserial.png)

Make sure you also populate the "HA_LongLiveToken" field with the long-lived token that you created earlier on.

### Start the script
After entering all of the required information you can go ahead and start the service script.

![](https://github.com/martinville/solarsynkv3/blob/main/scriptstarted.png?raw=true)

After starting the add-on, verify everything is working by clicking the "Log" tab. Scroll through the log to ensure sensor data is populated correctly. The log will display success or error messages based on the status of the integration.
