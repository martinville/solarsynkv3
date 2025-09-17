# Inverter Settings

The Solarsynk Home Assistant integration enables you to send settings to your inverter, with support currently limited
to updating battery and system mode settings.

## How it works

After each loop, when the integration retrieves the various values, it will check the entity named
`solarsynkv3_YOUR_INVERTER_SERIAL_NUMBER_settings`. If valid settings are found, they will be posted back to the SunSynk
Portal.

Once the settings are posted, the settings entity will be cleared to prevent the integration from repeatedly uploading
the same settings in a continuous loop.

When running the integration for the first time, you will see an error message indicating that the entity does not
exist, along with instructions on how to create it. However, the integration will also attempt to automatically create
the entity. If the automatic creation fails, you can follow the instructions in the log to manually create it.

## List of updatable settings

#### Battery settings 
```json
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
```

#### System mode settings 

| Name              | SunSynk Setting Page | Field                  | Explanation                                                     |
|:------------------|:---------------------|:-----------------------|:----------------------------------------------------------------|
| safetyType        | Unknown              | Unknown                | Unknown                                                         |
| battMode          | Battery Settings     | Batt Type              | Don't change this                                               |   
| solarSell         | System Mode          | Solar Export           | 0 is off, 1 is on                                               | 
| pvMaxLimit        | System Mode          | Inverter Power Limiter |
| energyMode        | System Mode          | Energy Pattern         | 0 is priority battery, 1 is priority load                       |
| peakAndVallery    | Unknown              | Unknown                | Unknown                                                         |
| sysWorkMode       | System Mode          | Work Mode              | 0 is Selling First, 1 is Zero Export, 2 is Limited to Home      |
| sellTime1         | System Mode          | Time 1                 |                                                                 |
| sellTime2         | System Mode          | Time 2                 |                                                                 |
| sellTime3         | System Mode          | Time 3                 |                                                                 |
| sellTime4         | System Mode          | Time 4                 |                                                                 |
| sellTime5         | System Mode          | Time 5                 |                                                                 |
| sellTime6         | System Mode          | Time 6                 |                                                                 |
| sellTime1Pac      | System Mode          | Power 1                |                                                                 |
| sellTime2Pac      | System Mode          | Power 2                |                                                                 |
| sellTime3Pac      | System Mode          | Power 3                |                                                                 |
| sellTime4Pac      | System Mode          | Power 4                |                                                                 |
| sellTime5Pac      | System Mode          | Power 5                |                                                                 |
| sellTime6Pac      | System Mode          | Power 6                |                                                                 |
| cap1              | System Mode          | Battery SoC 1          |                                                                 |
| cap2              | System Mode          | Battery SoC 2          |                                                                 |
| cap3              | System Mode          | Battery SoC 3          |                                                                 |
| cap4              | System Mode          | Battery SoC 4          |                                                                 |
| cap5              | System Mode          | Battery SoC 5          |                                                                 |
| cap6              | System Mode          | Battery SoC 6          |                                                                 |
| sellTime1Volt     | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| sellTime2Volt     | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| sellTime3Volt     | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| sellTime4Volt     | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| sellTime5Volt     | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| sellTime6Volt     | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| zeroExportPower   | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| solarMaxSellPower | Advanced Settings    | Max Solar Power        |                                                                 |
| mondayOn          | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| tuesdayOn         | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| wednesdayOn       | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| thursdayOn        | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| fridayOn          | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| saturdayOn        | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| sundayOn          | Unknown              | Unknown                | Doesn't seem to correspond to any setting in the SunSynk portal |
| time1on           | System Mode          | Grid Charge: Time 1    | Charge from Grid during period, 0 is off, 1 is on               |
| time2on           | System Mode          | Grid Charge: Time 2    | Charge from Grid during period, 0 is off, 1 is on               |
| time3on           | System Mode          | Grid Charge: Time 3    | Charge from Grid during period, 0 is off, 1 is on               |
| time4on           | System Mode          | Grid Charge: Time 4    | Charge from Grid during period, 0 is off, 1 is on               |
| time5on           | System Mode          | Grid Charge: Time 5    | Charge from Grid during period, 0 is off, 1 is on               |
| time6on           | System Mode          | Grid Charge: Time 6    | Charge from Grid during period, 0 is off, 1 is on               |
| genTime1on        | System Mode          | Gen Charge: Time 1     | Charge from other generation during period, 0 is off, 1 is on   |
| genTime2on        | System Mode          | Gen Charge: Time 2     | Charge from other generation during period, 0 is off, 1 is on   |
| genTime3on        | System Mode          | Gen Charge: Time 3     | Charge from other generation during period, 0 is off, 1 is on   |
| genTime4on        | System Mode          | Gen Charge: Time 4     | Charge from other generation during period, 0 is off, 1 is on   |
| genTime5on        | System Mode          | Gen Charge: Time 5     | Charge from other generation during period, 0 is off, 1 is on   |
| genTime6on        | System Mode          | Gen Charge: Time 6     | Charge from other generation during period, 0 is off, 1 is on   |

