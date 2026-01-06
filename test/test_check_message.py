from hl7_parser.check_message import checkMessageType
from hl7_parser.check_message import checkSegments


'''
Will get error if the message body miss any segment
among MSH, SCH, PID or PV1
'''
def test_checkSegments():
    
    assert checkSegments('./sample_data/sample_missing_seg.hl7') == "Required HL7 segment is missing!"


'''
Will get error if the message type is not SIU^S12
'''
def test_checkMessageType():

    assert checkMessageType('./sample_data/sample_invalid_msg.hl7') == "Message type is not SIU^S12"

