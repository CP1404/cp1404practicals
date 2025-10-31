"""
CP1404/CP5632 Practical
Wikipedia API exploration
Estimate: 20 min
Actual: 25 min
"""
import wikipedia

def main():
    print("Enter blank input to quit.")
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break
        try:
            # Try to fetch the page; autosuggest can be helpful but may choose a different page
            page = wikipedia.page(title, autosuggest=True)
            print(page.title)
            # Summaries can be long; show the first couple of sentences
            print(wikipedia.summary(page.title, sentences=2))
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(list(e.options)[:20])  # avoid flooding the screen
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except Exception as ex:
            # Catch-all for networking or library edge cases
            print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    main()
