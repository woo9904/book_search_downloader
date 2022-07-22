from selenium import webdriver
import time
import requests
import re
from bs4 import BeautifulSoup
import tkinter.ttk as ttk
from tkinter import *
import sys, os, time


def do_search():
    search=search_entry.get()
    number=option_entry.get()
    headers={}#add your user-agent
    #최신순 으로 검색 정렬은
    url="https://link.springer.com/search?query="+search+'&facet-content-type="Chapter"&sortOrder=newestFirst'

    #아니면 최신순 관련도 순으로 하려면
    url="https://link.springer.com/search?query="+search

    #페이지 이동
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")
    results=soup.find("ol", attrs={"id":"results-list"}).find_all("h2")
    #print(results)
    num=0
    doi_list=[]
    title_list=[]
    for i in results:
        num+=1
        if num==int(number)+1:
            break
        link="https://link.springer.com"+i.find("a", attrs={"class":"title"})["href"] #링크 추출 (Doi 얻기 위해서)
        #print(link)

        #title=i.find("a", attrs={"class":"title"}).get_text() #제목 추출
        

        res1=requests.get(link, headers=headers)
        res1.raise_for_status()
        soup=BeautifulSoup(res1.text, "lxml")
        #book_link="https://link.springer.com"+soup.find("a", attrs={"class":"test-cover-link"})["href"]+"#about" #필요 없음
        #이거 안먹힘. 다른방법
        #doi=soup.find("span", attrs={"id":"doi-url"}).get_text().split("_")[0]
        try:
            title=soup.find("a", attrs={"class":"unified-header__link"}).get_text()
        except AttributeError:
            try :
                title=soup.find("a", attrs={"class":"c-chapter-book-details__title"}).get_text()
            except AttributeError:
                title=i.find("a", attrs={"class":"title"}).get_text() #제목 추출

        #print(title)

        title_list.append(title)

        #doi="https://doi.org/"+link.split("/chapter/")[-1]
        doi=link.split("/")[-2:]
        doi="/".join(doi)
        #print(doi)
        doi_list.append(doi)

    result_list.delete(0,END)
    for x in title_list:
        result_list.insert(END, x)

    #책 검색
    options=webdriver.ChromeOptions()
    options.add_argument("widow-size=1920*1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36") #유저 에이전트 확인 필요

    #이방법은 통합 exe파일을 만들기 위한 방법
    # if chkvar.get()==0:
    #     options.add_experimental_option('prefs', {
    #     "download.prompt_for_download": False, #To auto download the file
    #     "download.directory_upgrade": True,
    #     "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    #     })

    # if getattr(sys, 'frozen', False):
    #     chromedriver_path=os.path.join(sys._MEIPASS, "chromedriver.exe")
    #     browser=webdriver.Chrome(chromedriver_path, options=options)
    # else:
    #     browser=webdriver.Chrome(options=options)

    #기본 방법
    browser=webdriver.Chrome("chromedriver.exe",options=options)

    browser.maximize_window() #창 최대화
    sci_hub="https://sci-hub.mksa.top/"

    for i in doi_list:
        browser.execute_script("window.open('{}')".format(sci_hub+i))

root=Tk()
root.title("book downloader")

option_frame=Frame(root)
option_frame.grid(row=0, column=0)

Label(option_frame, text="검색할 개수를 입력해주세요. \n (기본값:10, 최댓값:20) \n큰 숫자일 경우 서버에서 거부하거나 렉의 주범이 될수도 있습니다.").pack(padx=5, pady=5)
option_entry=Entry(option_frame)
option_entry.insert(0,"10")
option_entry.pack(padx=5, pady=5)

search_frame=Frame(root)
search_frame.grid(row=0, column=1)

Label(search_frame, text="검색어를 입력해주세요.").pack(padx=5, pady=5)
search_entry=Entry(search_frame)
search_entry.pack(padx=5, pady=5, side="left")

Button(search_frame, text="검색", command=do_search, padx=5, pady=5, width=10).pack(padx=5, pady=5, side="right")


result_frame=LabelFrame(root, text="검색결과(검색 제목)")
result_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

scrollbar=Scrollbar(result_frame)
scrollbar.pack(fill="y", side="right",padx=5, pady=5)
result_list=Listbox(result_frame, selectmode="extended",width=100, height=15, yscrollcommand=scrollbar.set)
result_list.pack(side="left")
scrollbar.config(command=result_list.yview)

chkvar=IntVar()  #chkvar에 int형으로 값을 저장한다
chkbox=Checkbutton(root, text="문서 내용 미리 보기", variable=chkvar)  #체크했을 때 값을 저장한다. 꼭 필요한 함수라 함
chkbox.select()
chkbox.grid(row=2, column=0, columnspan=2, sticky=E, padx=5, pady=5)

root.mainloop()

