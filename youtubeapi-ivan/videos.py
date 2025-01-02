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


def main(n):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    apiname = "youtube"
    apiver = "v3"
    key = "YOUR_CLIENT_SECRET_FILE.json"

    # Gets the developer key from an environment variable. You need to set one using your own developer key.
    youtube = build(apiname, apiver,
                    developerKey="AIzaSyDYC18PLsHQguqzhKCD0GOabhe49qK2p5I")
    # developerKey=os.getenv("YOUTUBE_DEVELOPER_KEY"))

    # Builds the request using video ids.
    if n == 0:
        videoIds = "yHF-9etoZyA,ymknJKeFoLY,zi_IOv7Oc_o,rSH-2gz_aIs,aNlZfBREjSs,cMJZtGIhCqE,VQZkcCMVTj4,AczvqfirMRM,yv8HUagtV_w,RG_pMMxf6rk,yPzP8AllF7A,3x3EETpfSZI,8rYPoLvHW_A,tFeJyx3vCZs,Wp7xf1BQXBA,hzZmoHU7cN0,OxxMMlK7Hhw,08yUsTWwSP8,X9kHwMw8cio,NuHoGT23VlQ,E1hFLpqf1AM,_3UAXQcrbGM,Tpm7X17oKa4,dCBULlO0gDQ,_3UAXQcrbGM,He1AiTaEyPU,pzPNtYeRTvg,Rm6iIHfh-7o,iN-uXRLJ-58,H0U9l3q4p68,lmHKZoPY-g0,zzZmzn3ynhc,rkw8BuCQSbw,29aAaRHGb7E,RayhKM1NsIc,0iW6s4XGQS0,hF58Z87b-ro,n2gNkXm6BhY,rNrHSaI9QL8,oYAWgJwuEOM,9rhWvc_ttJI,A3vIAguMG6Q"
        name = "videos-aperipe.csv"
    elif n == 1:
        videoIds = "tPJzm39kmoQ,fiGwu1aXNfw,VQZkcCMVTj4,mYgcEcJO4RQ,C_21ghi6grE,t8QAkme6m8M,O3sp5Qphl8A,QwCbJSV49nk,7CccNuwDjfY,khWe-Zhx2HY,U1_limKscyE,aSPua88KoDU,az4Am6P3ksY,9n59NlPpWWE,NgkeoiRCDbo,CCIKouQ1ttc,ZQoIvLf-Kb8,a5TjKzcdGuM,eu-HbrDVn4Y"
        name = "videos-nco.csv"
    elif n == 2:
        videoIds = "EMm1nPzChyI,EfjUDCPma2k,zyO3L6OZp84,xOFKSxXx_Dc,tXntAHuKaaU,FW8XRUXhcZI,elXImOSUr0Q,0TAyrBibNFQ,4OgVyKCjeKI,g7cB5MExYuI,ZLLoBaxp3Ok,tUQct2S46pc,9p_6pZCYVok,w-ZVY2mm6GU,a7KlRMEgOvY,lqbS2fVaZCE,qvfHyXuiB8w,dGYrMh-VhAw,iMF7XbefzXg,HSIaTLgr2bU"
        name = "videos-dctv.csv"
    elif n == 3:
        videoIds = "3bSS6i6wcfg,0TYWAuagax4,JFJeGlxBhvg"
        name = "videos-novos.csv"

    request = youtube.videos().list(

        part="statistics,snippet",
        id=videoIds)
    response = request.execute()

    # Creates a csv file to store some data from the videos: id, title and view count.

    i = 0
    with open(name, 'w', newline='') as csv_file:
        fieldnames = ["Numero", "id", "Titulo", "Views"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for data in response['items']:
            i += 1
            print(data['id'], data['snippet']['title'],
                  data['statistics']['viewCount'])
            writer.writerow(
                {"Numero": i, "id": data['id'], "Titulo": data['snippet']['title'], "Views": data['statistics']['viewCount']})


if __name__ == "__main__":
    main(0)
    main(1)
    main(2)
    main(3)
