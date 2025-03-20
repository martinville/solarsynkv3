import postapi

def GetInverterInfo(Token,Serial):
    import json
    import requests
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m" 
        
    # Inverter URL
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/{Serial}"
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
       
            

        else:
            print("Inverter fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)

def GetPvData(Token,Serial):
    import json
    import requests
    
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m" 
        
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://api.sunsynk.net/api/v1/inverter/$inverter_serial/realtime/input
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/{Serial}/realtime/input"
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
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)        

def GetGridData(Token,Serial):
    import json
    import requests
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"  
        
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://api.sunsynk.net/api/v1/inverter/grid/$inverter_serial/realtime?sn=$inverter_serial -o "griddata.json"
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/grid/{Serial}/realtime?sn={Serial}"
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
                postapi.PostHAEntity(Serial,"V","voltage",f"Grid {currentphase} Voltage",f"grid_phase{currentphase}_voltage",parsed_inverter_json['data']['vip'][x]['volt'])
                postapi.PostHAEntity(Serial,"V","current",f"Grid {currentphase} Current",f"grid_phase{currentphase}_current",parsed_inverter_json['data']['vip'][x]['current'])
                postapi.PostHAEntity(Serial,"V","power",f"Grid {currentphase} Grid",f"grid_phase{currentphase}_power",parsed_inverter_json['data']['vip'][x]['power'])
                 
               
                
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
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etoday To","grid_etotal_to",str(parsed_inverter_json['data']['etodayTo']))
            
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etotal From","grid_etotal_from",str(parsed_inverter_json['data']['etotalFrom']))
            postapi.PostHAEntity(Serial,"kWh","energy","Grid Etotal To","grid_etotal_to",str(parsed_inverter_json['data']['etotalTo']))
            postapi.PostHAEntity(Serial,"W","power","Grid limiter Total Power","grid_limiter_total_power",str(parsed_inverter_json['data']['limiterTotalPower']))
            
            print(ConsoleColor.OKGREEN + "Grid fetch complete" + ConsoleColor.ENDC)

            
            

        else:
            print("Grid data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)                

def GetBatteryData(Token,Serial):
    import json
    import requests
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"  
        
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" "https://api.sunsynk.net/api/v1/inverter/battery/$inverter_serial/realtime?sn=$inverter_serial&lan=en" -o "batterydata.json"
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/battery/{Serial}/realtime?sn={Serial}&lan=en"
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
            postapi.PostHAEntity(Serial,"Ah","current","Battery Capacity","battery_capactiy",str(parsed_inverter_json['data']['capacity']))
            postapi.PostHAEntity(Serial,"Ah","current","Battery Correct Capacity","battery_correct_capactiy",str(parsed_inverter_json['data']['correctCap']))
            postapi.PostHAEntity(Serial,"%","power_tor","Battery BMS SOC","battery_bms_soc",str(parsed_inverter_json['data']['bmsSoc']))
            postapi.PostHAEntity(Serial,"A","current","Battery BMS Voltage","battery_bms_current",str(parsed_inverter_json['data']['bmsCurrent']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery BMS Temperature","battery_bms_temperature",str(parsed_inverter_json['data']['bmsTemp']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Voltage","battery_voltage",str(parsed_inverter_json['data']['voltage']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery Temperature","battery_temperature",str(parsed_inverter_json['data']['temp']))
            postapi.PostHAEntity(Serial,"%","power_tor","Battery SOC","battery_soc",str(parsed_inverter_json['data']['soc']))
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
            postapi.PostHAEntity(Serial,"%","power_tor","Battery SOC 2","battery_soc2",str(parsed_inverter_json['data']['soc2']))            
            postapi.PostHAEntity(Serial,"V","voltage","Battery Charge Voltage 2","battery_charge_volt2",str(parsed_inverter_json['data']['chargeVolt2']))
            postapi.PostHAEntity(Serial,"V","voltage","Battery Discharge Voltage 2","battery_discharge_volt2",str(parsed_inverter_json['data']['dischargeVolt2']))            
            postapi.PostHAEntity(Serial,"A","current","Battery Charge Current Limit2","battery_charge_currentlimit2",str(parsed_inverter_json['data']['chargeCurrentLimit2']))
            postapi.PostHAEntity(Serial,"A","current","Battery Charge Current Limit2","battery_discharge_currentlimit2",str(parsed_inverter_json['data']['dischargeCurrentLimit2']))            
            postapi.PostHAEntity(Serial,"A","current","Battery Max Charge Current Limit2","battery_maxcharge_currentlimit2",str(parsed_inverter_json['data']['maxChargeCurrentLimit2']))
            postapi.PostHAEntity(Serial,"A","current","Battery Max Charge Current Limit2","battery_maxcharge_currentlimit2",str(parsed_inverter_json['data']['maxDischargeCurrentLimit2']))            
            postapi.PostHAEntity(Serial,"","","Battery BMS2 Version1","battery_bms2version1",str(parsed_inverter_json['data']['bms2Version1']))
            postapi.PostHAEntity(Serial,"","","Battery BMS2 Version2","battery_bms2version2",str(parsed_inverter_json['data']['bms2Version2']))            
            postapi.PostHAEntity(Serial,"","","Battery Status","battery_status",str(parsed_inverter_json['data']['status']))
            postapi.PostHAEntity(Serial,"%","power_tor","Battery SOC 1","battery_soc1",str(parsed_inverter_json['data']['batterySoc1']))                        
            postapi.PostHAEntity(Serial,"V","voltage","Battery Voltage 1","battery_voltage1",str(parsed_inverter_json['data']['batteryVolt1']))
            postapi.PostHAEntity(Serial,"W","power","Battery Power 1","battery_power1",str(parsed_inverter_json['data']['batteryPower1']))
            postapi.PostHAEntity(Serial,"°C","temperature","Battery Temperature 1","battery_temperature1",str(parsed_inverter_json['data']['batteryTemp1']))
            postapi.PostHAEntity(Serial,"A","current","Battery Current 1","battery_current1",str(parsed_inverter_json['data']['batteryCurrent1']))
            
            postapi.PostHAEntity(Serial,"","","Battery Status 2","battery_status2",str(parsed_inverter_json['data']['batteryStatus2']))
            postapi.PostHAEntity(Serial,"%","power_tor","Battery SOC 2","battery_soc2",str(parsed_inverter_json['data']['batterySoc2']))
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
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)         
        
def GetLoadData(Token,Serial):
    import json
    import requests
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m" 
        
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://api.sunsynk.net/api/v1/inverter/load/$inverter_serial/realtime?sn=$inverter_serial -o "loaddata.json"
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/load/{Serial}/realtime?sn={Serial}"
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
            postapi.PostHAEntity(Serial,"kWh","energy","Load Total Power","load_total_power",str(parsed_inverter_json['data']['totalPower']))
            postapi.PostHAEntity(Serial,"","","Load Smart Load Status","load_smar_load_status",str(parsed_inverter_json['data']['smartLoadStatus']))
            postapi.PostHAEntity(Serial,"Hz","frequency","Load Frequency","load_frequency",str(parsed_inverter_json['data']['loadFac']))
            postapi.PostHAEntity(Serial,"W","power","Load Power L1","load_power_l1",str(parsed_inverter_json['data']['upsPowerL1']))
            postapi.PostHAEntity(Serial,"W","power","Load Power L2","load_power_l2",str(parsed_inverter_json['data']['upsPowerL2']))
            postapi.PostHAEntity(Serial,"W","power","Load Power L3","load_power_l3",str(parsed_inverter_json['data']['upsPowerL3']))
            postapi.PostHAEntity(Serial,"W","power","Battery time","load_total_power",str(parsed_inverter_json['data']['upsPowerTotal']))

            print(ConsoleColor.OKGREEN + "Load fetch complete" + ConsoleColor.ENDC) 
            
        else:
            print("Load data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)          
        
def GetOutputData(Token,Serial):
    import json
    import requests
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m" 
        
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://api.sunsynk.net/api/v1/inverter/$inverter_serial/realtime/output -o "outputdata.json"
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/{Serial}/realtime/output"
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
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)         

def GetDCACTemp(Token,Serial):
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
        
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" "https://api.sunsynk.net/api/v1/inverter/$inverter_serial/output/day?lan=en&date=$VarCurrentDate&column=dc_temp,igbt_temp" -o "dcactemp.json"
    VarCurrentDate = datetime.today().strftime('%Y-%m-%d')
    #print(VarCurrentDate)
    inverter_url = f"https://api.sunsynk.net/api/v1/inverter/{Serial}/output/day?lan=en&date={VarCurrentDate}&column=dc_temp,igbt_temp"
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
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)         


