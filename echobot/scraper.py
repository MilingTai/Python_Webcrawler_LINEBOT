from bs4 import BeautifulSoup as bs
from abc import ABC, abstractmethod #抽象類別(ABC)
import requests

#Food abstract class
class Food(ABC):
    def __init__(self, area):
        self.area=area 
        
    #共同的介面，未來新增的美食網頁爬蟲，就可依據各自的邏輯來實作這個介面。
    @abstractmethod 
    def scrape(self):
        pass

#webscraper 
class IFoodie(Food):#inherit from Food abstract class
    def scrape(self):
        #Use requests to capture data 擷取, 對 url 發出 get request請求
        response =requests.get(
            "https://ifoodie.tw/explore/" + self.area  #地區
            +"/list?sortby=popular&opening=true") #最高人氣 &營業中
        
        #Use BeutifulSoup to parse 解析
        parser_object = bs(response.content, "lxml")
        
        #To get first 5th card data
        cards =parser_object.find_all(
            "div",{"class":'jsx-3292609844 restaurant-item  track-impression-ga'}, limit=5)
       
        content =""
        for card in cards:
            #餐廳名稱 
            title =card.find("a",{"class":"jsx-3292609844 title-text"}).getText()
            #餐廳評價
            stars =card.find("a",{"class":"jsx-1207467136 text"}).getText()
            #餐廳地址
            address =card.find("div",{"class":"jsx-3292609844 avg-price"}).getText()
            
            content += f"{title} \n{stars}顆星 \n{address} \n\n"
        
        return content
    
