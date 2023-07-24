import json
import boto3
from botocore.exceptions import ClientError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

hostName = "localhost"
serverPort = 8080
# Create QuickSight and STS clients
quicksightClient = boto3.client('quicksight',region_name='ap-south-1')
sts = boto3.client('sts')

@app.get("/embedUrl")    
def generateEmbedUrlForRegisteredUser():
    response = quicksightClient.generate_embed_url_for_registered_user(
    AwsAccountId='679995182974',
    SessionLifetimeInMinutes=123,
    UserArn='arn:aws:quicksight:ap-south-1:679995182974:user/default/abhishek@hellochef.com',
    ExperienceConfiguration={
        'Dashboard': {
            'InitialDashboardId': '53229f51-b03c-4336-bc02-c24079e33e61',
            'FeatureConfigurations': {
                'StatePersistence': {
                    'Enabled': True
                }
            }
        },
    },
    )
    embedUrl = response['EmbedUrl']
    return embedUrl
# x = generateEmbedUrlForRegisteredUser()
# print(x)