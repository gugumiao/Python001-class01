from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
    'webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '__mta=143366410.1593345786311.1593353020368.1593354134283.8; uuid_n_v=v1; uuid=51EBF720B93711EA9736CB82F1E069892ADF6E73284E49EB82304B4C6A33EA65; _csrf=12afee980c61d1edf46e8fd80059bba62585c23f95fa7024931801e5274cecc1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593345786; _lxsdk_cuid=172facf3f8ac8-04a9f54ae05617-31617402-c0000-172facf3f8bc8; _lxsdk=51EBF720B93711EA9736CB82F1E069892ADF6E73284E49EB82304B4C6A33EA65; mojo-uuid=32d9d9fa2e20455760fbf35e6b4ec6ea; mojo-session-id={"id":"15fa8bc46b610421c4778c9565b3d78c","time":1593352155377}; mojo-trace-id=10; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593354199; __mta=143366410.1593345786311.1593354134283.1593354199355.9; _lxsdk_s=172fb3059dc-85-44b-6ba%7C%7C17',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit'
    '/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

url = 'https://maoyan.com/films?showType=3'

try:
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    response.encoding = 'utf8'
    bs_info = bs(response.text, 'html.parser')
except Exception as e:
    print(e)

urls = []
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    for a in tags.find_all('a'):
        href = 'https://maoyan.com' + a.get('href')
        urls.append(href)

urls = urls[:10]
titles = []
types = []
dates = []


def func(url):
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    response.encoding = 'utf8'
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('h1', attrs={'class': 'name'}):
        titles.append(tags.text)
    movie = []
    for tags in bs_info.find_all('li', attrs={'class': 'ellipsis'}):
        movie.append(tags.text.split())
    types.append('/'.join(movie[0]))
    dates.append(movie[-1][0][:10])


for url in urls:
    func(url)

movies = {'电影名称': titles, '电影类型': types, '上映时间': dates}
df = pd.DataFrame(data=movies)
df.to_csv('./movies.csv', encoding='utf8', index=False, header=False)
