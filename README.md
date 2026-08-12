![](https://raw.githubusercontent.com/martinville/solarsynkv3/refs/heads/main/www/logo.png)


Integrate your Sunsynk account with Home Assistant for real-time solar energy monitoring. Track power generation, battery storage, and grid usage while enabling smart automations and custom alerts. Optimize energy efficiency, reduce costs, and stay in control with seamless remote access and intuitive dashboards.

## ☕ Support This Project

If you find this project useful, consider supporting it:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/mailmartins)

Or visit: [https://www.buymeacoffee.com/mailmartins](https://buymeacoffee.com/mailmartins)




## Documentation


[Installation](docs/INSTALL.md)

[Setting inverter settings](docs/INVERTER_SETTINGS.md)

## MQTT Discovery (optional)

SolarSynk can publish inverter data via **MQTT Discovery**. When enabled, every sensor gets a unique ID, is grouped under a device per inverter, and is manageable from the Home Assistant UI. Each inverter publishes to its own sub-topic. The broker is auto-detected from the Home Assistant MQTT service (Mosquitto add-on) and can be overridden manually. See [Installation](docs/INSTALL.md) for setup.
