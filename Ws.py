import time
from  bs4 import BeautifulSoup
import requests
from csv import writer


url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
print('Put in somes skills')
uf_skill = input('>')
Ufskill=uf_skill
Ufskill=Ufskill.lower()
print(f'Filtering out {uf_skill}')
def find_jobs():
        html_req=requests.get(url).text
        soup = BeautifulSoup(html_req,'lxml')
        jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
        for index,job in enumerate(jobs):
                publish_d=job.find('span',class_='sim-posted').span.text
                if 'few' in publish_d:
                        comp_name = job.find('h3',class_='joblist-comp-name').text.replace('  ','')
                        skills = job.find('span',class_='srp-skills').text.replace('  ','')
                        more_info=job.header.h2.a['href']
                        with open('jobs.csv','w',encoding='utf8',newline='') as f:
                                thewrit=writer(f)
                                header=['Company Name','Required Skills','More Info']
                                thewrit.writerow(header)
                                if uf_skill and Ufskill not in skills:
                                        f.write(f'''
                                                Company Name: {comp_name.strip()}
                                                Required Skills: {skills.strip()}
                                                More Info:{more_info}
                                                \n''')
if __name__ == '__main__':
        while True:
                find_jobs()
                time_wait=10
                print(f'Waiting...{time_wait}mins Please')
                time.sleep(time_wait* 60)
'''
with open(f'{index}.txt','w') as f:
f.write(f
Company Name: {comp_name.strip()}
Required Skills: {skills.strip()}
More Info:{more_info}
\n)
print(f'File saved in :{index}')
'''