import boto3



def GuardDuty_ThreatList_Update():
    client = boto3.client('guardduty', region_name="ap-northeast-2", aws_access_key_id=ACCESSKEY, aws_secret_access_key=SECRETKEY)
    TI_LIST = client.list_threat_intel_sets(DetectorId=detectorid, MaxResults=10)

    print(TI_LIST)

    ThreatID = TI_LIST['ThreatIntelSetIds'][0]
    print(ThreatID)
    TI_GET = client.get_threat_intel_set(DetectorId=detectorid, ThreatIntelSetId=ThreatID)
    ThreatName = TI_GET['Name']
    ThreatLocation = TI_GET['Location']
    print(ThreatLocation)
    TI_UPDATE = client.update_threat_intel_set(DetectorId=detectorid, ThreatIntelSetId=ThreatID, Name=ThreatName, Location=ThreatLocation, Activate=True)


if __name__ == '__main__':
    GuardDuty_ThreatList_Update()
