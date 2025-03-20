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

Refresh the browser. Right at the bottom you should now see the "SolarSynk" add-on. Simply click it then click "Install"

