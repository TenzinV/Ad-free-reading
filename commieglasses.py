import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def get_article_content(url):
    response = requests.get(url)
    article_text = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_body = soup.find('article')
        if article_body:
            paragraphs = article_body.find_all('p')
            for paragraph in paragraphs:
                paragraph_text = paragraph.get_text(strip=True)
                article_text += f"{paragraph_text}\n\n"
    if not article_text:
        article_text = "Content could not be retrieved or doesn't exist."
    return article_text


def show_article():
    url = url_entry.get()
    article_content = get_article_content(url)
    article_display.delete(1.0, tk.END)
    article_display.insert(tk.INSERT, article_content)


# Set up the GUI
root = tk.Tk()
root.title("Article Scraper and Viewer")
root.geometry("600x400")

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch Article", command=show_article)
fetch_button.pack(pady=5)

article_display = ScrolledText(root, wrap=tk.WORD)
article_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()

