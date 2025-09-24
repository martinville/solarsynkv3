import logging

import postapi
import json
import requests
from datetime import datetime

class ConsoleColor:    
    OKBLUE = "\033[34m"
    OKCYAN = "\033[36m"
    OKGREEN = "\033[32m"        
    MAGENTA = "\033[35m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m" 

# Load settings from JSON file
try:
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
        api_server = json_settings['API_Server']
except Exception as e:
    logging.error(f"Failed to load settings: {e}")
    print(ConsoleColor.FAIL + "Error loading settings.json. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
    exit()
    
def GetInverterInfo(Token,Serial):    
    global api_server         
    # Inverter URL
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":
            print("Inverter fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json);            
            print("Inverter Etotal: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etotal']) + ConsoleColor.ENDC)
            print("Inverter Emonth: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['emonth']) + ConsoleColor.ENDC)
            print("Inverter Etoday: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etoday']) + ConsoleColor.ENDC)
            print("Inverter Eyear: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['eyear']) + ConsoleColor.ENDC)
            print("Inverter Sn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sn']) + ConsoleColor.ENDC)
            print("Inverter Alias: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['alias']) + ConsoleColor.ENDC)
            print("Inverter Gsn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gsn']) + ConsoleColor.ENDC)
            print("Inverter Status: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['status']) + ConsoleColor.ENDC)
            print("Inverter RunStatus: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['runStatus']) + ConsoleColor.ENDC)
            print("Inverter Type: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['type']) + ConsoleColor.ENDC)
            print("Inverter ThumbUrl: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['thumbUrl']) + ConsoleColor.ENDC)
            print("Inverter Opened: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['opened']) + ConsoleColor.ENDC)
            print("Inverter MasterVer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['version']['masterVer']) + ConsoleColor.ENDC)
            print("Inverter SoftVer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['version']['softVer']) + ConsoleColor.ENDC)
            print("Inverter HardVer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['version']['hardVer']) + ConsoleColor.ENDC)
            print("Inverter HmiVer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['version']['hmiVer']) + ConsoleColor.ENDC)
            print("Inverter BmsVer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['version']['bmsVer']) + ConsoleColor.ENDC)
            print("Inverter CommVer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['version']['commVer']) + ConsoleColor.ENDC)
            print("Inverter Id: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['id']) + ConsoleColor.ENDC)
            print("Inverter Name: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['name']) + ConsoleColor.ENDC)
            print("Inverter Type: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['type']) + ConsoleColor.ENDC)
            print("Inverter Master: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['master']) + ConsoleColor.ENDC)
            print("Inverter Installer: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['installer']) + ConsoleColor.ENDC)
            print("Inverter Email: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['email']) + ConsoleColor.ENDC)
            print("Inverter Phone: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['plant']['phone']) + ConsoleColor.ENDC)
            print("Inverter CustCode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['custCode']) + ConsoleColor.ENDC)
            print("Inverter CommType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['commType']) + ConsoleColor.ENDC)
            print("Inverter Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pac']) + ConsoleColor.ENDC)
            print("Inverter UpdateAt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['updateAt']) + ConsoleColor.ENDC)
            print("Inverter RatePower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['ratePower']) + ConsoleColor.ENDC)
            print("Inverter Brand: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['brand']) + ConsoleColor.ENDC)
            print("Inverter Address: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['address']) + ConsoleColor.ENDC)
            print("Inverter Model: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['model']) + ConsoleColor.ENDC)
            print("Inverter ProtocolIdentifier: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['protocolIdentifier']) + ConsoleColor.ENDC)
            print("Inverter EquipType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['equipType']) + ConsoleColor.ENDC)
            print("Inverter Id: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['user']['id']) + ConsoleColor.ENDC)
            print("Inverter Nickname: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['user']['nickname']) + ConsoleColor.ENDC)
            print("Inverter Mobile: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['user']['mobile']) + ConsoleColor.ENDC)
            print("Inverter Email: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['user']['email']) + ConsoleColor.ENDC)
            #Post HA Entities
            postapi.PostHAEntity(Serial,"kWh","energy","Inverter Info etotal","etotal",str(parsed_inverter_json['data']['etotal']))
            postapi.PostHAEntity(Serial,"kWh","energy","Inverter Info emonth","emonth",str(parsed_inverter_json['data']['emonth']))
            postapi.PostHAEntity(Serial,"kWh","energy","Inverter Info etoday","etoday",str(parsed_inverter_json['data']['etoday']))
            postapi.PostHAEntity(Serial,"kWh","energy","Inverter Info eyear","eyear",str(parsed_inverter_json['data']['eyear']))
            postapi.PostHAEntity(Serial,"","","Inverter Info sn","sn",str(parsed_inverter_json['data']['sn']))
            postapi.PostHAEntity(Serial,"","","Inverter Info alias","alias",str(parsed_inverter_json['data']['alias']))
            postapi.PostHAEntity(Serial,"","","Inverter Info gsn","gsn",str(parsed_inverter_json['data']['gsn']))
            postapi.PostHAEntity(Serial,"","","Inverter Info status","status",str(parsed_inverter_json['data']['status']))
            postapi.PostHAEntity(Serial,"","","Inverter Info runStatus","runStatus",str(parsed_inverter_json['data']['runStatus']))
            postapi.PostHAEntity(Serial,"","","Inverter Info type","type",str(parsed_inverter_json['data']['type']))
            postapi.PostHAEntity(Serial,"","","Inverter Info thumbUrl","thumbUrl",str(parsed_inverter_json['data']['thumbUrl']))
            postapi.PostHAEntity(Serial,"","","Inverter Info opened","opened",str(parsed_inverter_json['data']['opened']))
            postapi.PostHAEntity(Serial,"","","Inverter Info version-masterVer","version_masterVer",str(parsed_inverter_json['data']['version']['masterVer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info version-softVer","version_softVer",str(parsed_inverter_json['data']['version']['softVer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info version-hardVer","version_hardVer",str(parsed_inverter_json['data']['version']['hardVer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info version-hmiVer","version_hmiVer",str(parsed_inverter_json['data']['version']['hmiVer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info version-bmsVer","version_bmsVer",str(parsed_inverter_json['data']['version']['bmsVer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info version-commVer","version_commVer",str(parsed_inverter_json['data']['version']['commVer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-id","plant_id",str(parsed_inverter_json['data']['plant']['id']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-name","plant_name",str(parsed_inverter_json['data']['plant']['name']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-type","plant_type",str(parsed_inverter_json['data']['plant']['type']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-master","plant_master",str(parsed_inverter_json['data']['plant']['master']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-installer","plant_installer",str(parsed_inverter_json['data']['plant']['installer']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-email","plant_email",str(parsed_inverter_json['data']['plant']['email']))
            postapi.PostHAEntity(Serial,"","","Inverter Info plant-phone","plant_phone",str(parsed_inverter_json['data']['plant']['phone']))
            postapi.PostHAEntity(Serial,"","","Inverter Info custCode","custCode",str(parsed_inverter_json['data']['custCode']))
            postapi.PostHAEntity(Serial,"","","Inverter Info commType","commType",str(parsed_inverter_json['data']['commType']))
            postapi.PostHAEntity(Serial,"W","power","Inverter Info pac","pac",str(parsed_inverter_json['data']['pac']))
            postapi.PostHAEntity(Serial,"","","Inverter Info updateAt","updateAt",str(parsed_inverter_json['data']['updateAt']))
            postapi.PostHAEntity(Serial,"W","power","Inverter Info ratePower","ratePower",str(parsed_inverter_json['data']['ratePower']))
            postapi.PostHAEntity(Serial,"","","Inverter Info brand","brand",str(parsed_inverter_json['data']['brand']))
            postapi.PostHAEntity(Serial,"","","Inverter Info address","address",str(parsed_inverter_json['data']['address']))
            postapi.PostHAEntity(Serial,"","","Inverter Info model","model",str(parsed_inverter_json['data']['model']))
            postapi.PostHAEntity(Serial,"","","Inverter Info protocolIdentifier","protocolIdentifier",str(parsed_inverter_json['data']['protocolIdentifier']))
            postapi.PostHAEntity(Serial,"","","Inverter Info equipType","equipType",str(parsed_inverter_json['data']['equipType']))
            postapi.PostHAEntity(Serial,"","","Inverter Info user-id","user_id",str(parsed_inverter_json['data']['user']['id']))
            postapi.PostHAEntity(Serial,"","","Inverter Info user-nickname","user_nickname",str(parsed_inverter_json['data']['user']['nickname']))
            postapi.PostHAEntity(Serial,"","","Inverter Info user-mobile","user_mobile",str(parsed_inverter_json['data']['user']['mobile']))
            postapi.PostHAEntity(Serial,"","","Inverter Info user-email","user_email",str(parsed_inverter_json['data']['user']['email']))
        
            
        
       
            

        else:
            print("Inverter fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)

def GetInverterSettingsData(Token,Serial):    
    global api_server    
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://{api_server}/api/v1/inverter/$inverter_serial/realtime/input
    #inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/realtime/input"
    inverter_url = f"https://{api_server}/api/v1/common/setting/{Serial}/read"
    
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "PV data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            print(parsed_inverter_json);
            #print("PV Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pac']) + ConsoleColor.ENDC)
            print("Inverter Setting sellTime1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime1']))
            print("Inverter Setting genTime2on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genTime2on']))
            print("Inverter Setting beep: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['beep']))
            print("Inverter Setting sellTime2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime2']))
            print("Inverter Setting wattOverExitFreqStopDelay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattOverExitFreqStopDelay']))
            print("Inverter Setting sellTime5: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime5']))
            print("Inverter Setting sellTime6: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime6']))
            print("Inverter Setting sellTime3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime3']))
            print("Inverter Setting sellTime4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime4']))
            print("Inverter Setting exMeterCtSwitch: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['exMeterCtSwitch']))
            print("Inverter Setting sdChargeOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sdChargeOn']))
            print("Inverter Setting lockInVoltVar: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lockInVoltVar']))
            print("Inverter Setting time2on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time2on']))
            print("Inverter Setting batWarn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batWarn']))
            print("Inverter Setting wattVarEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarEnable']))
            print("Inverter Setting reconnMinVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['reconnMinVolt']))
            print("Inverter Setting caFStart: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caFStart']))
            print("Inverter Setting pvMaxLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pvMaxLimit']))
            print("Inverter Setting sensorsCheck: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sensorsCheck']))
            print("Inverter Setting underFreq2Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underFreq2Delay']))
            print("Inverter Setting varQac2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varQac2']))
            print("Inverter Setting varQac3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varQac3']))
            print("Inverter Setting varQac1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varQac1']))
            print("Inverter Setting wattUnderExitFreq: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattUnderExitFreq']))
            print("Inverter Setting overVolt1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overVolt1']))
            print("Inverter Setting overVolt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overVolt2']))
            print("Inverter Setting varQac4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varQac4']))
            print("Inverter Setting genPeakPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genPeakPower']))
            print("Inverter Setting meterB: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['meterB']))
            print("Inverter Setting eeprom: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['eeprom']))
            print("Inverter Setting meterA: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['meterA']))
            print("Inverter Setting comSet: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['comSet']))
            print("Inverter Setting caVoltPressureEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caVoltPressureEnable']))
            print("Inverter Setting meterC: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['meterC']))
            print("Inverter Setting wattUnderFreq1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattUnderFreq1']))
            print("Inverter Setting solarMaxSellPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['solarMaxSellPower']))
            print("Inverter Setting acCoupleOnGridSideEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acCoupleOnGridSideEnable']))
            print("Inverter Setting thursdayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['thursdayOn']))
            print("Inverter Setting time3On: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time3On']))
            print("Inverter Setting batteryRestartCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryRestartCap']))
            print("Inverter Setting overFreq1Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overFreq1Delay']))
            print("Inverter Setting bmsErrStop: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bmsErrStop']))
            print("Inverter Setting checkTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['checkTime']))
            print("Inverter Setting acOutputPowerLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acOutputPowerLimit']))
            print("Inverter Setting atsSwitch: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['atsSwitch']))
            print("Inverter Setting pv1SelfCheck: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pv1SelfCheck']))
            print("Inverter Setting acCurrentUp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acCurrentUp']))
            print("Inverter Setting rsd: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['rsd']))
            print("Inverter Setting batteryOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryOn']))
            print("Inverter Setting genTime1on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genTime1on']))
            print("Inverter Setting volt12: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt12']))
            print("Inverter Setting volt10: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt10']))
            print("Inverter Setting volt11: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt11']))
            print("Inverter Setting time1on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time1on']))
            print("Inverter Setting wattUnderFreq1StartDelay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattUnderFreq1StartDelay']))
            print("Inverter Setting rcd: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['rcd']))
            print("Inverter Setting chargeVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeVolt']))
            print("Inverter Setting wednesdayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wednesdayOn']))
            print("Inverter Setting mpptMulti: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['mpptMulti']))
            print("Inverter Setting floatVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['floatVolt']))
            print("Inverter Setting workState: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['workState']))
            print("Inverter Setting loadMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['loadMode']))
            print("Inverter Setting sysWorkMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sysWorkMode']))
            print("Inverter Setting sn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sn']))
            print("Inverter Setting genCoolingTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genCoolingTime']))
            print("Inverter Setting genPeakShaving: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genPeakShaving']))
            print("Inverter Setting offGridImmediatelyOff: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['offGridImmediatelyOff']))
            print("Inverter Setting sellTime3Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime3Volt']))
            print("Inverter Setting sellTime2Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime2Pac']))
            print("Inverter Setting current12: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current12']))
            print("Inverter Setting time2On: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time2On']))
            print("Inverter Setting current10: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current10']))
            print("Inverter Setting current11: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current11']))
            print("Inverter Setting batteryEfficiency: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryEfficiency']))
            print("Inverter Setting genAndGridSignal: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genAndGridSignal']))
            print("Inverter Setting pv3SelfCheck: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pv3SelfCheck']))
            print("Inverter Setting wattV4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattV4']))
            print("Inverter Setting acFreqLow: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acFreqLow']))
            print("Inverter Setting wattV2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattV2']))
            print("Inverter Setting wattV3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattV3']))
            print("Inverter Setting wattV1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattV1']))
            print("Inverter Setting batteryEmptyV: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryEmptyV']))
            print("Inverter Setting open: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['open']))
            print("Inverter Setting reconnMaxFreq: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['reconnMaxFreq']))
            print("Inverter Setting standard: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['standard']))
            print("Inverter Setting wattVarReactive2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarReactive2']))
            print("Inverter Setting disableFloatCharge: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['disableFloatCharge']))
            print("Inverter Setting inverterType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['inverterType']))
            print("Inverter Setting wattVarReactive3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarReactive3']))
            print("Inverter Setting wattVarReactive4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarReactive4']))
            print("Inverter Setting solarPSU: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['solarPSU']))
            print("Inverter Setting fridayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['fridayOn']))
            print("Inverter Setting wattVarReactive1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarReactive1']))
            print("Inverter Setting time4on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time4on']))
            print("Inverter Setting cap6: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['cap6']))
            print("Inverter Setting generatorForcedStart: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['generatorForcedStart']))
            print("Inverter Setting overLongVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overLongVolt']))
            print("Inverter Setting cap4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['cap4']))
            print("Inverter Setting cap5: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['cap5']))
            print("Inverter Setting batteryChargeType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryChargeType']))
            print("Inverter Setting genOffVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genOffVolt']))
            print("Inverter Setting cap2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['cap2']))
            print("Inverter Setting cap3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['cap3']))
            print("Inverter Setting absorptionVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['absorptionVolt']))
            print("Inverter Setting genToLoad: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genToLoad']))
            print("Inverter Setting mpptNum: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['mpptNum']))
            print("Inverter Setting underFreq2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underFreq2']))
            print("Inverter Setting underFreq1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underFreq1']))
            print("Inverter Setting wattPfEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattPfEnable']))
            print("Inverter Setting remoteLock: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['remoteLock']))
            print("Inverter Setting generatorStartCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['generatorStartCap']))
            print("Inverter Setting batteryMaxCurrentCharge: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryMaxCurrentCharge']))
            print("Inverter Setting overFreq1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overFreq1']))
            print("Inverter Setting tuesdayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['tuesdayOn']))
            print("Inverter Setting genOnVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genOnVolt']))
            print("Inverter Setting overFreq2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overFreq2']))
            print("Inverter Setting solar2WindInputEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['solar2WindInputEnable']))
            print("Inverter Setting caVStop: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caVStop']))
            print("Inverter Setting time5On: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time5On']))
            print("Inverter Setting battMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['battMode']))
            print("Inverter Setting allowRemoteControl: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['allowRemoteControl']))
            print("Inverter Setting genOnCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genOnCap']))
            print("Inverter Setting gridAlwaysOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gridAlwaysOn']))
            print("Inverter Setting batteryLowVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryLowVolt']))
            print("Inverter Setting acFreqUp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acFreqUp']))
            print("Inverter Setting cap1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['cap1']))
            print("Inverter Setting chargeLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeLimit']))
            print("Inverter Setting generatorStartVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['generatorStartVolt']))
            print("Inverter Setting overVolt1Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overVolt1Delay']))
            print("Inverter Setting sellTime1Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime1Pac']))
            print("Inverter Setting californiaFreqPressureEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['californiaFreqPressureEnable']))
            print("Inverter Setting activePowerControl: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['activePowerControl']))
            print("Inverter Setting batteryRestartVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryRestartVolt']))
            print("Inverter Setting zeroExportPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['zeroExportPower']))
            print("Inverter Setting overVolt2Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overVolt2Delay']))
            print("Inverter Setting equChargeCycle: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['equChargeCycle']))
            print("Inverter Setting dischargeCurrent: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeCurrent']))
            print("Inverter Setting solarSell: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['solarSell']))
            print("Inverter Setting mpptVoltLow: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['mpptVoltLow']))
            print("Inverter Setting time3on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time3on']))
            print("Inverter Setting wattVoltEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVoltEnable']))
            print("Inverter Setting caFwEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caFwEnable']))
            print("Inverter Setting maxOperatingTimeOfGen: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['maxOperatingTimeOfGen']))
            print("Inverter Setting micExportGridOff: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['micExportGridOff']))
            print("Inverter Setting importPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['importPower']))
            print("Inverter Setting pvLine: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pvLine']))
            print("Inverter Setting three41: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['three41']))
            print("Inverter Setting caVwEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caVwEnable']))
            print("Inverter Setting batteryShutdownVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryShutdownVolt']))
            print("Inverter Setting volt3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt3']))
            print("Inverter Setting volt4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt4']))
            print("Inverter Setting volt1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt1']))
            print("Inverter Setting volt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt2']))
            print("Inverter Setting startVoltUp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['startVoltUp']))
            print("Inverter Setting volt7: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt7']))
            print("Inverter Setting volt8: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt8']))
            print("Inverter Setting volt5: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt5']))
            print("Inverter Setting sellTime6Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime6Pac']))
            print("Inverter Setting volt6: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt6']))
            print("Inverter Setting time4On: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time4On']))
            print("Inverter Setting sellTime4Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime4Volt']))
            print("Inverter Setting volt9: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['volt9']))
            print("Inverter Setting facLowProtect: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['facLowProtect']))
            print("Inverter Setting wattOverFreq1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattOverFreq1']))
            print("Inverter Setting wattPf4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattPf4']))
            print("Inverter Setting lowNoiseMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lowNoiseMode']))
            print("Inverter Setting tempco: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['tempco']))
            print("Inverter Setting arcFactFrz: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactFrz']))
            print("Inverter Setting wattPf1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattPf1']))
            print("Inverter Setting wattPf2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattPf2']))
            print("Inverter Setting wattPf3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattPf3']))
            print("Inverter Setting meterSelect: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['meterSelect']))
            print("Inverter Setting genChargeOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genChargeOn']))
            print("Inverter Setting externalCtRatio: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['externalCtRatio']))
            print("Inverter Setting gridMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gridMode']))
            print("Inverter Setting sellTime5Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime5Pac']))
            print("Inverter Setting lowThrough: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lowThrough']))
            print("Inverter Setting drmEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['drmEnable']))
            print("Inverter Setting pv2SelfCheck: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pv2SelfCheck']))
            print("Inverter Setting underFreq1Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underFreq1Delay']))
            print("Inverter Setting energyMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['energyMode']))
            print("Inverter Setting ampm: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['ampm']))
            print("Inverter Setting gridPeakShaving: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gridPeakShaving']))
            print("Inverter Setting time6on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time6on']))
            print("Inverter Setting fac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['fac']))
            print("Inverter Setting vacLowProtect: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vacLowProtect']))
            print("Inverter Setting chargeCurrentLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeCurrentLimit']))
            print("Inverter Setting caLv3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caLv3']))
            print("Inverter Setting sundayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sundayOn']))
            print("Inverter Setting genTime6on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genTime6on']))
            print("Inverter Setting batteryImpedance: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryImpedance']))
            print("Inverter Setting safetyType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['safetyType']))
            print("Inverter Setting varVolt4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varVolt4']))
            print("Inverter Setting varVolt3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varVolt3']))
            print("Inverter Setting varVolt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varVolt2']))
            print("Inverter Setting specialFunction: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['specialFunction']))
            print("Inverter Setting varVolt1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varVolt1']))
            print("Inverter Setting mondayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['mondayOn']))
            print("Inverter Setting commAddr: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['commAddr']))
            print("Inverter Setting saturdayOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['saturdayOn']))
            print("Inverter Setting dischargeLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeLimit']))
            print("Inverter Setting atsEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['atsEnable']))
            print("Inverter Setting exMeterCt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['exMeterCt']))
            print("Inverter Setting overFreq2Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['overFreq2Delay']))
            print("Inverter Setting phase: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['phase']))
            print("Inverter Setting autoDim: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['autoDim']))
            print("Inverter Setting batteryWorkStatus: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryWorkStatus']))
            print("Inverter Setting genToLoadOn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genToLoadOn']))
            print("Inverter Setting timeSync: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['timeSync']))
            print("Inverter Setting wattOverWgralFreq: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattOverWgralFreq']))
            print("Inverter Setting sdBatteryCurrent: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sdBatteryCurrent']))
            print("Inverter Setting peakAndVallery: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['peakAndVallery']))
            print("Inverter Setting batteryEmptyVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryEmptyVolt']))
            print("Inverter Setting batteryLowCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryLowCap']))
            print("Inverter Setting underVolt2Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underVolt2Delay']))
            print("Inverter Setting equChargeTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['equChargeTime']))
            print("Inverter Setting battType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['battType']))
            print("Inverter Setting gridPeakPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gridPeakPower']))
            print("Inverter Setting reset: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['reset']))
            print("Inverter Setting vacHighProtect: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vacHighProtect']))
            print("Inverter Setting genTime5on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genTime5on']))
            print("Inverter Setting deyeGenPowerDoubleFlag: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['deyeGenPowerDoubleFlag']))
            print("Inverter Setting pwm: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pwm']))
            print("Inverter Setting time5on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time5on']))
            print("Inverter Setting highThrough: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['highThrough']))
            print("Inverter Setting lockOutVoltVar: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lockOutVoltVar']))
            print("Inverter Setting lockInWattPF: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lockInWattPF']))
            print("Inverter Setting caVStart: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caVStart']))
            print("Inverter Setting acVoltUp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acVoltUp']))
            print("Inverter Setting wattFreqEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattFreqEnable']))
            print("Inverter Setting wattOverExitFreq: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattOverExitFreq']))
            print("Inverter Setting sellTime5Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime5Volt']))
            print("Inverter Setting caFStop: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['caFStop']))
            print("Inverter Setting lowPowerMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lowPowerMode']))
            print("Inverter Setting varVoltEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['varVoltEnable']))
            print("Inverter Setting acCoupleFreqUpper: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acCoupleFreqUpper']))
            print("Inverter Setting impedanceLow: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['impedanceLow']))
            print("Inverter Setting acType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acType']))
            print("Inverter Setting facHighProtect: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['facHighProtect']))
            print("Inverter Setting recoveryTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['recoveryTime']))
            print("Inverter Setting underVolt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underVolt2']))
            print("Inverter Setting lithiumMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lithiumMode']))
            print("Inverter Setting underVolt1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underVolt1']))
            print("Inverter Setting gridSignal: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gridSignal']))
            print("Inverter Setting wattOverFreq1StartDelay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattOverFreq1StartDelay']))
            print("Inverter Setting testCommand: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['testCommand']))
            print("Inverter Setting time6On: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time6On']))
            print("Inverter Setting signalIslandModeEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['signalIslandModeEnable']))
            print("Inverter Setting upsStandard: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['upsStandard']))
            print("Inverter Setting reconnMinFreq: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['reconnMinFreq']))
            print("Inverter Setting parallelRegister2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['parallelRegister2']))
            print("Inverter Setting parallelRegister1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['parallelRegister1']))
            print("Inverter Setting startVoltLow: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['startVoltLow']))
            print("Inverter Setting smartLoadOpenDelay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['smartLoadOpenDelay']))
            print("Inverter Setting genTime4on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genTime4on']))
            print("Inverter Setting sellTime1Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime1Volt']))
            print("Inverter Setting wattVarActive4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarActive4']))
            print("Inverter Setting wattVarActive3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarActive3']))
            print("Inverter Setting genConnectGrid: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genConnectGrid']))
            print("Inverter Setting flag2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['flag2']))
            print("Inverter Setting softStart: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['softStart']))
            print("Inverter Setting lockOutWattPF: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lockOutWattPF']))
            print("Inverter Setting sdStartCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sdStartCap']))
            print("Inverter Setting current4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current4']))
            print("Inverter Setting current3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current3']))
            print("Inverter Setting current2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current2']))
            print("Inverter Setting current1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current1']))
            print("Inverter Setting gfdi: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gfdi']))
            print("Inverter Setting current8: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current8']))
            print("Inverter Setting current7: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current7']))
            print("Inverter Setting current6: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current6']))
            print("Inverter Setting current5: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current5']))
            print("Inverter Setting checkSelfTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['checkSelfTime']))
            print("Inverter Setting limit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['limit']))
            print("Inverter Setting wattW3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattW3']))
            print("Inverter Setting wattVarActive2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarActive2']))
            print("Inverter Setting wattW4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattW4']))
            print("Inverter Setting wattVarActive1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattVarActive1']))
            print("Inverter Setting externalCurrent: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['externalCurrent']))
            print("Inverter Setting wattW1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattW1']))
            print("Inverter Setting wattW2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattW2']))
            print("Inverter Setting vnResponseTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vnResponseTime']))
            print("Inverter Setting batteryShutdownCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryShutdownCap']))
            print("Inverter Setting wattUnderExitFreqStopDelay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattUnderExitFreqStopDelay']))
            print("Inverter Setting offset: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['offset']))
            print("Inverter Setting sellTime4Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime4Pac']))
            print("Inverter Setting wattActivePf1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattActivePf1']))
            print("Inverter Setting current9: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current9']))
            print("Inverter Setting dischargeVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeVolt']))
            print("Inverter Setting qvResponseTime: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['qvResponseTime']))
            print("Inverter Setting wattActivePf4: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattActivePf4']))
            print("Inverter Setting time1On: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time1On']))
            print("Inverter Setting wattActivePf2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattActivePf2']))
            print("Inverter Setting four19: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['four19']))
            print("Inverter Setting wattActivePf3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattActivePf3']))
            print("Inverter Setting micExportAll: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['micExportAll']))
            print("Inverter Setting batteryMaxCurrentDischarge: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryMaxCurrentDischarge']))
            print("Inverter Setting isletProtect: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['isletProtect']))
            print("Inverter Setting lockOutChange: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['lockOutChange']))
            print("Inverter Setting californiaVoltPressureEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['californiaVoltPressureEnable']))
            print("Inverter Setting equVoltCharge: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['equVoltCharge']))
            print("Inverter Setting batteryCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryCap']))
            print("Inverter Setting genOffCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genOffCap']))
            print("Inverter Setting genTime3on: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genTime3on']))
            print("Inverter Setting sellTime6Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime6Volt']))
            print("Inverter Setting sellTime3Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime3Pac']))
            print("Inverter Setting acCoupleOnLoadSideEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acCoupleOnLoadSideEnable']))
            print("Inverter Setting sdStartVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sdStartVolt']))
            print("Inverter Setting generatorBatteryCurrent: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['generatorBatteryCurrent']))
            print("Inverter Setting reconnMaxVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['reconnMaxVolt']))
            print("Inverter Setting modbusSn: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['modbusSn']))
            print("Inverter Setting inverterOutputVoltage: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['inverterOutputVoltage']))
            print("Inverter Setting chargeCurrent: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeCurrent']))
            print("Inverter Setting solar1WindInputEnable: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['solar1WindInputEnable']))
            print("Inverter Setting dcVoltUp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dcVoltUp']))
            print("Inverter Setting parallel: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['parallel']))
            print("Inverter Setting limter: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['limter']))
            print("Inverter Setting batErr: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batErr']))
            print("Inverter Setting backupDelay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['backupDelay']))
            print("Inverter Setting dischargeCurrentLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeCurrentLimit']))
            print("Inverter Setting arcFactT: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactT']))
            print("Inverter Setting wattUnderWgalFreq: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['wattUnderWgalFreq']))
            print("Inverter Setting commBaudRate: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['commBaudRate']))
            print("Inverter Setting equipMode: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['equipMode']))
            print("Inverter Setting gridSideINVMeter2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['gridSideINVMeter2']))
            print("Inverter Setting underVolt1Delay: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['underVolt1Delay']))
            print("Inverter Setting arcFaultType: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFaultType']))
            print("Inverter Setting arcFactB: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactB']))
            print("Inverter Setting normalUpwardSlope: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['normalUpwardSlope']))
            print("Inverter Setting arcFactC: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactC']))
            print("Inverter Setting pf: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pf']))
            print("Inverter Setting arcFactD: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactD']))
            print("Inverter Setting genMinSolar: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genMinSolar']))
            print("Inverter Setting sellTime2Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['sellTime2Volt']))
            print("Inverter Setting arcFactF: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactF']))
            print("Inverter Setting arcFactI: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['arcFactI']))
            print("Inverter Setting acVoltLow: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acVoltLow']))
            print("Inverter Setting genSignal: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['genSignal']))
            #Post HA Entities
            postapi.PostHAEntity(Serial,"","","sellTime1","sellTime1",str(parsed_inverter_json['data']['sellTime1']))
            postapi.PostHAEntity(Serial,"","","genTime2on","genTime2on",str(parsed_inverter_json['data']['genTime2on']))
            postapi.PostHAEntity(Serial,"","","beep","beep",str(parsed_inverter_json['data']['beep']))
            postapi.PostHAEntity(Serial,"","","sellTime2","sellTime2",str(parsed_inverter_json['data']['sellTime2']))
            postapi.PostHAEntity(Serial,"","","wattOverExitFreqStopDelay","wattOverExitFreqStopDelay",str(parsed_inverter_json['data']['wattOverExitFreqStopDelay']))
            postapi.PostHAEntity(Serial,"","","sellTime5","sellTime5",str(parsed_inverter_json['data']['sellTime5']))
            postapi.PostHAEntity(Serial,"","","sellTime6","sellTime6",str(parsed_inverter_json['data']['sellTime6']))
            postapi.PostHAEntity(Serial,"","","sellTime3","sellTime3",str(parsed_inverter_json['data']['sellTime3']))
            postapi.PostHAEntity(Serial,"","","sellTime4","sellTime4",str(parsed_inverter_json['data']['sellTime4']))
            postapi.PostHAEntity(Serial,"","","exMeterCtSwitch","exMeterCtSwitch",str(parsed_inverter_json['data']['exMeterCtSwitch']))
            postapi.PostHAEntity(Serial,"","","sdChargeOn","sdChargeOn",str(parsed_inverter_json['data']['sdChargeOn']))
            postapi.PostHAEntity(Serial,"","","lockInVoltVar","lockInVoltVar",str(parsed_inverter_json['data']['lockInVoltVar']))
            postapi.PostHAEntity(Serial,"","","time2on","time2on",str(parsed_inverter_json['data']['time2on']))
            postapi.PostHAEntity(Serial,"","","batWarn","batWarn",str(parsed_inverter_json['data']['batWarn']))
            postapi.PostHAEntity(Serial,"","","wattVarEnable","wattVarEnable",str(parsed_inverter_json['data']['wattVarEnable']))
            postapi.PostHAEntity(Serial,"","","reconnMinVolt","reconnMinVolt",str(parsed_inverter_json['data']['reconnMinVolt']))
            postapi.PostHAEntity(Serial,"","","caFStart","caFStart",str(parsed_inverter_json['data']['caFStart']))
            postapi.PostHAEntity(Serial,"","","pvMaxLimit","pvMaxLimit",str(parsed_inverter_json['data']['pvMaxLimit']))
            postapi.PostHAEntity(Serial,"","","sensorsCheck","sensorsCheck",str(parsed_inverter_json['data']['sensorsCheck']))
            postapi.PostHAEntity(Serial,"","","underFreq2Delay","underFreq2Delay",str(parsed_inverter_json['data']['underFreq2Delay']))
            postapi.PostHAEntity(Serial,"","","varQac2","varQac2",str(parsed_inverter_json['data']['varQac2']))
            postapi.PostHAEntity(Serial,"","","varQac3","varQac3",str(parsed_inverter_json['data']['varQac3']))
            postapi.PostHAEntity(Serial,"","","varQac1","varQac1",str(parsed_inverter_json['data']['varQac1']))
            postapi.PostHAEntity(Serial,"","","wattUnderExitFreq","wattUnderExitFreq",str(parsed_inverter_json['data']['wattUnderExitFreq']))
            postapi.PostHAEntity(Serial,"","","overVolt1","overVolt1",str(parsed_inverter_json['data']['overVolt1']))
            postapi.PostHAEntity(Serial,"","","overVolt2","overVolt2",str(parsed_inverter_json['data']['overVolt2']))
            postapi.PostHAEntity(Serial,"","","varQac4","varQac4",str(parsed_inverter_json['data']['varQac4']))
            postapi.PostHAEntity(Serial,"","","genPeakPower","genPeakPower",str(parsed_inverter_json['data']['genPeakPower']))
            postapi.PostHAEntity(Serial,"","","meterB","meterB",str(parsed_inverter_json['data']['meterB']))
            postapi.PostHAEntity(Serial,"","","eeprom","eeprom",str(parsed_inverter_json['data']['eeprom']))
            postapi.PostHAEntity(Serial,"","","meterA","meterA",str(parsed_inverter_json['data']['meterA']))
            postapi.PostHAEntity(Serial,"","","comSet","comSet",str(parsed_inverter_json['data']['comSet']))
            postapi.PostHAEntity(Serial,"","","caVoltPressureEnable","caVoltPressureEnable",str(parsed_inverter_json['data']['caVoltPressureEnable']))
            postapi.PostHAEntity(Serial,"","","meterC","meterC",str(parsed_inverter_json['data']['meterC']))
            postapi.PostHAEntity(Serial,"","","wattUnderFreq1","wattUnderFreq1",str(parsed_inverter_json['data']['wattUnderFreq1']))
            postapi.PostHAEntity(Serial,"","","solarMaxSellPower","solarMaxSellPower",str(parsed_inverter_json['data']['solarMaxSellPower']))
            postapi.PostHAEntity(Serial,"","","acCoupleOnGridSideEnable","acCoupleOnGridSideEnable",str(parsed_inverter_json['data']['acCoupleOnGridSideEnable']))
            postapi.PostHAEntity(Serial,"","","thursdayOn","thursdayOn",str(parsed_inverter_json['data']['thursdayOn']))
            postapi.PostHAEntity(Serial,"","","time3On","time3On",str(parsed_inverter_json['data']['time3On']))
            postapi.PostHAEntity(Serial,"","","batteryRestartCap","batteryRestartCap",str(parsed_inverter_json['data']['batteryRestartCap']))
            postapi.PostHAEntity(Serial,"","","overFreq1Delay","overFreq1Delay",str(parsed_inverter_json['data']['overFreq1Delay']))
            postapi.PostHAEntity(Serial,"","","bmsErrStop","bmsErrStop",str(parsed_inverter_json['data']['bmsErrStop']))
            postapi.PostHAEntity(Serial,"","","checkTime","checkTime",str(parsed_inverter_json['data']['checkTime']))
            postapi.PostHAEntity(Serial,"","","acOutputPowerLimit","acOutputPowerLimit",str(parsed_inverter_json['data']['acOutputPowerLimit']))
            postapi.PostHAEntity(Serial,"","","atsSwitch","atsSwitch",str(parsed_inverter_json['data']['atsSwitch']))
            postapi.PostHAEntity(Serial,"","","pv1SelfCheck","pv1SelfCheck",str(parsed_inverter_json['data']['pv1SelfCheck']))
            postapi.PostHAEntity(Serial,"","","acCurrentUp","acCurrentUp",str(parsed_inverter_json['data']['acCurrentUp']))
            postapi.PostHAEntity(Serial,"","","rsd","rsd",str(parsed_inverter_json['data']['rsd']))
            postapi.PostHAEntity(Serial,"","","batteryOn","batteryOn",str(parsed_inverter_json['data']['batteryOn']))
            postapi.PostHAEntity(Serial,"","","genTime1on","genTime1on",str(parsed_inverter_json['data']['genTime1on']))
            postapi.PostHAEntity(Serial,"","","volt12","volt12",str(parsed_inverter_json['data']['volt12']))
            postapi.PostHAEntity(Serial,"","","volt10","volt10",str(parsed_inverter_json['data']['volt10']))
            postapi.PostHAEntity(Serial,"","","volt11","volt11",str(parsed_inverter_json['data']['volt11']))
            postapi.PostHAEntity(Serial,"","","time1on","time1on",str(parsed_inverter_json['data']['time1on']))
            postapi.PostHAEntity(Serial,"","","wattUnderFreq1StartDelay","wattUnderFreq1StartDelay",str(parsed_inverter_json['data']['wattUnderFreq1StartDelay']))
            postapi.PostHAEntity(Serial,"","","rcd","rcd",str(parsed_inverter_json['data']['rcd']))
            postapi.PostHAEntity(Serial,"","","chargeVolt","chargeVolt",str(parsed_inverter_json['data']['chargeVolt']))
            postapi.PostHAEntity(Serial,"","","wednesdayOn","wednesdayOn",str(parsed_inverter_json['data']['wednesdayOn']))
            postapi.PostHAEntity(Serial,"","","mpptMulti","mpptMulti",str(parsed_inverter_json['data']['mpptMulti']))
            postapi.PostHAEntity(Serial,"","","floatVolt","floatVolt",str(parsed_inverter_json['data']['floatVolt']))
            postapi.PostHAEntity(Serial,"","","workState","workState",str(parsed_inverter_json['data']['workState']))
            postapi.PostHAEntity(Serial,"","","loadMode","loadMode",str(parsed_inverter_json['data']['loadMode']))
            postapi.PostHAEntity(Serial,"","","sysWorkMode","sysWorkMode",str(parsed_inverter_json['data']['sysWorkMode']))
            postapi.PostHAEntity(Serial,"","","sn","sn",str(parsed_inverter_json['data']['sn']))
            postapi.PostHAEntity(Serial,"","","genCoolingTime","genCoolingTime",str(parsed_inverter_json['data']['genCoolingTime']))
            postapi.PostHAEntity(Serial,"","","genPeakShaving","genPeakShaving",str(parsed_inverter_json['data']['genPeakShaving']))
            postapi.PostHAEntity(Serial,"","","offGridImmediatelyOff","offGridImmediatelyOff",str(parsed_inverter_json['data']['offGridImmediatelyOff']))
            postapi.PostHAEntity(Serial,"","","sellTime3Volt","sellTime3Volt",str(parsed_inverter_json['data']['sellTime3Volt']))
            postapi.PostHAEntity(Serial,"","","sellTime2Pac","sellTime2Pac",str(parsed_inverter_json['data']['sellTime2Pac']))
            postapi.PostHAEntity(Serial,"","","current12","current12",str(parsed_inverter_json['data']['current12']))
            postapi.PostHAEntity(Serial,"","","time2On","time2On",str(parsed_inverter_json['data']['time2On']))
            postapi.PostHAEntity(Serial,"","","current10","current10",str(parsed_inverter_json['data']['current10']))
            postapi.PostHAEntity(Serial,"","","current11","current11",str(parsed_inverter_json['data']['current11']))
            postapi.PostHAEntity(Serial,"","","batteryEfficiency","batteryEfficiency",str(parsed_inverter_json['data']['batteryEfficiency']))
            postapi.PostHAEntity(Serial,"","","genAndGridSignal","genAndGridSignal",str(parsed_inverter_json['data']['genAndGridSignal']))
            postapi.PostHAEntity(Serial,"","","pv3SelfCheck","pv3SelfCheck",str(parsed_inverter_json['data']['pv3SelfCheck']))
            postapi.PostHAEntity(Serial,"","","wattV4","wattV4",str(parsed_inverter_json['data']['wattV4']))
            postapi.PostHAEntity(Serial,"","","acFreqLow","acFreqLow",str(parsed_inverter_json['data']['acFreqLow']))
            postapi.PostHAEntity(Serial,"","","wattV2","wattV2",str(parsed_inverter_json['data']['wattV2']))
            postapi.PostHAEntity(Serial,"","","wattV3","wattV3",str(parsed_inverter_json['data']['wattV3']))
            postapi.PostHAEntity(Serial,"","","wattV1","wattV1",str(parsed_inverter_json['data']['wattV1']))
            postapi.PostHAEntity(Serial,"","","batteryEmptyV","batteryEmptyV",str(parsed_inverter_json['data']['batteryEmptyV']))
            postapi.PostHAEntity(Serial,"","","open","open",str(parsed_inverter_json['data']['open']))
            postapi.PostHAEntity(Serial,"","","reconnMaxFreq","reconnMaxFreq",str(parsed_inverter_json['data']['reconnMaxFreq']))
            postapi.PostHAEntity(Serial,"","","standard","standard",str(parsed_inverter_json['data']['standard']))
            postapi.PostHAEntity(Serial,"","","wattVarReactive2","wattVarReactive2",str(parsed_inverter_json['data']['wattVarReactive2']))
            postapi.PostHAEntity(Serial,"","","disableFloatCharge","disableFloatCharge",str(parsed_inverter_json['data']['disableFloatCharge']))
            postapi.PostHAEntity(Serial,"","","inverterType","inverterType",str(parsed_inverter_json['data']['inverterType']))
            postapi.PostHAEntity(Serial,"","","wattVarReactive3","wattVarReactive3",str(parsed_inverter_json['data']['wattVarReactive3']))
            postapi.PostHAEntity(Serial,"","","wattVarReactive4","wattVarReactive4",str(parsed_inverter_json['data']['wattVarReactive4']))
            postapi.PostHAEntity(Serial,"","","solarPSU","solarPSU",str(parsed_inverter_json['data']['solarPSU']))
            postapi.PostHAEntity(Serial,"","","fridayOn","fridayOn",str(parsed_inverter_json['data']['fridayOn']))
            postapi.PostHAEntity(Serial,"","","wattVarReactive1","wattVarReactive1",str(parsed_inverter_json['data']['wattVarReactive1']))
            postapi.PostHAEntity(Serial,"","","time4on","time4on",str(parsed_inverter_json['data']['time4on']))
            postapi.PostHAEntity(Serial,"","","cap6","cap6",str(parsed_inverter_json['data']['cap6']))
            postapi.PostHAEntity(Serial,"","","generatorForcedStart","generatorForcedStart",str(parsed_inverter_json['data']['generatorForcedStart']))
            postapi.PostHAEntity(Serial,"","","overLongVolt","overLongVolt",str(parsed_inverter_json['data']['overLongVolt']))
            postapi.PostHAEntity(Serial,"","","cap4","cap4",str(parsed_inverter_json['data']['cap4']))
            postapi.PostHAEntity(Serial,"","","cap5","cap5",str(parsed_inverter_json['data']['cap5']))
            postapi.PostHAEntity(Serial,"","","batteryChargeType","batteryChargeType",str(parsed_inverter_json['data']['batteryChargeType']))
            postapi.PostHAEntity(Serial,"","","genOffVolt","genOffVolt",str(parsed_inverter_json['data']['genOffVolt']))
            postapi.PostHAEntity(Serial,"","","cap2","cap2",str(parsed_inverter_json['data']['cap2']))
            postapi.PostHAEntity(Serial,"","","cap3","cap3",str(parsed_inverter_json['data']['cap3']))
            postapi.PostHAEntity(Serial,"","","absorptionVolt","absorptionVolt",str(parsed_inverter_json['data']['absorptionVolt']))
            postapi.PostHAEntity(Serial,"","","genToLoad","genToLoad",str(parsed_inverter_json['data']['genToLoad']))
            postapi.PostHAEntity(Serial,"","","mpptNum","mpptNum",str(parsed_inverter_json['data']['mpptNum']))
            postapi.PostHAEntity(Serial,"","","underFreq2","underFreq2",str(parsed_inverter_json['data']['underFreq2']))
            postapi.PostHAEntity(Serial,"","","underFreq1","underFreq1",str(parsed_inverter_json['data']['underFreq1']))
            postapi.PostHAEntity(Serial,"","","wattPfEnable","wattPfEnable",str(parsed_inverter_json['data']['wattPfEnable']))
            postapi.PostHAEntity(Serial,"","","remoteLock","remoteLock",str(parsed_inverter_json['data']['remoteLock']))
            postapi.PostHAEntity(Serial,"","","generatorStartCap","generatorStartCap",str(parsed_inverter_json['data']['generatorStartCap']))
            postapi.PostHAEntity(Serial,"","","batteryMaxCurrentCharge","batteryMaxCurrentCharge",str(parsed_inverter_json['data']['batteryMaxCurrentCharge']))
            postapi.PostHAEntity(Serial,"","","overFreq1","overFreq1",str(parsed_inverter_json['data']['overFreq1']))
            postapi.PostHAEntity(Serial,"","","tuesdayOn","tuesdayOn",str(parsed_inverter_json['data']['tuesdayOn']))
            postapi.PostHAEntity(Serial,"","","genOnVolt","genOnVolt",str(parsed_inverter_json['data']['genOnVolt']))
            postapi.PostHAEntity(Serial,"","","overFreq2","overFreq2",str(parsed_inverter_json['data']['overFreq2']))
            postapi.PostHAEntity(Serial,"","","solar2WindInputEnable","solar2WindInputEnable",str(parsed_inverter_json['data']['solar2WindInputEnable']))
            postapi.PostHAEntity(Serial,"","","caVStop","caVStop",str(parsed_inverter_json['data']['caVStop']))
            postapi.PostHAEntity(Serial,"","","time5On","time5On",str(parsed_inverter_json['data']['time5On']))
            postapi.PostHAEntity(Serial,"","","battMode","battMode",str(parsed_inverter_json['data']['battMode']))
            postapi.PostHAEntity(Serial,"","","allowRemoteControl","allowRemoteControl",str(parsed_inverter_json['data']['allowRemoteControl']))
            postapi.PostHAEntity(Serial,"","","genOnCap","genOnCap",str(parsed_inverter_json['data']['genOnCap']))
            postapi.PostHAEntity(Serial,"","","gridAlwaysOn","gridAlwaysOn",str(parsed_inverter_json['data']['gridAlwaysOn']))
            postapi.PostHAEntity(Serial,"","","batteryLowVolt","batteryLowVolt",str(parsed_inverter_json['data']['batteryLowVolt']))
            postapi.PostHAEntity(Serial,"","","acFreqUp","acFreqUp",str(parsed_inverter_json['data']['acFreqUp']))
            postapi.PostHAEntity(Serial,"","","cap1","cap1",str(parsed_inverter_json['data']['cap1']))
            postapi.PostHAEntity(Serial,"","","chargeLimit","chargeLimit",str(parsed_inverter_json['data']['chargeLimit']))
            postapi.PostHAEntity(Serial,"","","generatorStartVolt","generatorStartVolt",str(parsed_inverter_json['data']['generatorStartVolt']))
            postapi.PostHAEntity(Serial,"","","overVolt1Delay","overVolt1Delay",str(parsed_inverter_json['data']['overVolt1Delay']))
            postapi.PostHAEntity(Serial,"","","sellTime1Pac","sellTime1Pac",str(parsed_inverter_json['data']['sellTime1Pac']))
            postapi.PostHAEntity(Serial,"","","californiaFreqPressureEnable","californiaFreqPressureEnable",str(parsed_inverter_json['data']['californiaFreqPressureEnable']))
            postapi.PostHAEntity(Serial,"","","activePowerControl","activePowerControl",str(parsed_inverter_json['data']['activePowerControl']))
            postapi.PostHAEntity(Serial,"","","batteryRestartVolt","batteryRestartVolt",str(parsed_inverter_json['data']['batteryRestartVolt']))
            postapi.PostHAEntity(Serial,"","","zeroExportPower","zeroExportPower",str(parsed_inverter_json['data']['zeroExportPower']))
            postapi.PostHAEntity(Serial,"","","overVolt2Delay","overVolt2Delay",str(parsed_inverter_json['data']['overVolt2Delay']))
            postapi.PostHAEntity(Serial,"","","equChargeCycle","equChargeCycle",str(parsed_inverter_json['data']['equChargeCycle']))
            postapi.PostHAEntity(Serial,"","","dischargeCurrent","dischargeCurrent",str(parsed_inverter_json['data']['dischargeCurrent']))
            postapi.PostHAEntity(Serial,"","","solarSell","solarSell",str(parsed_inverter_json['data']['solarSell']))
            postapi.PostHAEntity(Serial,"","","mpptVoltLow","mpptVoltLow",str(parsed_inverter_json['data']['mpptVoltLow']))
            postapi.PostHAEntity(Serial,"","","time3on","time3on",str(parsed_inverter_json['data']['time3on']))
            postapi.PostHAEntity(Serial,"","","wattVoltEnable","wattVoltEnable",str(parsed_inverter_json['data']['wattVoltEnable']))
            postapi.PostHAEntity(Serial,"","","caFwEnable","caFwEnable",str(parsed_inverter_json['data']['caFwEnable']))
            postapi.PostHAEntity(Serial,"","","maxOperatingTimeOfGen","maxOperatingTimeOfGen",str(parsed_inverter_json['data']['maxOperatingTimeOfGen']))
            postapi.PostHAEntity(Serial,"","","micExportGridOff","micExportGridOff",str(parsed_inverter_json['data']['micExportGridOff']))
            postapi.PostHAEntity(Serial,"","","importPower","importPower",str(parsed_inverter_json['data']['importPower']))
            postapi.PostHAEntity(Serial,"","","pvLine","pvLine",str(parsed_inverter_json['data']['pvLine']))
            postapi.PostHAEntity(Serial,"","","three41","three41",str(parsed_inverter_json['data']['three41']))
            postapi.PostHAEntity(Serial,"","","caVwEnable","caVwEnable",str(parsed_inverter_json['data']['caVwEnable']))
            postapi.PostHAEntity(Serial,"","","batteryShutdownVolt","batteryShutdownVolt",str(parsed_inverter_json['data']['batteryShutdownVolt']))
            postapi.PostHAEntity(Serial,"","","volt3","volt3",str(parsed_inverter_json['data']['volt3']))
            postapi.PostHAEntity(Serial,"","","volt4","volt4",str(parsed_inverter_json['data']['volt4']))
            postapi.PostHAEntity(Serial,"","","volt1","volt1",str(parsed_inverter_json['data']['volt1']))
            postapi.PostHAEntity(Serial,"","","volt2","volt2",str(parsed_inverter_json['data']['volt2']))
            postapi.PostHAEntity(Serial,"","","startVoltUp","startVoltUp",str(parsed_inverter_json['data']['startVoltUp']))
            postapi.PostHAEntity(Serial,"","","volt7","volt7",str(parsed_inverter_json['data']['volt7']))
            postapi.PostHAEntity(Serial,"","","volt8","volt8",str(parsed_inverter_json['data']['volt8']))
            postapi.PostHAEntity(Serial,"","","volt5","volt5",str(parsed_inverter_json['data']['volt5']))
            postapi.PostHAEntity(Serial,"","","sellTime6Pac","sellTime6Pac",str(parsed_inverter_json['data']['sellTime6Pac']))
            postapi.PostHAEntity(Serial,"","","volt6","volt6",str(parsed_inverter_json['data']['volt6']))
            postapi.PostHAEntity(Serial,"","","time4On","time4On",str(parsed_inverter_json['data']['time4On']))
            postapi.PostHAEntity(Serial,"","","sellTime4Volt","sellTime4Volt",str(parsed_inverter_json['data']['sellTime4Volt']))
            postapi.PostHAEntity(Serial,"","","volt9","volt9",str(parsed_inverter_json['data']['volt9']))
            postapi.PostHAEntity(Serial,"","","facLowProtect","facLowProtect",str(parsed_inverter_json['data']['facLowProtect']))
            postapi.PostHAEntity(Serial,"","","wattOverFreq1","wattOverFreq1",str(parsed_inverter_json['data']['wattOverFreq1']))
            postapi.PostHAEntity(Serial,"","","wattPf4","wattPf4",str(parsed_inverter_json['data']['wattPf4']))
            postapi.PostHAEntity(Serial,"","","lowNoiseMode","lowNoiseMode",str(parsed_inverter_json['data']['lowNoiseMode']))
            postapi.PostHAEntity(Serial,"","","tempco","tempco",str(parsed_inverter_json['data']['tempco']))
            postapi.PostHAEntity(Serial,"","","arcFactFrz","arcFactFrz",str(parsed_inverter_json['data']['arcFactFrz']))
            postapi.PostHAEntity(Serial,"","","wattPf1","wattPf1",str(parsed_inverter_json['data']['wattPf1']))
            postapi.PostHAEntity(Serial,"","","wattPf2","wattPf2",str(parsed_inverter_json['data']['wattPf2']))
            postapi.PostHAEntity(Serial,"","","wattPf3","wattPf3",str(parsed_inverter_json['data']['wattPf3']))
            postapi.PostHAEntity(Serial,"","","meterSelect","meterSelect",str(parsed_inverter_json['data']['meterSelect']))
            postapi.PostHAEntity(Serial,"","","genChargeOn","genChargeOn",str(parsed_inverter_json['data']['genChargeOn']))
            postapi.PostHAEntity(Serial,"","","externalCtRatio","externalCtRatio",str(parsed_inverter_json['data']['externalCtRatio']))
            postapi.PostHAEntity(Serial,"","","gridMode","gridMode",str(parsed_inverter_json['data']['gridMode']))
            postapi.PostHAEntity(Serial,"","","sellTime5Pac","sellTime5Pac",str(parsed_inverter_json['data']['sellTime5Pac']))
            postapi.PostHAEntity(Serial,"","","lowThrough","lowThrough",str(parsed_inverter_json['data']['lowThrough']))
            postapi.PostHAEntity(Serial,"","","drmEnable","drmEnable",str(parsed_inverter_json['data']['drmEnable']))
            postapi.PostHAEntity(Serial,"","","pv2SelfCheck","pv2SelfCheck",str(parsed_inverter_json['data']['pv2SelfCheck']))
            postapi.PostHAEntity(Serial,"","","underFreq1Delay","underFreq1Delay",str(parsed_inverter_json['data']['underFreq1Delay']))
            postapi.PostHAEntity(Serial,"","","energyMode","energyMode",str(parsed_inverter_json['data']['energyMode']))
            postapi.PostHAEntity(Serial,"","","ampm","ampm",str(parsed_inverter_json['data']['ampm']))
            postapi.PostHAEntity(Serial,"","","gridPeakShaving","gridPeakShaving",str(parsed_inverter_json['data']['gridPeakShaving']))
            postapi.PostHAEntity(Serial,"","","time6on","time6on",str(parsed_inverter_json['data']['time6on']))
            postapi.PostHAEntity(Serial,"","","fac","fac",str(parsed_inverter_json['data']['fac']))
            postapi.PostHAEntity(Serial,"","","vacLowProtect","vacLowProtect",str(parsed_inverter_json['data']['vacLowProtect']))
            postapi.PostHAEntity(Serial,"","","chargeCurrentLimit","chargeCurrentLimit",str(parsed_inverter_json['data']['chargeCurrentLimit']))
            postapi.PostHAEntity(Serial,"","","caLv3","caLv3",str(parsed_inverter_json['data']['caLv3']))
            postapi.PostHAEntity(Serial,"","","sundayOn","sundayOn",str(parsed_inverter_json['data']['sundayOn']))
            postapi.PostHAEntity(Serial,"","","genTime6on","genTime6on",str(parsed_inverter_json['data']['genTime6on']))
            postapi.PostHAEntity(Serial,"","","batteryImpedance","batteryImpedance",str(parsed_inverter_json['data']['batteryImpedance']))
            postapi.PostHAEntity(Serial,"","","safetyType","safetyType",str(parsed_inverter_json['data']['safetyType']))
            postapi.PostHAEntity(Serial,"","","varVolt4","varVolt4",str(parsed_inverter_json['data']['varVolt4']))
            postapi.PostHAEntity(Serial,"","","varVolt3","varVolt3",str(parsed_inverter_json['data']['varVolt3']))
            postapi.PostHAEntity(Serial,"","","varVolt2","varVolt2",str(parsed_inverter_json['data']['varVolt2']))
            postapi.PostHAEntity(Serial,"","","specialFunction","specialFunction",str(parsed_inverter_json['data']['specialFunction']))
            postapi.PostHAEntity(Serial,"","","varVolt1","varVolt1",str(parsed_inverter_json['data']['varVolt1']))
            postapi.PostHAEntity(Serial,"","","mondayOn","mondayOn",str(parsed_inverter_json['data']['mondayOn']))
            postapi.PostHAEntity(Serial,"","","commAddr","commAddr",str(parsed_inverter_json['data']['commAddr']))
            postapi.PostHAEntity(Serial,"","","saturdayOn","saturdayOn",str(parsed_inverter_json['data']['saturdayOn']))
            postapi.PostHAEntity(Serial,"","","dischargeLimit","dischargeLimit",str(parsed_inverter_json['data']['dischargeLimit']))
            postapi.PostHAEntity(Serial,"","","atsEnable","atsEnable",str(parsed_inverter_json['data']['atsEnable']))
            postapi.PostHAEntity(Serial,"","","exMeterCt","exMeterCt",str(parsed_inverter_json['data']['exMeterCt']))
            postapi.PostHAEntity(Serial,"","","overFreq2Delay","overFreq2Delay",str(parsed_inverter_json['data']['overFreq2Delay']))
            postapi.PostHAEntity(Serial,"","","phase","phase",str(parsed_inverter_json['data']['phase']))
            postapi.PostHAEntity(Serial,"","","autoDim","autoDim",str(parsed_inverter_json['data']['autoDim']))
            postapi.PostHAEntity(Serial,"","","batteryWorkStatus","batteryWorkStatus",str(parsed_inverter_json['data']['batteryWorkStatus']))
            postapi.PostHAEntity(Serial,"","","genToLoadOn","genToLoadOn",str(parsed_inverter_json['data']['genToLoadOn']))
            postapi.PostHAEntity(Serial,"","","timeSync","timeSync",str(parsed_inverter_json['data']['timeSync']))
            postapi.PostHAEntity(Serial,"","","wattOverWgralFreq","wattOverWgralFreq",str(parsed_inverter_json['data']['wattOverWgralFreq']))
            postapi.PostHAEntity(Serial,"","","sdBatteryCurrent","sdBatteryCurrent",str(parsed_inverter_json['data']['sdBatteryCurrent']))
            postapi.PostHAEntity(Serial,"","","peakAndVallery","peakAndVallery",str(parsed_inverter_json['data']['peakAndVallery']))
            postapi.PostHAEntity(Serial,"","","batteryEmptyVolt","batteryEmptyVolt",str(parsed_inverter_json['data']['batteryEmptyVolt']))
            postapi.PostHAEntity(Serial,"","","batteryLowCap","batteryLowCap",str(parsed_inverter_json['data']['batteryLowCap']))
            postapi.PostHAEntity(Serial,"","","underVolt2Delay","underVolt2Delay",str(parsed_inverter_json['data']['underVolt2Delay']))
            postapi.PostHAEntity(Serial,"","","equChargeTime","equChargeTime",str(parsed_inverter_json['data']['equChargeTime']))
            postapi.PostHAEntity(Serial,"","","battType","battType",str(parsed_inverter_json['data']['battType']))
            postapi.PostHAEntity(Serial,"","","gridPeakPower","gridPeakPower",str(parsed_inverter_json['data']['gridPeakPower']))
            postapi.PostHAEntity(Serial,"","","reset","reset",str(parsed_inverter_json['data']['reset']))
            postapi.PostHAEntity(Serial,"","","vacHighProtect","vacHighProtect",str(parsed_inverter_json['data']['vacHighProtect']))
            postapi.PostHAEntity(Serial,"","","genTime5on","genTime5on",str(parsed_inverter_json['data']['genTime5on']))
            postapi.PostHAEntity(Serial,"","","deyeGenPowerDoubleFlag","deyeGenPowerDoubleFlag",str(parsed_inverter_json['data']['deyeGenPowerDoubleFlag']))
            postapi.PostHAEntity(Serial,"","","pwm","pwm",str(parsed_inverter_json['data']['pwm']))
            postapi.PostHAEntity(Serial,"","","time5on","time5on",str(parsed_inverter_json['data']['time5on']))
            postapi.PostHAEntity(Serial,"","","highThrough","highThrough",str(parsed_inverter_json['data']['highThrough']))
            postapi.PostHAEntity(Serial,"","","lockOutVoltVar","lockOutVoltVar",str(parsed_inverter_json['data']['lockOutVoltVar']))
            postapi.PostHAEntity(Serial,"","","lockInWattPF","lockInWattPF",str(parsed_inverter_json['data']['lockInWattPF']))
            postapi.PostHAEntity(Serial,"","","caVStart","caVStart",str(parsed_inverter_json['data']['caVStart']))
            postapi.PostHAEntity(Serial,"","","acVoltUp","acVoltUp",str(parsed_inverter_json['data']['acVoltUp']))
            postapi.PostHAEntity(Serial,"","","wattFreqEnable","wattFreqEnable",str(parsed_inverter_json['data']['wattFreqEnable']))
            postapi.PostHAEntity(Serial,"","","wattOverExitFreq","wattOverExitFreq",str(parsed_inverter_json['data']['wattOverExitFreq']))
            postapi.PostHAEntity(Serial,"","","sellTime5Volt","sellTime5Volt",str(parsed_inverter_json['data']['sellTime5Volt']))
            postapi.PostHAEntity(Serial,"","","caFStop","caFStop",str(parsed_inverter_json['data']['caFStop']))
            postapi.PostHAEntity(Serial,"","","lowPowerMode","lowPowerMode",str(parsed_inverter_json['data']['lowPowerMode']))
            postapi.PostHAEntity(Serial,"","","varVoltEnable","varVoltEnable",str(parsed_inverter_json['data']['varVoltEnable']))
            postapi.PostHAEntity(Serial,"","","acCoupleFreqUpper","acCoupleFreqUpper",str(parsed_inverter_json['data']['acCoupleFreqUpper']))
            postapi.PostHAEntity(Serial,"","","impedanceLow","impedanceLow",str(parsed_inverter_json['data']['impedanceLow']))
            postapi.PostHAEntity(Serial,"","","acType","acType",str(parsed_inverter_json['data']['acType']))
            postapi.PostHAEntity(Serial,"","","facHighProtect","facHighProtect",str(parsed_inverter_json['data']['facHighProtect']))
            postapi.PostHAEntity(Serial,"","","recoveryTime","recoveryTime",str(parsed_inverter_json['data']['recoveryTime']))
            postapi.PostHAEntity(Serial,"","","underVolt2","underVolt2",str(parsed_inverter_json['data']['underVolt2']))
            postapi.PostHAEntity(Serial,"","","lithiumMode","lithiumMode",str(parsed_inverter_json['data']['lithiumMode']))
            postapi.PostHAEntity(Serial,"","","underVolt1","underVolt1",str(parsed_inverter_json['data']['underVolt1']))
            postapi.PostHAEntity(Serial,"","","gridSignal","gridSignal",str(parsed_inverter_json['data']['gridSignal']))
            postapi.PostHAEntity(Serial,"","","wattOverFreq1StartDelay","wattOverFreq1StartDelay",str(parsed_inverter_json['data']['wattOverFreq1StartDelay']))
            postapi.PostHAEntity(Serial,"","","testCommand","testCommand",str(parsed_inverter_json['data']['testCommand']))
            postapi.PostHAEntity(Serial,"","","time6On","time6On",str(parsed_inverter_json['data']['time6On']))
            postapi.PostHAEntity(Serial,"","","signalIslandModeEnable","signalIslandModeEnable",str(parsed_inverter_json['data']['signalIslandModeEnable']))
            postapi.PostHAEntity(Serial,"","","upsStandard","upsStandard",str(parsed_inverter_json['data']['upsStandard']))
            postapi.PostHAEntity(Serial,"","","reconnMinFreq","reconnMinFreq",str(parsed_inverter_json['data']['reconnMinFreq']))
            postapi.PostHAEntity(Serial,"","","parallelRegister2","parallelRegister2",str(parsed_inverter_json['data']['parallelRegister2']))
            postapi.PostHAEntity(Serial,"","","parallelRegister1","parallelRegister1",str(parsed_inverter_json['data']['parallelRegister1']))
            postapi.PostHAEntity(Serial,"","","startVoltLow","startVoltLow",str(parsed_inverter_json['data']['startVoltLow']))
            postapi.PostHAEntity(Serial,"","","smartLoadOpenDelay","smartLoadOpenDelay",str(parsed_inverter_json['data']['smartLoadOpenDelay']))
            postapi.PostHAEntity(Serial,"","","genTime4on","genTime4on",str(parsed_inverter_json['data']['genTime4on']))
            postapi.PostHAEntity(Serial,"","","sellTime1Volt","sellTime1Volt",str(parsed_inverter_json['data']['sellTime1Volt']))
            postapi.PostHAEntity(Serial,"","","wattVarActive4","wattVarActive4",str(parsed_inverter_json['data']['wattVarActive4']))
            postapi.PostHAEntity(Serial,"","","wattVarActive3","wattVarActive3",str(parsed_inverter_json['data']['wattVarActive3']))
            postapi.PostHAEntity(Serial,"","","genConnectGrid","genConnectGrid",str(parsed_inverter_json['data']['genConnectGrid']))
            postapi.PostHAEntity(Serial,"","","flag2","flag2",str(parsed_inverter_json['data']['flag2']))
            postapi.PostHAEntity(Serial,"","","softStart","softStart",str(parsed_inverter_json['data']['softStart']))
            postapi.PostHAEntity(Serial,"","","lockOutWattPF","lockOutWattPF",str(parsed_inverter_json['data']['lockOutWattPF']))
            postapi.PostHAEntity(Serial,"","","sdStartCap","sdStartCap",str(parsed_inverter_json['data']['sdStartCap']))
            postapi.PostHAEntity(Serial,"","","current4","current4",str(parsed_inverter_json['data']['current4']))
            postapi.PostHAEntity(Serial,"","","current3","current3",str(parsed_inverter_json['data']['current3']))
            postapi.PostHAEntity(Serial,"","","current2","current2",str(parsed_inverter_json['data']['current2']))
            postapi.PostHAEntity(Serial,"","","current1","current1",str(parsed_inverter_json['data']['current1']))
            postapi.PostHAEntity(Serial,"","","gfdi","gfdi",str(parsed_inverter_json['data']['gfdi']))
            postapi.PostHAEntity(Serial,"","","current8","current8",str(parsed_inverter_json['data']['current8']))
            postapi.PostHAEntity(Serial,"","","current7","current7",str(parsed_inverter_json['data']['current7']))
            postapi.PostHAEntity(Serial,"","","current6","current6",str(parsed_inverter_json['data']['current6']))
            postapi.PostHAEntity(Serial,"","","current5","current5",str(parsed_inverter_json['data']['current5']))
            postapi.PostHAEntity(Serial,"","","checkSelfTime","checkSelfTime",str(parsed_inverter_json['data']['checkSelfTime']))
            postapi.PostHAEntity(Serial,"","","limit","limit",str(parsed_inverter_json['data']['limit']))
            postapi.PostHAEntity(Serial,"","","wattW3","wattW3",str(parsed_inverter_json['data']['wattW3']))
            postapi.PostHAEntity(Serial,"","","wattVarActive2","wattVarActive2",str(parsed_inverter_json['data']['wattVarActive2']))
            postapi.PostHAEntity(Serial,"","","wattW4","wattW4",str(parsed_inverter_json['data']['wattW4']))
            postapi.PostHAEntity(Serial,"","","wattVarActive1","wattVarActive1",str(parsed_inverter_json['data']['wattVarActive1']))
            postapi.PostHAEntity(Serial,"","","externalCurrent","externalCurrent",str(parsed_inverter_json['data']['externalCurrent']))
            postapi.PostHAEntity(Serial,"","","wattW1","wattW1",str(parsed_inverter_json['data']['wattW1']))
            postapi.PostHAEntity(Serial,"","","wattW2","wattW2",str(parsed_inverter_json['data']['wattW2']))
            postapi.PostHAEntity(Serial,"","","vnResponseTime","vnResponseTime",str(parsed_inverter_json['data']['vnResponseTime']))
            postapi.PostHAEntity(Serial,"","","batteryShutdownCap","batteryShutdownCap",str(parsed_inverter_json['data']['batteryShutdownCap']))
            postapi.PostHAEntity(Serial,"","","wattUnderExitFreqStopDelay","wattUnderExitFreqStopDelay",str(parsed_inverter_json['data']['wattUnderExitFreqStopDelay']))
            postapi.PostHAEntity(Serial,"","","offset","offset",str(parsed_inverter_json['data']['offset']))
            postapi.PostHAEntity(Serial,"","","sellTime4Pac","sellTime4Pac",str(parsed_inverter_json['data']['sellTime4Pac']))
            postapi.PostHAEntity(Serial,"","","wattActivePf1","wattActivePf1",str(parsed_inverter_json['data']['wattActivePf1']))
            postapi.PostHAEntity(Serial,"","","current9","current9",str(parsed_inverter_json['data']['current9']))
            postapi.PostHAEntity(Serial,"","","dischargeVolt","dischargeVolt",str(parsed_inverter_json['data']['dischargeVolt']))
            postapi.PostHAEntity(Serial,"","","qvResponseTime","qvResponseTime",str(parsed_inverter_json['data']['qvResponseTime']))
            postapi.PostHAEntity(Serial,"","","wattActivePf4","wattActivePf4",str(parsed_inverter_json['data']['wattActivePf4']))
            postapi.PostHAEntity(Serial,"","","time1On","time1On",str(parsed_inverter_json['data']['time1On']))
            postapi.PostHAEntity(Serial,"","","wattActivePf2","wattActivePf2",str(parsed_inverter_json['data']['wattActivePf2']))
            postapi.PostHAEntity(Serial,"","","four19","four19",str(parsed_inverter_json['data']['four19']))
            postapi.PostHAEntity(Serial,"","","wattActivePf3","wattActivePf3",str(parsed_inverter_json['data']['wattActivePf3']))
            postapi.PostHAEntity(Serial,"","","micExportAll","micExportAll",str(parsed_inverter_json['data']['micExportAll']))
            postapi.PostHAEntity(Serial,"","","batteryMaxCurrentDischarge","batteryMaxCurrentDischarge",str(parsed_inverter_json['data']['batteryMaxCurrentDischarge']))
            postapi.PostHAEntity(Serial,"","","isletProtect","isletProtect",str(parsed_inverter_json['data']['isletProtect']))
            postapi.PostHAEntity(Serial,"","","lockOutChange","lockOutChange",str(parsed_inverter_json['data']['lockOutChange']))
            postapi.PostHAEntity(Serial,"","","californiaVoltPressureEnable","californiaVoltPressureEnable",str(parsed_inverter_json['data']['californiaVoltPressureEnable']))
            postapi.PostHAEntity(Serial,"","","equVoltCharge","equVoltCharge",str(parsed_inverter_json['data']['equVoltCharge']))
            postapi.PostHAEntity(Serial,"","","batteryCap","batteryCap",str(parsed_inverter_json['data']['batteryCap']))
            postapi.PostHAEntity(Serial,"","","genOffCap","genOffCap",str(parsed_inverter_json['data']['genOffCap']))
            postapi.PostHAEntity(Serial,"","","genTime3on","genTime3on",str(parsed_inverter_json['data']['genTime3on']))
            postapi.PostHAEntity(Serial,"","","sellTime6Volt","sellTime6Volt",str(parsed_inverter_json['data']['sellTime6Volt']))
            postapi.PostHAEntity(Serial,"","","sellTime3Pac","sellTime3Pac",str(parsed_inverter_json['data']['sellTime3Pac']))
            postapi.PostHAEntity(Serial,"","","acCoupleOnLoadSideEnable","acCoupleOnLoadSideEnable",str(parsed_inverter_json['data']['acCoupleOnLoadSideEnable']))
            postapi.PostHAEntity(Serial,"","","sdStartVolt","sdStartVolt",str(parsed_inverter_json['data']['sdStartVolt']))
            postapi.PostHAEntity(Serial,"","","generatorBatteryCurrent","generatorBatteryCurrent",str(parsed_inverter_json['data']['generatorBatteryCurrent']))
            postapi.PostHAEntity(Serial,"","","reconnMaxVolt","reconnMaxVolt",str(parsed_inverter_json['data']['reconnMaxVolt']))
            postapi.PostHAEntity(Serial,"","","modbusSn","modbusSn",str(parsed_inverter_json['data']['modbusSn']))
            postapi.PostHAEntity(Serial,"","","inverterOutputVoltage","inverterOutputVoltage",str(parsed_inverter_json['data']['inverterOutputVoltage']))
            postapi.PostHAEntity(Serial,"","","chargeCurrent","chargeCurrent",str(parsed_inverter_json['data']['chargeCurrent']))
            postapi.PostHAEntity(Serial,"","","solar1WindInputEnable","solar1WindInputEnable",str(parsed_inverter_json['data']['solar1WindInputEnable']))
            postapi.PostHAEntity(Serial,"","","dcVoltUp","dcVoltUp",str(parsed_inverter_json['data']['dcVoltUp']))
            postapi.PostHAEntity(Serial,"","","parallel","parallel",str(parsed_inverter_json['data']['parallel']))
            postapi.PostHAEntity(Serial,"","","limter","limter",str(parsed_inverter_json['data']['limter']))
            postapi.PostHAEntity(Serial,"","","batErr","batErr",str(parsed_inverter_json['data']['batErr']))
            postapi.PostHAEntity(Serial,"","","backupDelay","backupDelay",str(parsed_inverter_json['data']['backupDelay']))
            postapi.PostHAEntity(Serial,"","","dischargeCurrentLimit","dischargeCurrentLimit",str(parsed_inverter_json['data']['dischargeCurrentLimit']))
            postapi.PostHAEntity(Serial,"","","arcFactT","arcFactT",str(parsed_inverter_json['data']['arcFactT']))
            postapi.PostHAEntity(Serial,"","","wattUnderWgalFreq","wattUnderWgalFreq",str(parsed_inverter_json['data']['wattUnderWgalFreq']))
            postapi.PostHAEntity(Serial,"","","commBaudRate","commBaudRate",str(parsed_inverter_json['data']['commBaudRate']))
            postapi.PostHAEntity(Serial,"","","equipMode","equipMode",str(parsed_inverter_json['data']['equipMode']))
            postapi.PostHAEntity(Serial,"","","gridSideINVMeter2","gridSideINVMeter2",str(parsed_inverter_json['data']['gridSideINVMeter2']))
            postapi.PostHAEntity(Serial,"","","underVolt1Delay","underVolt1Delay",str(parsed_inverter_json['data']['underVolt1Delay']))
            postapi.PostHAEntity(Serial,"","","arcFaultType","arcFaultType",str(parsed_inverter_json['data']['arcFaultType']))
            postapi.PostHAEntity(Serial,"","","arcFactB","arcFactB",str(parsed_inverter_json['data']['arcFactB']))
            postapi.PostHAEntity(Serial,"","","normalUpwardSlope","normalUpwardSlope",str(parsed_inverter_json['data']['normalUpwardSlope']))
            postapi.PostHAEntity(Serial,"","","arcFactC","arcFactC",str(parsed_inverter_json['data']['arcFactC']))
            postapi.PostHAEntity(Serial,"","","pf","pf",str(parsed_inverter_json['data']['pf']))
            postapi.PostHAEntity(Serial,"","","arcFactD","arcFactD",str(parsed_inverter_json['data']['arcFactD']))
            postapi.PostHAEntity(Serial,"","","genMinSolar","genMinSolar",str(parsed_inverter_json['data']['genMinSolar']))
            postapi.PostHAEntity(Serial,"","","sellTime2Volt","sellTime2Volt",str(parsed_inverter_json['data']['sellTime2Volt']))
            postapi.PostHAEntity(Serial,"","","arcFactF","arcFactF",str(parsed_inverter_json['data']['arcFactF']))
            postapi.PostHAEntity(Serial,"","","arcFactI","arcFactI",str(parsed_inverter_json['data']['arcFactI']))
            postapi.PostHAEntity(Serial,"","","acVoltLow","acVoltLow",str(parsed_inverter_json['data']['acVoltLow']))
            postapi.PostHAEntity(Serial,"","","genSignal","genSignal",str(parsed_inverter_json['data']['genSignal']))
            


            
            
            print(ConsoleColor.OKGREEN + "Inverter Settings fetch complete" + ConsoleColor.ENDC)
       
            

        else:
            print("PV data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)  

def GetPvData(Token,Serial):    
    global api_server    
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://{api_server}/api/v1/inverter/$inverter_serial/realtime/input
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/realtime/input"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "PV data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json);
            print("PV Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pac']) + ConsoleColor.ENDC)
            print("PV Grid_tip_power: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['grid_tip_power']) + ConsoleColor.ENDC)
            print("PV Etoday: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etoday']) + ConsoleColor.ENDC)
            print("PV Etotal: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etotal']) + ConsoleColor.ENDC)
            #Post HA entities #Usage: PostHAEntity(UOM,UOMLong,fName,sName,State)
            postapi.PostHAEntity(Serial,"W","current","PV Pac","pv_pac",str(parsed_inverter_json['data']['pac']))
            postapi.PostHAEntity(Serial,"W","current","PV Grid_tip_power","pv_grid_tip_power",parsed_inverter_json['data']['grid_tip_power'])
            postapi.PostHAEntity(Serial,"kWh","energy","PV Etoday","pv_etoday",str(parsed_inverter_json['data']['etoday']))
            postapi.PostHAEntity(Serial,"kWh","energy","PV Etotal","pv_etotal",str(parsed_inverter_json['data']['etotal']))
            
            print(ConsoleColor.WARNING + str(len(parsed_inverter_json['data']['pvIV'])) + ConsoleColor.ENDC +  " MPPTs detected.")
            #Loop through MPPTS
            for x in range(len(parsed_inverter_json['data']['pvIV'])): 
                currentmppt = str(x)
                print(f"PV MPPT {currentmppt} Power: " + ConsoleColor.OKCYAN + parsed_inverter_json['data']['pvIV'][x]['ppv'] + ConsoleColor.ENDC)
                print(f"PV MPPT {currentmppt} Voltage: " + ConsoleColor.OKCYAN + parsed_inverter_json['data']['pvIV'][x]['vpv'] + ConsoleColor.ENDC)
                print(f"PV MPPT {currentmppt} Current: " + ConsoleColor.OKCYAN + parsed_inverter_json['data']['pvIV'][x]['ipv'] + ConsoleColor.ENDC)
                #Post HA entities #Usage: PostHAEntity(UOM,UOMLong,fName,sName,State)
                postapi.PostHAEntity(Serial,"W","power",f"PV MPPT {currentmppt} Power",f"pv_mppt{currentmppt}_power",parsed_inverter_json['data']['pvIV'][x]['ppv'])
                postapi.PostHAEntity(Serial,"V","voltage",f"PV MPPT {currentmppt} Voltage",f"pv_mppt{currentmppt}_voltage",parsed_inverter_json['data']['pvIV'][x]['vpv'])
                postapi.PostHAEntity(Serial,"A","current",f"PV MPPT {currentmppt} Current",f"pv_mppt{currentmppt}_current",parsed_inverter_json['data']['pvIV'][x]['ipv'])
            
            
            print(ConsoleColor.OKGREEN + "PV fetch complete" + ConsoleColor.ENDC)
       
            

        else:
            print("PV data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)        

def GetGridData(Token,Serial):    
    global api_server   
    inverter_url = f"https://{api_server}/api/v1/inverter/grid/{Serial}/realtime?sn={Serial}"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success": 
            #print(parsed_inverter_json)
            print(ConsoleColor.BOLD + "Grid data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            print(ConsoleColor.WARNING + str(len(parsed_inverter_json['data']['vip'])) + ConsoleColor.ENDC +  " Phase(s) detected.")
            #Loop through phases
            for x in range(len(parsed_inverter_json['data']['vip'])):
                currentphase = str(x)
                print(f"Grid Phase {currentphase} Voltage: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['volt']) + ConsoleColor.ENDC)
                print(f"Grid Phase {currentphase} Current: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['current']) + ConsoleColor.ENDC)
                print(f"Grid Phase {currentphase} Power: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['power']) + ConsoleColor.ENDC)
                postapi.PostHAEntity(Serial,"V","voltage",f"Grid Phase {currentphase} Voltage",f"grid_phase{currentphase}_voltage",parsed_inverter_json['data']['vip'][x]['volt'])
                postapi.PostHAEntity(Serial,"A","current",f"Grid Phase {currentphase} Current",f"grid_phase{currentphase}_current",parsed_inverter_json['data']['vip'][x]['current'])
                postapi.PostHAEntity(Serial,"W","power",f"Grid Phase {currentphase} Power",f"grid_phase{currentphase}_power",parsed_inverter_json['data']['vip'][x]['power'])                
                
                
            print("Grid Pac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pac']) + ConsoleColor.ENDC)
            print("Grid Qac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['qac']) + ConsoleColor.ENDC)
            print("Grid Fac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['fac']) + ConsoleColor.ENDC)
            print("Grid Pf: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pf']) + ConsoleColor.ENDC)
            print("Grid Status: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['status']) + ConsoleColor.ENDC)
            print("Grid AcRealyStatus: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['acRealyStatus']) + ConsoleColor.ENDC)
            print("Grid EtodayFrom: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etodayFrom']) + ConsoleColor.ENDC)
            print("Grid EtodayTo: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etodayTo']) + ConsoleColor.ENDC)
            print("Grid EtotalFrom: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etotalFrom']) + ConsoleColor.ENDC)
            print("Grid EtotalTo: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etotalTo']) + ConsoleColor.ENDC)
            print("Grid LimiterPowerArr: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['limiterPowerArr']) + ConsoleColor.ENDC)
            print("Grid LimiterTotalPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['limiterTotalPower']) + ConsoleColor.ENDC)
            
            postapi.PostHAEntity(Serial,"W","power","Grid Power AC","grid_pac",str(parsed_inverter_json['data']['pac']))
            postapi.PostHAEntity(Serial,"W","power","Grid Reactive Power","grid_qac",str(parsed_inverter_json['data']['qac']))
            postapi.PostHAEntity(Serial,"Hz","frequency","Grid Frequency","grid_fac",str(parsed_inverter_json['data']['fac']))
            postapi.PostHAEntity(Serial,"W","power","Grid Power Factor","grid_pf",str(parsed_inverter_json['data']['pf']))            
            postapi.PostHAEntity(Serial,"","","Grid Status","grid_status",str(parsed_inverter_json['data']['status']))
            postapi.PostHAEntity(Serial,"","","Grid AC Relays Status","grid_acrelay_status",str(parsed_inverter_json['data']['acRealyStatus']))
            
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etoday From","grid_etoday_from",str(parsed_inverter_json['data']['etodayFrom']))
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etoday To","grid_etoday_to",str(parsed_inverter_json['data']['etodayTo']))
            
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etotal From","grid_etotal_from",str(parsed_inverter_json['data']['etotalFrom']))
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etotal To","grid_etotal_to",str(parsed_inverter_json['data']['etotalTo']))
            postapi.PostHAEntity(Serial,"W","power","Grid limiter Total Power","grid_limiter_total_power",str(parsed_inverter_json['data']['limiterTotalPower']))
            
            print(ConsoleColor.OKGREEN + "Grid fetch complete" + ConsoleColor.ENDC)

            
            

        else:
            print("Grid data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)                

def GetBatteryData(Token,Serial):  
    global api_server  
    inverter_url = f"https://{api_server}/api/v1/inverter/battery/{Serial}/realtime?sn={Serial}&lan=en"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success": 
            #print(parsed_inverter_json)
            print("Battery Time: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['time']) + ConsoleColor.ENDC)
            print("Battery EtodayChg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etodayChg']) + ConsoleColor.ENDC)
            print("Battery EtodayDischg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etodayDischg']) + ConsoleColor.ENDC)
            print("Battery EmonthChg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['emonthChg']) + ConsoleColor.ENDC)
            print("Battery EmonthDischg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['emonthDischg']) + ConsoleColor.ENDC)
            print("Battery EyearChg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['eyearChg']) + ConsoleColor.ENDC)
            print("Battery EyearDischg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['eyearDischg']) + ConsoleColor.ENDC)
            print("Battery EtotalChg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etotalChg']) + ConsoleColor.ENDC)
            print("Battery EtotalDischg: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['etotalDischg']) + ConsoleColor.ENDC)
            print("Battery Type: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['type']) + ConsoleColor.ENDC)
            print("Battery Power: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['power']) + ConsoleColor.ENDC)
            print("Battery Capacity: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['capacity']) + ConsoleColor.ENDC)
            print("Battery CorrectCap: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['correctCap']) + ConsoleColor.ENDC)
            print("Battery BmsSoc: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bmsSoc']) + ConsoleColor.ENDC)
            print("Battery BmsVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bmsVolt']) + ConsoleColor.ENDC)
            print("Battery BmsCurrent: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bmsCurrent']) + ConsoleColor.ENDC)
            print("Battery BmsTemp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bmsTemp']) + ConsoleColor.ENDC)
            print("Battery Current: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current']) + ConsoleColor.ENDC)
            print("Battery Voltage: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['voltage']) + ConsoleColor.ENDC)
            print("Battery Temp: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['temp']) + ConsoleColor.ENDC)
            print("Battery Soc: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['soc']) + ConsoleColor.ENDC)
            print("Battery ChargeVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeVolt']) + ConsoleColor.ENDC)
            print("Battery DischargeVolt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeVolt']) + ConsoleColor.ENDC)
            print("Battery ChargeCurrentLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeCurrentLimit']) + ConsoleColor.ENDC)
            print("Battery DischargeCurrentLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeCurrentLimit']) + ConsoleColor.ENDC)
            print("Battery MaxChargeCurrentLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['maxChargeCurrentLimit']) + ConsoleColor.ENDC)
            print("Battery MaxDischargeCurrentLimit: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['maxDischargeCurrentLimit']) + ConsoleColor.ENDC)
            print("Battery Bms1Version1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bms1Version1']) + ConsoleColor.ENDC)
            print("Battery Bms1Version2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bms1Version2']) + ConsoleColor.ENDC)
            print("Battery Current2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['current2']) + ConsoleColor.ENDC)
            print("Battery Voltage2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['voltage2']) + ConsoleColor.ENDC)
            print("Battery Temp2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['temp2']) + ConsoleColor.ENDC)
            print("Battery Soc2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['soc2']) + ConsoleColor.ENDC)
            print("Battery ChargeVolt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeVolt2']) + ConsoleColor.ENDC)
            print("Battery DischargeVolt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeVolt2']) + ConsoleColor.ENDC)
            print("Battery ChargeCurrentLimit2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['chargeCurrentLimit2']) + ConsoleColor.ENDC)
            print("Battery DischargeCurrentLimit2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dischargeCurrentLimit2']) + ConsoleColor.ENDC)
            print("Battery MaxChargeCurrentLimit2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['maxChargeCurrentLimit2']) + ConsoleColor.ENDC)
            print("Battery MaxDischargeCurrentLimit2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['maxDischargeCurrentLimit2']) + ConsoleColor.ENDC)
            print("Battery Bms2Version1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bms2Version1']) + ConsoleColor.ENDC)
            print("Battery Bms2Version2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['bms2Version2']) + ConsoleColor.ENDC)
            print("Battery Status: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['status']) + ConsoleColor.ENDC)
            print("Battery BatterySoc1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batterySoc1']) + ConsoleColor.ENDC)
            print("Battery BatteryCurrent1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryCurrent1']) + ConsoleColor.ENDC)
            print("Battery BatteryVolt1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryVolt1']) + ConsoleColor.ENDC)
            print("Battery BatteryPower1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryPower1']) + ConsoleColor.ENDC)
            print("Battery BatteryTemp1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryTemp1']) + ConsoleColor.ENDC)
            print("Battery BatteryStatus2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryStatus2']) + ConsoleColor.ENDC)
            print("Battery BatterySoc2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batterySoc2']) + ConsoleColor.ENDC)
            print("Battery BatteryCurrent2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryCurrent2']) + ConsoleColor.ENDC)
            print("Battery BatteryVolt2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryVolt2']) + ConsoleColor.ENDC)
            print("Battery BatteryPower2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryPower2']) + ConsoleColor.ENDC)
            print("Battery BatteryTemp2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batteryTemp2']) + ConsoleColor.ENDC)
            print("Battery NumberOfBatteries: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['numberOfBatteries']) + ConsoleColor.ENDC)
            print("Battery Batt1Factory: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batt1Factory']) + ConsoleColor.ENDC)
            print("Battery Batt2Factory: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['batt2Factory']) + ConsoleColor.ENDC)
            
            postapi.PostHAEntity(Serial,"","","Battery time","battery_time",str(parsed_inverter_json['data']['time']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery Etoday Charge","battery_etoday_charge",str(parsed_inverter_json['data']['etodayChg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery Etoday Discharge","battery_etoday_discharge",str(parsed_inverter_json['data']['etodayDischg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery EMonth Charge","battery_emonth_charge",str(parsed_inverter_json['data']['emonthChg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery EMonth Discharge","battery_emonth_discharge",str(parsed_inverter_json['data']['emonthDischg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery Eyear Charge","battery_eyear_charge",str(parsed_inverter_json['data']['eyearChg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery Eyear Discharge","battery_eyear_discharge",str(parsed_inverter_json['data']['eyearDischg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery Etotal Charge","battery_etotal_charge",str(parsed_inverter_json['data']['etotalChg']))
            postapi.PostHAEntity(Serial,"kWh","energy","Battery Etotal Discharge","battery_etotal_discharge",str(parsed_inverter_json['data']['etotalDischg']))
            
            postapi.PostHAEntity(Serial,"","","Battery Type","battery_type",str(parsed_inverter_json['data']['type']))
            postapi.PostHAEntity(Serial,"W","power","Battery Power","battery_power",str(parsed_inverter_json['data']['power']))
            postapi.PostHAEntity(Serial,"Ah","current","Battery Capacity","battery_capacity",str(parsed_inverter_json['data']['capacity']))
            postapi.PostHAEntity(Serial,"Ah","current","Battery Correct Capacity","battery_correct_capacity",str(parsed_inverter_json['data']['correctCap']))
            postapi.PostHAEntity(Serial,"%","battery","Battery BMS SOC","battery_bms_soc",str(parsed_inverter_json['data']['bmsSoc']))
            postapi.PostHAEntity(Serial,"A","current","Battery BMS Voltage","battery_bms_current",str(parsed_inverter_json['data']['bmsCurrent']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery BMS Temperature","battery_bms_temperature",str(parsed_inverter_json['data']['bmsTemp']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Voltage","battery_voltage",str(parsed_inverter_json['data']['voltage']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery Temperature","battery_temperature",str(parsed_inverter_json['data']['temp']))
            postapi.PostHAEntity(Serial,"%","battery","Battery SOC","battery_soc",str(parsed_inverter_json['data']['soc']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Charge Voltage","battery_charge_volt",str(parsed_inverter_json['data']['chargeVolt']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Discharge Voltage","battery_discharge_volt",str(parsed_inverter_json['data']['dischargeVolt']))
            postapi.PostHAEntity(Serial,"A","current","Battery Charge Current Limit","battery_charge_currentlimit",str(parsed_inverter_json['data']['chargeCurrentLimit']))
            postapi.PostHAEntity(Serial,"A","current","Battery Max Charge Current Limit","battery_charge_maxcharge_currentlimit",str(parsed_inverter_json['data']['maxChargeCurrentLimit']))
            postapi.PostHAEntity(Serial,"A","current","Battery Max Discharge Current Limit","battery_charge_maxdischarge_currentlimit",str(parsed_inverter_json['data']['maxDischargeCurrentLimit']))
            postapi.PostHAEntity(Serial,"","","Battery BMS1 Version1","battery_bms1version1",str(parsed_inverter_json['data']['bms1Version1']))
            postapi.PostHAEntity(Serial,"","","Battery BMS1 Version2","battery_bms1version2",str(parsed_inverter_json['data']['bms1Version2']))            
            postapi.PostHAEntity(Serial,"A","current","Battery Current 2","battery_current2",str(parsed_inverter_json['data']['current2']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Voltage 2","battery_voltage2",str(parsed_inverter_json['data']['voltage2']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery Temperature 2","battery_temperature2",str(parsed_inverter_json['data']['temp2']))
            postapi.PostHAEntity(Serial,"%","battery","Battery SOC 2","battery_soc2",str(parsed_inverter_json['data']['soc2']))            
            postapi.PostHAEntity(Serial,"V","voltage","Battery Charge Voltage 2","battery_charge_volt2",str(parsed_inverter_json['data']['chargeVolt2']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Discharge Voltage 2","battery_discharge_volt2",str(parsed_inverter_json['data']['dischargeVolt2']))            
            postapi.PostHAEntity(Serial,"A","current","Battery Charge Current Limit2","battery_charge_currentlimit2",str(parsed_inverter_json['data']['chargeCurrentLimit2']))
            postapi.PostHAEntity(Serial,"A","current","Battery Charge Current Limit2","battery_discharge_currentlimit2",str(parsed_inverter_json['data']['dischargeCurrentLimit2']))            
            postapi.PostHAEntity(Serial,"A","current","Battery Max Charge Current Limit2","battery_maxcharge_currentlimit2",str(parsed_inverter_json['data']['maxChargeCurrentLimit2']))
            postapi.PostHAEntity(Serial,"A","current","Battery Max Charge Current Limit2","battery_maxcharge_currentlimit2",str(parsed_inverter_json['data']['maxDischargeCurrentLimit2']))            
            postapi.PostHAEntity(Serial,"","","Battery BMS2 Version1","battery_bms2version1",str(parsed_inverter_json['data']['bms2Version1']))
            postapi.PostHAEntity(Serial,"","","Battery BMS2 Version2","battery_bms2version2",str(parsed_inverter_json['data']['bms2Version2']))            
            postapi.PostHAEntity(Serial,"","","Battery Status","battery_status",str(parsed_inverter_json['data']['status']))
            postapi.PostHAEntity(Serial,"%","battery","Battery SOC 1","battery_soc1",str(parsed_inverter_json['data']['batterySoc1']))                        
            
            
            postapi.PostHAEntity(Serial,"A","current","Battery Current","battery_current",str(parsed_inverter_json['data']['current']))
            
            postapi.PostHAEntity(Serial,"V","voltage","Battery Voltage 1","battery_voltage1",str(parsed_inverter_json['data']['batteryVolt1']))
            postapi.PostHAEntity(Serial,"W","power","Battery Power 1","battery_power1",str(parsed_inverter_json['data']['batteryPower1']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery Temperature 1","battery_temperature1",str(parsed_inverter_json['data']['batteryTemp1']))
            postapi.PostHAEntity(Serial,"A","current","Battery Current 1","battery_current1",str(parsed_inverter_json['data']['batteryCurrent1']))
            
            postapi.PostHAEntity(Serial,"","","Battery Status 2","battery_status2",str(parsed_inverter_json['data']['batteryStatus2']))
            postapi.PostHAEntity(Serial,"%","battery","Battery SOC 2","battery_soc2",str(parsed_inverter_json['data']['batterySoc2']))
            postapi.PostHAEntity(Serial,"A","current","Battery Current 2","battery_current1",str(parsed_inverter_json['data']['batteryCurrent2']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Voltage 2","battery_voltage1",str(parsed_inverter_json['data']['batteryVolt2']))
            
            postapi.PostHAEntity(Serial,"W","power","Battery Power 2","battery_voltage1",str(parsed_inverter_json['data']['batteryPower2']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery Temperature 2","battery_temperature2",str(parsed_inverter_json['data']['batteryTemp2']))
            postapi.PostHAEntity(Serial,"","","Battery Voltage 2","battery_number_of_batteries",str(parsed_inverter_json['data']['numberOfBatteries']))
            postapi.PostHAEntity(Serial,"","","Battery 1 Factory","battery_batt1_factory",str(parsed_inverter_json['data']['batt1Factory']))
            postapi.PostHAEntity(Serial,"","","Battery 2 Factory","battery_batt2_factory",str(parsed_inverter_json['data']['batt2Factory']))
            
            print(ConsoleColor.OKGREEN + "Battery fetch complete" + ConsoleColor.ENDC)
            
        else:
            print("Battery data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)         
        
def GetLoadData(Token,Serial): 
    global api_server    
    inverter_url = f"https://{api_server}/api/v1/inverter/load/{Serial}/realtime?sn={Serial}"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Load data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json)            
            print(ConsoleColor.WARNING + str(len(parsed_inverter_json['data']['vip'])) + ConsoleColor.ENDC +  " Load(s) detected.")
            #Loop through Load Phases            
            for x in range(len(parsed_inverter_json['data']['vip'])): 
                currentloadphase = str(x)
                print(f"Load {currentloadphase} Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['volt']) + ConsoleColor.ENDC)
                print(f"Load {currentloadphase} Current: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['current']) + ConsoleColor.ENDC)
                print(f"Load {currentloadphase} Power: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['power']) + ConsoleColor.ENDC)    
                postapi.PostHAEntity(Serial,"V","voltage",f"Load Voltage Phase {currentloadphase}",f"load_voltager_phase_{currentloadphase}",parsed_inverter_json['data']['vip'][x]['volt'])
                postapi.PostHAEntity(Serial,"A","current",f"Load Current Phase {currentloadphase}",f"load_current_phase_{currentloadphase}",parsed_inverter_json['data']['vip'][x]['current'])
                postapi.PostHAEntity(Serial,"W","power",f"Load Power Phase {currentloadphase}",f"load_power_phase_{currentloadphase}",parsed_inverter_json['data']['vip'][x]['power'])
                
            
            print("Load totalUsed: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['totalUsed']) + ConsoleColor.ENDC)
            print("Load smartLoadStatus: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['dailyUsed']) + ConsoleColor.ENDC)                
            print("Load totalPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['totalPower']) + ConsoleColor.ENDC)
            print("Load smartLoadStatus: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['smartLoadStatus']) + ConsoleColor.ENDC)
            print("Load loadFac: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['loadFac']) + ConsoleColor.ENDC)
            print("Load upsPowerL1: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['upsPowerL1']) + ConsoleColor.ENDC)
            print("Load upsPowerL2: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['upsPowerL2']) + ConsoleColor.ENDC)
            print("Load upsPowerL3: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['upsPowerL3']) + ConsoleColor.ENDC)
            print("Load upsPowerTotal: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['upsPowerTotal']) + ConsoleColor.ENDC)
            
            postapi.PostHAEntity(Serial,"kWh","energy","Load Total Used","load_total_used",str(parsed_inverter_json['data']['totalUsed']))
            postapi.PostHAEntity(Serial,"kWh","energy","Load Daily Used","load_daily_used",str(parsed_inverter_json['data']['dailyUsed']))
            postapi.PostHAEntity(Serial,"W","power","Load Total Power","load_total_power",str(parsed_inverter_json['data']['totalPower']))
            postapi.PostHAEntity(Serial,"","","Load Smart Load Status","load_smar_load_status",str(parsed_inverter_json['data']['smartLoadStatus']))
            postapi.PostHAEntity(Serial,"Hz","frequency","Load Frequency","load_frequency",str(parsed_inverter_json['data']['loadFac']))
            postapi.PostHAEntity(Serial,"W","power","Load Power L1","load_power_l1",str(parsed_inverter_json['data']['upsPowerL1']))
            postapi.PostHAEntity(Serial,"W","power","Load Power L2","load_power_l2",str(parsed_inverter_json['data']['upsPowerL2']))
            postapi.PostHAEntity(Serial,"W","power","Load Power L3","load_power_l3",str(parsed_inverter_json['data']['upsPowerL3']))
            postapi.PostHAEntity(Serial,"W","power","Load UPS Total Power","load_ups_total_power",str(parsed_inverter_json['data']['upsPowerTotal']))

            print(ConsoleColor.OKGREEN + "Load fetch complete" + ConsoleColor.ENDC) 
            
        else:
            print("Load data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)          
        
def GetOutputData(Token,Serial):
    global api_server   
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/realtime/output"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Output data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json)            
            print(ConsoleColor.WARNING + str(len(parsed_inverter_json['data']['vip'])) + ConsoleColor.ENDC +  " Output Phase(es) detected.")
            #Loop through Load Phases            
            for x in range(len(parsed_inverter_json['data']['vip'])): 
                currentOutput = str(x) 
                print(f"Output {currentOutput} Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['volt']) + ConsoleColor.ENDC)
                print(f"Output {currentOutput} Current: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['current']) + ConsoleColor.ENDC)
                print(f"Output {currentOutput} Power: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['vip'][x]['power']) + ConsoleColor.ENDC)
                postapi.PostHAEntity(Serial,"V","voltage",f"Inverter Voltage Phase {currentOutput}",f"inverter_voltager_phase_{currentOutput}",parsed_inverter_json['data']['vip'][x]['volt'])                
                postapi.PostHAEntity(Serial,"current","current",f"Inverter Current Phase {currentOutput}",f"inverter_current_phase_{currentOutput}",parsed_inverter_json['data']['vip'][x]['current'])
                postapi.PostHAEntity(Serial,"power","power",f"Inverter Power Phase {currentOutput}",f"inverter_power_phase_{currentOutput}",parsed_inverter_json['data']['vip'][x]['power'])
            
            print("Inverter totalPower: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pInv']) + ConsoleColor.ENDC)
            print("Inverter Power AC: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['pac']) + ConsoleColor.ENDC)                
            print("Inverter Frequency: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['fac']) + ConsoleColor.ENDC) 
            postapi.PostHAEntity(Serial,"W","power","Inverter In Power","inverter_in_power",str(parsed_inverter_json['data']['pInv']))
            postapi.PostHAEntity(Serial,"W","power","Inverter Power","inverter_power",str(parsed_inverter_json['data']['pac']))
            postapi.PostHAEntity(Serial,"Hz","frequency","Inverter Frequency","inverter_frequency",str(parsed_inverter_json['data']['fac']))

            print(ConsoleColor.OKGREEN + "Output fetch complete" + ConsoleColor.ENDC)
                
            
        else:
            print("Output data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)         

def GetDCACTemp(Token,Serial):    
    global api_server       
    VarCurrentDate = datetime.today().strftime('%Y-%m-%d')
    #print(VarCurrentDate)
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/output/day?lan=en&date={VarCurrentDate}&column=dc_temp,igbt_temp"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Inverter data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(str(parsed_inverter_json))
            #DC Temp              
            LastRecNum=len(parsed_inverter_json['data']['infos'][0]['records'])-1
            print(f"Inverter Temp UOM: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['infos'][0]['unit']) + ConsoleColor.ENDC) 
            print(f"Inverter DC Temp Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['infos'][0]['records'][LastRecNum]['value']) + ConsoleColor.ENDC)            
            print(f"Inverter AC Temp Volt: " + ConsoleColor.OKCYAN + str(parsed_inverter_json['data']['infos'][1]['records'][LastRecNum]['value']) + ConsoleColor.ENDC)   
            
            postapi.PostHAEntity(Serial,"","","Inverter Temp UOM","inverter_temp_uom",str(parsed_inverter_json['data']['infos'][0]['unit']))
            postapi.PostHAEntity(Serial,"°C","power","Inverter DC Temperature","inverter_dc_temperature",str(parsed_inverter_json['data']['infos'][0]['records'][LastRecNum]['value']))
            postapi.PostHAEntity(Serial,"°C","power","Inverter AC Temperature","inverter_ac_temperature",str(parsed_inverter_json['data']['infos'][1]['records'][LastRecNum]['value']))
            
            print(ConsoleColor.OKGREEN + "DC/AC Temperature fetch complete" + ConsoleColor.ENDC)
            
        else:
            print("Inverter data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)         









