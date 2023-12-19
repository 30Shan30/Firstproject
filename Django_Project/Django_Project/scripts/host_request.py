import os
import subprocess
from api.models import *

##This line 69 until 89 only currently only insert into host,hostparameter but i trigger again same value it insert as new entry into hostparameter table.
### i would like to know before insert/update into host and hostparameter table , i would like to check the data exist or not 
# if data exists 
## Modified_at (only there is changes and insert new entry will be django auto defined date and time )
##FIRST json request trigger at Dec. 12, 2023, 3 a.m.
# {
#     "rawdata": [
#         {
#             "cmdbid": "CMDB32489720670",
#             "name": "MKZSQLT99",
#             "product": "testproduct"
#             "cmdb": {
#                 "ci_name":          ["first_test_trigger"],
#                 "serial_number":    ["MKZSQLT99_Isecure"]
#             }
#         }
#     ]
# }


    #first check data exist if not insert  into host table

    # CMDBID            NAME        PRODUCT         MODIFIED AT             MODIFIED BY
    # CMDB32489720670	MKZSQLT99	testproduct	    Dec. 12, 2023, 3 a.m.	shan


    #first  check data exist if not insert hostparameter table
    # ID    FK                  PARAMETER_SECTION   PARAMETER           PARAMETER_INDEX     VALUE               MODIFIED_AT             MODIFIED BY
    # 129	CMDB32489720670	    cmdb                serial_number	    0	                MKZSQLT99_Isecure	Dec. 12, 2023, 3 a.m.	shan
    # 128	CMDB32489720670	    cmdb	            ci_name             0	                first_test_trigger	Dec. 12, 2023, 3 a.m.	shan
    ######


##Second request trigger at Dec. 15, 2023, 8 a.m.
# {
#     "rawdata": [
#         {
#             "cmdbid": "CMDB32489720670",
#             "name": "MKZSQLT99",
#             "product": "testproduct"
#             "cmdb": {
#                 "ci_name":          ["first_test_trigger"],
#                 "serial_number":    ["MKZSQLT99_IsecureTest"],
#                 "child_dependency": ["CMDB0987654321","CMDB1233465688"]
#             }
#         }
#     ]
# }

    ## second request: check there is same value given by request never update modified_at because there is no update in host table skip update.

        # CMDBID            NAME        PRODUCT         MODIFIED AT             MODIFIED BY
        # CMDB32489720670	MKZSQLT99	testproduct	    Dec. 12, 2023, 3 a.m.	shan


        #second request : update hostparameter table (only update value has been change for MKZSQLT99_IsecureTest where CMDB32489720670,cmdb,serial_number )
        ## insert new entry child_dependency data not exist at all 

        # ID    FK                  PARAMETER_SECTION   PARAMETER           PARAMETER_INDEX     VALUE                   MODIFIED_AT             MODIFIED BY
        # 129	CMDB32489720670	    cmdb                serial_number	    0	                MKZSQLT99_IsecureTest	Dec. 15, 2023, 8 a.m.	shan
        # 128	CMDB32489720670	    cmdb	            ci_name             0	                first_test_trigger	    Dec. 12, 2023, 3 a.m.	shan
        # 130	CMDB32489720670	    cmdb	            child_dependency    0	                CMDB0987654321	        Dec. 15, 2023, 8 a.m.	shan       
        # 131	CMDB32489720670	    cmdb	            child_dependency    1	                CMDB1233465688	        Dec. 15, 2023, 8 a.m.	shan                
        ######


def host_request(data):
    
    try :
        for item in data:
            Host.objects.create(cmdbid = item['cmdbid'], name = item['name'],product = item['product'],modified_at = item['modified_at'],modified_by = item['modified_by'])
            r = Host.objects.get(cmdbid=item['cmdbid'])
            if item['cmdb']:
                for key, value in (item['cmdb'].items()):
                        for i in range(len(value)):
                            HostParameter.objects.create(fk=r, parameter_section='cmdb',
                                                    parameter=key, parameter_index=i,
                                                    value=value[i],
                                                    modified_at=item['modified_at'],
                                                    modified_by=item['modified_by']
                                                    )
                print(item['cmdb'].items())
                response_data={"error":False,"Message":"Updated Successfully"}
    except:
        response_data = {"error": True, "Message": "Failed to Update Data"}
        return response_data
    return True

