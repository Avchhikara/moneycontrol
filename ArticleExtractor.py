import requests
from bs4 import BeautifulSoup

from utils.DateParser import parse_date


def get_article(article_url):
    page = str(requests.get(article_url).content.decode("utf-8", "ignore"))
    soup = BeautifulSoup(page, "html.parser")
    article = {}

    # Getting the article's title
    article["title"] = soup.find(
        attrs={"class": "article_title"}).string.strip()

    # Getting the summary
    article["summary"] = soup.find(
        attrs={"class": "article_desc"}).string.strip()

    # Getting the timestamp
    time_date_element = soup.find(attrs={"class": "article_schedule"})
    time_date_string = ""
    for element in time_date_element.contents:
        if element and element.string.strip():
            time_date_string += element.string.strip()
    article["timestamp"] = parse_date(
        time_date_string
    )

    # Getting article author
    author_element = soup.select_one(".content_block span")
    article["author"] = author_element.string

    # Getting the image url
    article["img_url"] = soup.select_one(".article_image img")["data-src"]

    # Getting the article's content
    content = soup.select(".content_wrapper > p")
    article["content"] = " ".join(
        [c.string for c in content if c.string])
    # Getting all the tags
    tags = soup.select(".tags_first_line > a")
    article["tags"] = [tag.string.strip("#") for tag in tags]

    return article


if __name__ == "__main__":
    urls = [
        "https://www.moneycontrol.com/news/india/india-pushes-back-deadline-for-coal-fired-utilities-to-adopt-new-emission-norms-6723791.html",
        "https://www.moneycontrol.com/news/business/govt-sets-up-7-vehicle-testing-fitness-centres-says-road-ministry-official-6723831.html",
        "https://www.moneycontrol.com/news/business/personal-finance/despite-governments-u-turn-on-small-saving-interest-rates-dont-rush-for-ppf-before-april-5-6722871.html",
        "https://www.moneycontrol.com/news/business/companies/usha-international-sees-rising-interest-for-sewing-machines-among-youngsters-6720641.html"
    ]
    for url in urls:
        article = get_article(url)
        print(article)
