import json
from src.main.web_scraping.scraper import *
from src.main.python_logger.py_logger import *


logger = PyLogger.get_logger()


def scrap_companies():
    file = open("resource.json")
    data = json.load(file)
    for company in data["companies"]:
        name = company["companyName"]
        url = company["url"]

        if not company["jobs_list"]["tag"]:
            continue

        try:
            tag = company["jobs_list"]
            jobs = scrape_url(url)
            jobs = jobs.find_all(tag["tag"], {"class": tag["class"], "id": tag["id"]})
            for job in jobs:
                content = scrape_content(str(job))
                path = content.find("a")
                if path is not None:
                    path = path.get("href")
                    link = get_valid_link(path)
                    if not link:
                        link = url + path
                    item = content.get_text().strip().split("\n")
                    item = [itm.strip() for itm in item if len(itm) > 0]
                    logger.info("Job Info: {} \nJob Link: {}\n".format(item, link))
        except Exception as e:
            logger.info("{}".format(e))
            pass


if __name__ == "__main__":
    import time

    start_time = time.time()
    scrap_companies()
    logger.info("Time spent: {} seconds".format(time.time() - start_time))
