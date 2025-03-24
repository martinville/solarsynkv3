# Sending Settings back to inverter

### Intro
The Solarsynk Home Assistant integration enables you to send settings to your inverter, with support currently limited to updating battery settings.

### How it works
After each loop when the integration is fetching the various values it will also check the entity named [solarsynkv3_YOUR_INVERTER_SERIAL_NUMBER_settings] 

