# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import csv
from googleapiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    apiname = "youtube"
    apiver = "v3"
    key = "YOUR_CLIENT_SECRET_FILE.json"

    #Gets the developer key from an environment variable. You need to set one using your own developer key.
    youtube = build(apiname, apiver,
    developerKey=os.getenv("YOUTUBE_DEVELOPER_KEY"))


    #Builds the request using video ids.

    request = youtube.videos().list(
        part="statistics,snippet",
        #Vídeos iniciais
        #id="yHF-9etoZyA,ymknJKeFoLY,cMJZtGIhCqE,E1hFLpqf1AM,8rYPoLvHW_A,AczvqfirMRM,RG_pMMxf6rk,zi_IOv7Oc_o,yPzP8AllF7A,aNlZfBREjSs,hzZmoHU7cN0,yv8HUagtV_w,Tpm7X17oKa4,NuHoGT23VlQ,3x3EETpfSZI,Wp7xf1BQXBA,dCBULlO0gDQ,OxxMMlK7Hhw,08yUsTWwSP8,Rm6iIHfh-7o,lmHKZoPY-g0,rkw8BuCQSbw,zzZmzn3ynhc,_3UAXQcrbGM,pzPNtYeRTvg,S3YrDEW-l4Q,X9kHwMw8cio,29aAaRHGb7E,H0U9l3q4p68,He1AiTaEyPU,RayhKM1NsIc,hF58Z87b-ro,0iW6s4XGQS0,rNrHSaI9QL8,oYAWgJwuEOM,9rhWvc_ttJI,A3vIAguMG6Q,n2gNkXm6BhY,rSH-2gz_aIs,iN-uXRLJ-58"
        #Vídeos PCO
        #id="tPJzm39kmoQ,fiGwu1aXNfw,t8QAkme6m8M,QwCbJSV49nk,O3sp5Qphl8A,7CccNuwDjfY,Rw57unxzcGs,khWe-Zhx2HY,U1_limKscyE,az4Am6P3ksY,9n59NlPpWWE,NgkeoiRCDbo,CCIKouQ1ttc,ZQoIvLf-Kb8,a5TjKzcdGuM,eu-HbrDVn4Y,aSPua88KoDU,mYgcEcJO4RQ"    )
        #Videos DCTV
        id="xOFKSxXx_Dc,EMm1nPzChyI,tXntAHuKaaU,zyO3L6OZp84,FW8XRUXhcZI,ZLLoBaxp3Ok,w-ZVY2mm6GU,elXImOSUr0Q,qvfHyXuiB8w,a7KlRMEgOvY,4OgVyKCjeKI,0TAyrBibNFQ,lqbS2fVaZCE,g7cB5MExYuI,EfjUDCPma2k,tUQct2S46pc,9p_6pZCYVok,dGYrMh-VhAw,iMF7XbefzXg,HSIaTLgr2bU")
    response = request.execute()

    #Creates a csv file to store some data from the videos: id, title and view count.

    i = 0
    with open('videos.csv', 'w', newline='') as csv_file:
        fieldnames = ["Numero","id", "Titulo", "Views"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for data in response['items']:
            i+=1
            print(data['id'],data['snippet']['title'],data['statistics']['viewCount']);
            writer.writerow({"Numero": i, "id": data['id'],"Titulo": data['snippet']['title'], "Views": data['statistics']['viewCount']})
            # if i == 40:
            #     writer.writerow({})
            #     writer.writerow({"Numero": "-", "id":"-","Titulo": "PCO", "Views": "-"})
            #     writer.writerow({})
            # if i == 58:
            #     writer.writerow({})
            #     writer.writerow({"Numero": "-", "Titulo": "DCTV", "Views": "-"})
            #     writer.writerow({})


if __name__ == "__main__":
    main()