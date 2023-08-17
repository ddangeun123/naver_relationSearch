import requests
from bs4 import BeautifulSoup
import urllib.parse

from selenium.webdriver import Chrome


class Crawler():

    def __init__(self) -> None:
        
        pass
    def GetCookie(self):
        driver = Chrome()
        driver.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%82%B0%EC%95%88&oquery=%EC%95%88%EC%82%B0&tqi=iLNhTlp0J14ssK3RWoRssssste0-175832')
        return driver.get_cookies()
    
    def GetHtml(self, url:str):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        cookie = self.GetCookie()
        cookies = {'Cookie': cookie}
        try:
            res = requests.get(url, headers=headers, cookies=cookies)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                return soup
            else:
                print(f'Error Code : {res.status_code}')
                soup = BeautifulSoup(res.text, 'html.parser')
                return soup
        except Exception as e:
            print(f'Error {e}')
            return 'error'

    def encode_to_utf8(self, input_string):
        encoded_string = urllib.parse.quote(input_string)
        return encoded_string

    def GetData(self, keyword:str):
        base_url = 'https://search.naver.com/search.naver'
        query = self.encode_to_utf8(keyword)
        tail_url = 'tqi=iLibplp0Yidssc3Qco4ssssss08-144619'
        query_string = f'sm=tab_hty.top&where=nexearch&query={query}&{tail_url}' #iL4dKsp0J1ZssUC3ncdssssstfN-421523
        url = base_url+'?'+query_string
        doc = self.GetHtml(url)
        
        data_elements = doc.select('#nx_right_related_keywords > div > div.related_srch > ul > li > a > div')
        # populor_contents_selector = (f'#main_pack > section:nth-child(32) > div > div > div.api_pcpg_wrap > div.api_flicking_wrap.group_popular_block._au_conveyer_container > div:nth-child({}) > a > div > div.dsc_area > div')
        popular_elements = doc.select('#main_pack > section:nth-child(32) > div > div > div.api_pcpg_wrap > div.api_flicking_wrap.group_popular_block._au_conveyer_container > div')
        results = []
        for de in data_elements:
            results.append(de.text)
        

        if len(results)==0:
            results.append("관련검색어가 없습니다.")
        data = {
            'keyword':keyword,
            'result':results
        }
        # print(data)
        return data

    if __name__ =='__main__':
        GetData('카페인')
