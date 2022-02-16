from bs4 import BeautifulSoup


class AdvertisementPageParser:

    def __init__(self):
        self.soup = None

    @property
    def title(self):
        title_tag = self.soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            return title_tag.text
        return None

    @property
    def price(self):
        price_tag = self.soup.find('span', attrs={'class': 'price'})
        if price_tag:
            return price_tag.text
        return None

    @property
    def body(self):
        body_tag = self.soup.select_one('#postingbody')
        if body_tag:
            return body_tag.text
        return None

    @property
    def post_id(self):
        selector = 'body > section > section > section > div.postinginfos > p:nth-child(1)'
        id_tag = self.soup.select_one(selector)
        if id_tag:
            return id_tag.text.replace('post id: ', '')
        return None

    @property
    def created_time(self):
        time_selector = 'body > section > section > section > div.postinginfos > p:nth-child(2) > time'
        time = self.soup.select_one(time_selector)
        if time:
            return time.attrs['datetime']

    def parse(self, html_data):
        self.soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(
            title=self.title, price=self.price, body=self.body,
            post_id=self.post_id, created_time=self.created_time,
        )
        return data
