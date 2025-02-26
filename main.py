import requests

resp = requests.get("https://zenquotes.io/api/random")
print(resp)
if resp.status_code == 200:
    data = resp.json()
    if isinstance(data, list) and len(data) > 0:
        quote_data = data[0]
    if "q" in quote_data and "a" in quote_data:
        quote = quote_data["q"]
        author = quote_data["a"]
        print("Цитата:", quote)
        print("Автор:", author)
        with open("quote.txt", "w", encoding="utf-8") as file:
            file.write(f"\"{quote}\"-{author}\n")
        with open("quote.txt", "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            print(len(words))
