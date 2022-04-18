import os
import shutil
from pathlib import Path
from webbrowser import get
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Delete folder results if it exists
if os.path.exists("results"):
    shutil.rmtree("results")

# Create a folder for results
Path("results").mkdir(parents=True, exist_ok=True)


class Language:
    pass

    def __init__(self, lang):
        self.lang: str = lang


go = Language("go")
java = Language("java")
javascript = Language("javascript")
python = Language("python")
ruby = Language("ruby")
swift = Language("swift")
php = Language("php")
typescript = Language("typescript")


def get_url_list(lang: str) -> list:
    """
    It gets the HTML of the docs page, parses it, and then writes the links to a file

    :param lang: The language you want to scrape
    """
    url: str = f"https://docs.temporal.io/docs/{lang}/"
    grab = requests.get(url)
    soup = BeautifulSoup(grab.text, "html.parser")
    for link in soup.find_all("a"):
        try:
            if link.get("href").startswith(f"/docs/{lang}/how-to"):
                with open(f"results/links-{lang}.md", "a") as f:
                    f.write(link.get("href") + "\n")
        except AttributeError:
            pass


get_url_list(java.lang)
get_url_list(go.lang)
get_url_list(javascript.lang)
get_url_list(python.lang)
get_url_list(ruby.lang)
get_url_list(swift.lang)
get_url_list(php.lang)
get_url_list(typescript.lang)


# print the number of items in file
def count_lines(file):
    """
    It opens a file, counts the number of lines in the file, and then prints the number of lines in the
    file

    :param file: the file to be counted
    :return: The number of lines in the file.
    """
    try:
        with open(file, "r") as fp:
            num_lines: str = sum(1 for line in fp if line.rstrip())
        print(
            f"{file.split('/links-', 1)[1]}",
            (round(num_lines / 31, 2) * 100),
            "% percent complete",
        )
        # create a csv file with two columns named "language" and "percent"
        with open(f"results/stats-results.csv", "a") as f:
            f.write(f"{file.split('/links-', 1)[1]},{round(num_lines / 31, 2) * 100}\n")
        return num_lines
    except FileNotFoundError:
        pass


# Calling the function count_lines and passing the file name as an argument.
count_lines("results/links-go.md")
count_lines("results/links-java.md")
count_lines("results/links-javascript.md")
count_lines("results/links-python.md")
count_lines("results/links-ruby.md")
count_lines("results/links-swift.md")
count_lines("results/links-php.md")
count_lines("results/links-typescript.md")

# print today's date in month, day, year format
date_generated = datetime.now().strftime("%B %d, %Y")

# Reading the csv file and plotting a bar graph and add title and labels
df = pd.read_csv("results/stats-results.csv", names=["language", "percent"])
df.plot.bar(
    x="language",
    y="percent",
    rot=0,
    color="blue",
    title=f"Percentage of completion for {date_generated}",
)
plt.show()
