# 관심 채용정보 크롤링 및 새 게시물 텔레그램 알림 예제
import requests
import json
import datetime
import time
from config import CRAWLING_URL
from telegram_send import send

#크롤링
url = CRAWLING_URL
form_data = {
    'recruitClassSn' : '',
    'recruitClassName' : '',
    'jobnoticeStateCode' : '10',
    'pageSize' : '999',
    'currentPage' : '1'
}
response = requests.post(url, form_data)
source = json.loads(response.text)

results = ''
i = 1
recentNum = 0
notice_up_yn = 0
print('최근 게시물 번호'+str(recentNum))
if source['list'][0]['jobnoticeSn'] != recentNum:
    recentNum = source['list'][0]['jobnoticeSn']
    results = '----- 관심 채용 정보 -----\n\n'
    for row in source["list"]:
     #   if row['jobnoticeName'].find('전산원') != -1 or row['jobnoticeName'].find('정보보안팀') != -1:
     #       results += '전산원' + row['receiptState'] + '\n'

        if row['receiptState'] == '접수중' and (row['jobnoticeName'].find('전산원') != -1 or row['jobnoticeName'].find('정보보안팀') != -1) :
            results += str(i) + '. ' + str(row['jobnoticeSn']) + ' ' + row['recruitTypeName'] + '\n ' + row['jobnoticeName']+ ' ' + row['receiptState'] + '\n ' + str(datetime.date.fromtimestamp(row['applyStartDate']['time']/1000))+ ' ~ ' + str(datetime.datetime.fromtimestamp(row['applyEndDate']['time']/1000))+ ' \n' + "https://yuhs.recruiter.co.kr/app/jobnotice/view?systemKindCode="+row['systemKindCode']+'&jobnoticeSn='+str(row['jobnoticeSn']) + '\n\n' 
            i += 1
            notice_up_yn == 1
            
if notice_up_yn == 1 :
    send(results)
else :
    results += '전산 공고 없음\n'
print(results)

    
