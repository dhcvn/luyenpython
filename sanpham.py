import scrapy

class sanphamSpider(scrapy.Spider):
    name='sanpham'
    start_urls = ["https://www.bachhoaxanh.com/"]
    
    def __init__(self):
        self.alldanhmuc = "ul.colmenu-ul div.parent a"
        
    
    def parse(self,response):
        for a in response.css(self.alldanhmuc):
            yield response.follow(a, callback=self.parse_slsp)
        
    def parse_slsp(self, response):
        def extract_with_css(query):
            return listproduct.css(query).get(default='').strip()
        def extract_danhmuccon(path):
            return response.css(path).get(default='').strip()
        for listproduct in response.css("ul.cate li"):
            if listproduct.css("div.product-name")!=[]:
                yield {
                    'danhmuccon': extract_danhmuccon("h1::text"),
                    'pro_name': extract_with_css("div.product-name::text"),
                    'price': extract_with_css("div.price span::text"),
                    'strong': extract_with_css("div.price strong::text"),
                    'discount': extract_with_css("div.price label::text"),
                    'buynobuy': extract_with_css("a.buy::text")
                }