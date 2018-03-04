# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:43:41 2018

@author: user
"""

import urllib.request
import boto3


def reko_test_init():
    # provide IAM user having programmatic access for AmazonRekognitionReadOnlyAccess
#Account ID or alias: 236128220840
#IAM user name: GroupeAWSAnna
#Password: DSTI2017a

    # externalize credentials, do not hard code them (demo purpose only)

      
        client = boto3.client(
        'rekognition',
        'us-east-1',
        aws_access_key_id='AKIA.......',
        aws_secret_access_key='8......'
    )
        return client

def reko_test_op(fburl,client):    # alternatively image could be read from a local using:
    #  with open('source.jpg', 'rb') as source_image:
    #      source_bytes = source_image.read()

        with urllib.request.urlopen(fburl) as f:
            source_bytes = f.read()

        response = client.detect_faces(Image={'Bytes': source_bytes}, Attributes=['ALL'])

        for faceDetail in response['FaceDetails']:
            # Confidence level that the bounding box contains a face (and not a different object such as a tree).
            # estimated age range (low-high), in years, for a face
            print("Confidence={} AgeRange->Low={} AgeRange->High={}".format(
                faceDetail['Confidence'],
                faceDetail['AgeRange']['Low'],
                faceDetail['AgeRange']['High']))

            # Gender of the face and the confidence level in the determination.
            print("Gender: Confidence={} Genre={}".format(
                faceDetail['Gender']['Confidence'],
                faceDetail['Gender']['Value']))
            
            return (str(faceDetail['Confidence'])+','+
                str(faceDetail['AgeRange']['Low'])+','+
                str(faceDetail['AgeRange']['High'])+','+
                str(faceDetail['Gender']['Confidence'])+','+
                faceDetail['Gender']['Value'])




fin = open("julie.fievez2.csv",'r',encoding = 'utf-8')
fout = open("julie.fievez3.csv",'w',encoding = 'utf-8')
fout.write("FB url,FB ID,Age confidence,Age low,Age High,Gender Conf, Gender\n")
cl=reko_test_init()
for line in fin :  
    aa=line.split(',')    
    myfburl = 'https://graph.facebook.com/'+aa[1][:-1]+'/picture?width=9999&height=9999'
    reponse= reko_test_op(myfburl,cl)
    if reponse == None : reponse = 'No face photo'
    fout.write(aa[0]+','+aa[1][:-1]+','+reponse+"\n")
   
 
fin.close()
fout.close()
 