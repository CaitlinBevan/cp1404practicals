import wikipedia


def main():
    prompt = input("Enter a page title or search phrase: ")
    while prompt != "":
        try:
            page_title = wikipedia.page(prompt)
            print(page_title.title)
            print(wikipedia.summary(prompt))
            print(page_title.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        prompt = input("Enter a page title or search phrase: ")


main()
