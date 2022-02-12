from bs4 import BeautifulSoup


class AdvertisementPageParser:
    def parse(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(
            title=None, price=None, body=None, post_id=None, 
            craeted_items=None, modified_items=None, 
        )
        title_tag = soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            data['title'] = title_tag.text
        
        price_tag = soup.find('span', attrs={'class': 'price'})
        if price_tag:
            data['price'] = price_tag.text
        
        body_tag = soup.select_one('#postingbody')
        if body_tag:
            data['body'] = body_tag.text
        
        
        return data