from flask import Flask, render_template, jsonify
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from myspider.spiders.myspider import MySpider
from CrawlerScrapy.CrawlerScrapy.spiders.SpiderItoma import MySpider
import threading

app = Flask(__name__)

urls = []

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider)
    try:
        process.start()
    except Exception as e:
        print(f"Error starting Scrapy process: {e}")


def poll_urls():
    global urls
    threading.Timer(1.0, poll_urls).start()
    new_urls = list(MySpider.visited_urls - set(urls))
    urls.extend(new_urls)
    if new_urls:
        print(f"Found {len(new_urls)} new URLs")
        print(new_urls)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_spider")
def start_spider():
    thread = threading.Thread(target=run_spider)
    thread.start()
    return "Spider started"

@app.route("/get_urls")
def get_urls():
    return jsonify(urls)

if __name__ == "__main__":
    poll_urls()
    app.run()