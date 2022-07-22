# book_search_downloader
to search research papers comfortably, add keywords and find papers with chrome automatically.

It is for my father, he often searched reference for study. But lots of data makes my father tired and it took a lot of time.    
I catched father's inconvenience, so I made this program. 

* **제작자 : 정우진(Woo)**
* **제작 일 : 21.04.04**
* **보고서 작성 일 : 22.07.19**


## Description

아버지는 종종 일을 하기 위해 기술 동향을 조사하시거나 관련된 여러 자료를 많이 찾아 읽으신다.    
이때 매번 검색하시고 그 검색하신 자료를 하나하나 읽으신다. 그 과정은 [springer](https://link.springer.com/) 에서 키워드를 검색하신 뒤,    
보고자 하는 서적 및 자료를 찾으시면 해당 doi를 가져가서 [sci-hub](https://sci-hub.mksa.top/)에서 검색을 하신다.    
이때 조사하고자 하는 서적 전문이나, 논문을 얻을 수 있다.    

하지만 매번 이러한 귀찮은 작업이 많아지면서 이 검색으로만 시간을 뺏기고 반복적인 일이다 보니 체력적으로도 힘이 빠지는걸 확인할 수 있었다.   

따라서 이를 알아차리고 좀 더 자료 검색에 쉽게 도와드리기 위해서, 또는 나 또한 자료 조사할 때 유용하게 사용하기 위해서   
다음과 같은 프로그램을 만들게 되었다. 

## Environment
실행에 필요한 package이다.   

* python 3.8.10
* tkinter, bs4, requests
* **selenium (to download latest selenium chromedriver [download_link](https://sites.google.com/chromium.org/driver/)), bs4** 다운받은 chromedriver.exe 폴더 안에 넣기
  
## Files
작성한 코드가 각자 어떤 역할을 하는지 설명해준다. 
* book_downloader.py
	* main 코드. UI와 검색 기능이 포함된 코드이다. 
  * 이때 검색방법이 최신순으로 검색하기, 관련도 순으로 검색하기로 나눌 수 있는데 16번째 코드 라인을 주석처리하면 관련도 순으로 검색 19번째 코드 라인을 주석 처리하면 최신순으로 검색이 가능하다. 
  * bs4로 web scraping을 사용하였고, 결과를 보여주기 위해서는 selenium을 사용하였다. 
	
## Usage
작품을 실행하기 위한 방법에 대해 설명한다.   

1. book_downloader.py를 실행한다. 
2. 검색할 개수와 검색어를 입력한다. 
3. 검색 버튼을 누른 뒤, 기다린다. 
4. 다음과 같이 검색 결과(제목)과 자동으로 창이 켜지면서 문서를 볼 수 있게 된다. 

|(1) 초기 화면 |(2) 데이터 입력 및 결과 |(3) selenium 결과 창|
|--|--|--|
|![nn](/image/main.png)|![nn](/image/result.png)|![nn](/image/web.png)|

추가적으로 검색할 자료가 sci-hub에 없을 수도 있다. 이럴 경우 페이지 화면은 오류 창이 뜨거나 창이 켜지지 않을 수도 있다. 

---------------------------------------------------------

