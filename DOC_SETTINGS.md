# Sending Settings back to inverter

### Intro
The Solarsynk Home Assistant integration enables you to send settings to your inverter, with support currently limited to updating battery settings.

### How it works
After each loop, when the integration retrieves the various values, it will also check the entity named [solarsynkv3_YOUR_INVERTER_SERIAL_NUMBER_settings]. If valid settings are found, it will post them back to the SunSynk Portal.

When running the integration for the first time, you will see an error message indicating that the entity does not exist, along with instructions on how to create it. However, the integration will also attempt to automatically create the entity. If the automatic creation fails, you can follow the instructions in the log to manually create it.

#### Below is a list of all settings that can be updated
{
    "absorptionVolt": "57.6",
    "battMode": "-1",
    "batteryCap": "100",
    "batteryEfficiency": "99",
    "batteryEmptyV": "45",
    "batteryImpedance": "8",
    "batteryLowCap": "35",
    "batteryLowVolt": "47.5",
    "batteryMaxCurrentCharge": "40",
    "batteryMaxCurrentDischarge": "70",
    "batteryOn": "1",
    "batteryRestartCap": "50",
    "batteryRestartVolt": "52",
    "batteryShutdownCap": "20",
    "batteryShutdownVolt": "46",
    "bmsErrStop": "0",
    "disableFloatCharge": "0",
    "equChargeCycle": "90",
    "equChargeTime": "0",
    "equVoltCharge": "57.6",
    "floatVolt": "55.2",
    "genChargeOn": "0",
    "genSignal": "1",
    "generatorBatteryCurrent": "40",
    "generatorForcedStart": "0",
    "generatorStartCap": "30",
    "generatorStartVolt": "49",
    "gridSignal": "1",
    "lithiumMode": "0",
    "lowNoiseMode": "8000",
    "lowPowerMode": "0",
    "safetyType": "0",
    "sdBatteryCurrent": "40",
    "sdChargeOn": "1",
    "sdStartCap": "30",
    "sdStartVol": "undefined",
    "sdStartVolt": "49",
    "signalIslandModeEnable": "0",
    "sn": "123456",
    "tempco": "0"
}

## Setting the Settings Entity Value with a Properly Formatted String
Each setting must be separated by a semicolon (;).

### Example of a Single Setting:
"batteryCap": "100"

### Example of Updating Multiple Settings Simultaneously:
"batteryCap": "100";"batteryLowCap": "35"


