import requests
import csv
from pathlib import Path
from lxml import html
import re

# 常量
TMDB_BASE_URL = 'https://www.themoviedb.org'
TMDB_TOP_URL = 'https://www.themoviedb.org/movie/top-rated'     #第一页的电影榜单url
TMDB_TOP_URL_2 = 'https://www.themoviedb.org/discover/movie/items'      #第二页之后
MOVIE_LIST_FILE = 'movie_list.csv'
BASE_DIR = Path(__file__).parent

# 获取电影详情数据
def get_movie_info(url):
    # 发送请求，获取数据
    print(f'发送请求{url}，获取电影详情数据')
    movie_response = requests.get(url,timeout=60)
    # 解析数据，获取详情
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_names = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    # 电影年份
    movie_years = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    # 电影上映时间
    movie_dates = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class = "release"]/text()')
    # 电影标签
    movie_tags = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class = "genres"]/a/text()')
    # 电影时长
    movie_times = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class = "runtime"]/text()')
    # 评分
    movie_scores = movie_doc.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    # 语言
    movie_languages = movie_doc.xpath(
    '//section[contains(@class,"facts") and contains(@class,"left_column")]'
    '//p[strong[normalize-space(.)="默认语言"]]'
    '/strong/following-sibling::text()[1]'
)
    # 导演
    movie_directors = movie_doc.xpath(
    '//ol[contains(@class,"people")]/li[p[contains(@class,"character") and contains(normalize-space(.),"Director")]]/p/a/text()'
)
    # 作者
    movie_authors = movie_doc.xpath(
    '//ol[contains(@class,"people")]/li[p[contains(@class,"character") and contains(normalize-space(.),"Writer")]]/p/a/text()'
)
    # 简介
    movie_description = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
    # 返回电影详情——返回为字典
    movie_info = { 
        '电影名':movie_names[0].strip() if movie_names else '',
        '年份':get_movie_years(movie_years),
        '上映时间':get_movie_dates(movie_dates),
        '类型':",".join(movie_tags) if movie_tags else '',
        '时长(min)':get_movie_times(movie_times),
        '评分':movie_scores[0].strip() if movie_scores else '',
        '语言':movie_languages[0].strip() if movie_languages else '',
        '导演':",".join(movie_directors) if movie_directors else '',
        '作者':",".join(movie_authors) if movie_authors else '',
        '简介':movie_description[0].strip() if movie_description else '',
    }
    return movie_info

def get_movie_years(movie_years):
    movie_year = movie_years[0].strip() if movie_years else ''
    match = re.search(r'\d{4}', movie_year)
    return match.group() if match else ''

def get_movie_dates(movie_dates):
    movie_date = movie_dates[0].strip() if movie_dates else ''
    return re.search(r'\d{4}-\d{2}-\d{2}',movie_date).group()

def get_movie_times(movie_times):
    movie_time = movie_times[0].strip() if movie_times else ''
    h = re.search(r'(\d+)h',movie_time)
    m = re.search(r'(\d+)m',movie_time)
    h = int(h.group(1)) if h else 0
    m = int(m.group(1)) if m else 0
    return h * 60 + m


# 将数据保存为csv文件函数
def save_movies_to_csv(movies,output_dir = BASE_DIR / 'csv_data'):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    with open (output_dir / MOVIE_LIST_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['电影名','年份','上映时间','类型','时长(min)','评分','语言','导演','作者','简介'])
        writer.writeheader()
        writer.writerows(movies)
                                                                                 
# 主函数                                                                         
def main():
    all_movies = []                                                                      
    for page in range(1,16):
        if page == 1:
            # 发送请求                                                                   
            response = requests.get(TMDB_TOP_URL,timeout=60)                  
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     f'air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-04-17&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated',
                                     timeout=60)
        # 解析数据
        doc = html.fromstring(response.text)
        movie_urls = doc.xpath('//div[@class = "flex flex-wrap w-full"]/a/@href')
        # 遍历电影列表，获取电影详情数据
        for url in movie_urls:
            if url:
                # 获取电影详情url地址
                movie_info_url = TMDB_BASE_URL + url
                # 发送请求，获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)
    # 将数据保存为csv文件
    print('将获取到的所有数据保存为csv文件')
    save_movies_to_csv(all_movies)

if __name__ == '__main__':
    main()