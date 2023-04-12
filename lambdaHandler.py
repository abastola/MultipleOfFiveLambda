import json
import os
import sys
import time

def lambda_handler(event, context):
    response = {}
    for i in range(10):
        response[i] = i*5
    print(event) #This sends event body {TPS, Interval, Iteration} to cloudwatch [Important for data analytics]
    return {
        'statusCode': 200,
        'body': {}
    }


#CloudWatch Query
'''
fields @timestamp as Timestamp, body, @requestId, requestContext.requestId, @initDuration as ColdStartDurationInMS, @duration as DurationInMS, @billedDuration as BilledDurationInMS, @memorySize/1000000 as MemorySetInMB, @maxMemoryUsed/1000000 as MemoryUsedInMB
| sort @timestamp asc
| filter ispresent(@duration) or ispresent(requestContext.requestId) 
| limit 4050
'''