## Setting Format

Note that you cannot mix battery settings with system mode settings. i.e. `"batteryCap": "100";"time2on":"true"` will
not work.

### Version 1

Each setting must be separated by a semicolon (;) Names and values must be separated by a colon (:), and enclosed in
double quotes.

#### Battery settings example of a single setting:

`"batteryCap": "100"`

#### Example to update multiple battery settings simultaneously:

`"batteryCap": "100";"batteryLowCap": "35"`

#### System mode settings example of a single setting:

`"time2on":"true"`

#### Example to update multiple system mode settings simultaneously:

Below will turn on the timer switch (peakAndVallery) and at the same time enable grid charge Timer 2 and Timer 3

`"peakAndVallery": "1";"time2on":"true";"time3on":"true"`

### Version 2

The concept of version 2 is to allow both a more concise formatting, and to allow for shorter setting names, to allow
more settings to be updated within the HomeAssistant maximum length of 255 characters.

To identify a version 2 setting value, the value must be prefixed with `v2#`.

Each setting key and value must be separated by a colon (:), and each setting must be separated by a semicolon (;). For
eaxmple:

`v2#setting1:value1;setting2:value2;setting3:value3`

Quotes are not required around names or values.

You can use either the full name of the setting, or the abbreviated name, as listed in the table below.

So the following are equivalent:

`v2#peakAndVallery:1`

and

`v2#pav:1`

#### Short Names

| Name              | Short Name |
|:------------------|:-----------|
| safetyType        | st         |
| battMode          | bm         |   
| solarSell         | ss         | 
| pvMaxLimit        | pml        |
| energyMode        | em         |
| peakAndVallery    | pav        |
| sysWorkMode       | swm        |
| sellTime1         | s1         |
| sellTime2         | s2         |
| sellTime3         | s3         |
| sellTime4         | s4         |
| sellTime5         | s5         |
| sellTime6         | s6         |
| sellTime1Pac      | s1p        |
| sellTime2Pac      | s2p        |
| sellTime3Pac      | s3p        |
| sellTime4Pac      | s4p        |
| sellTime5Pac      | s5p        |
| sellTime6Pac      | s6p        |
| cap1              | c1         |
| cap2              | c2         |
| cap3              | c3         |
| cap4              | c4         |
| cap5              | c5         |
| cap6              | c6         |
| sellTime1Volt     | s1v        |
| sellTime2Volt     | s2v        |
| sellTime3Volt     | s3v        |
| sellTime4Volt     | s4v        |
| sellTime5Volt     | s5v        |
| sellTime6Volt     | s6v        |
| zeroExportPower   | zep        |
| solarMaxSellPower | msp        |
| mondayOn          | dmo        |
| tuesdayOn         | dtu        |
| wednesdayOn       | dwe        |
| thursdayOn        | dth        |
| fridayOn          | dfr        |
| saturdayOn        | dsa        |
| sundayOn          | dsu        |
| time1on           | gr1        |
| time2on           | gr2        |
| time3on           | gr3        |
| time4on           | gr4        |
| time5on           | gr5        |
| time6on           | gr6        |
| genTime1on        | ge1        |
| genTime2on        | ge2        |
| genTime3on        | ge3        |
| genTime4on        | ge4        |
| genTime5on        | ge5        |
| genTime6on        | ge6        |

#### Short Values

Some values can also be shortened. Any value that expects `true` or `false` can be shortened to `t` or `f`.

Thus the following are equivalent:

`v2#genTime1on:true`

and

`v2#ge1:t`


