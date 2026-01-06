from hl7_parser.produce_data import indexOfSegment
from hl7_parser.produce_data import extractSchedule
from hl7_parser.produce_data import extractPatientInfo
from hl7_parser.produce_data import extractProviderInfo

'''
Will get error if the message body miss any segment
among MSH, SCH, PID or PV1
'''
def test_indexOfSegment():
    assert indexOfSegment('./sample_data/sample_missing_seg.hl7') == "Required HL7 segment is missing!"


'''
appointment_id, appointment_reason, iso_time will be None
if the message has any missing segment among
MSH, SCH, PID or PV1
'''
def test_extractSchedule():
    assert extractSchedule('./sample_data/sample_missing_seg.hl7') == (None, None, None) 


'''
patient_id, patient_first_name, patient_last_name, date_of_birth,
patient_gender will be None
if the message has any missing segment among
MSH, SCH, PID or PV1
'''
def test_extractPatientInfo():
    assert extractPatientInfo('./sample_data/sample_missing_seg.hl7') == (None, None, None, None, None)



'''
provider_id, provider_name, provider_location will be None
if the message has any missing segment among
MSH, SCH, PID or PV1
'''
def test_extractProviderInfo():
    assert extractProviderInfo('./sample_data/sample_missing_seg.hl7') == (None, None, None)