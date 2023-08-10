import requests
from bs4 import BeautifulSoup
import urllib.parse


class Crawler():

    def __init__(self) -> None:

        pass
    def GetHtml(self, url:str):
        try:
            res = requests.get(url)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                return soup
            else:
                return res.status_code
        except Exception as e:
            print('Error'+e)
            return 'error'

    def encode_to_utf8(self, input_string):
        encoded_string = urllib.parse.quote(input_string)
        return encoded_string

    def GetData(self, keyword:str):
        base_url = 'https://search.naver.com/search.naver'
        query = self.encode_to_utf8(keyword)
        query_string = f'sm=tab_hty.top&where=nexearch&query={query}' #iL4dKsp0J1ZssUC3ncdssssstfN-421523
        url = base_url+'?'+query_string
        print('요청 url :'+url)
        doc = self.GetHtml(url)
        data_elements = doc.select('#nx_right_related_keywords > div > div.related_srch > ul > li > a > div')

        results = []
        for de in data_elements:
            results.append(de.text)
        if len(results)==0:
            results.append("관련검색어가 없습니다.")
        data = {
            'keyword':keyword,
            'result':results
        }
        return data

    if __name__ =='__main__':
        GetData('카페인')
