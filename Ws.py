import time
from  bs4 import BeautifulSoup
import requests


print('Put in somes skills')
uf_skill = input('>')
Ufskill=uf_skill
Ufskill=Ufskill.lower()
print(f'Filtering out {uf_skill}')
def find_jobs():
        html_requ=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
        soup = BeautifulSoup(html_requ,'lxml')
        jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
        for index,job in enumerate(jobs):
                publish_d=job.find('span',class_='sim-posted').span.text
                if 'few' in publish_d:
                        comp_name = job.find('h3',class_='joblist-comp-name').text.replace('  ','')
                        skills = job.find('span',class_='srp-skills').text.replace('  ','')
                        more_info=job.header.h2.a['href']
                        if uf_skill and Ufskill not in skills:
                                with open(f'{index}.txt','w') as f:

                                        f.write(f'''
                                        Company Name: {comp_name.strip()}
                                        Required Skills: {skills.strip()}
                                        More Info:{more_info}
                                        \n''')
                                print(f'File saved in :{index}')
if __name__ == '__main__':
        while True:
                find_jobs()
                time_wait=10
                print(f'Waiting...{time_wait}mins Please')
                time.sleep(time_wait* 60)