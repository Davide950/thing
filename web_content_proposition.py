import requests

# Sostituisci con la tua chiave API e il tuo ID di motore di ricerca personalizzato (CSE)
api_key = "AIzaSyCE34PP9dKpk0Iz2jZHQAz6B67FAeKyrB8"
cse_id = "c258b386aa6e54a70"



def web_content_proposition(keywords: list[tuple], predicted_content) -> dict:
    keywords.append(predicted_content)
    content_proposition = {}
    for i in range(len(keywords)):
        if i == len(keywords)-1:
            url = f"https://www.googleapis.com/customsearch/v1?q={keywords[i][1]}&key={api_key}&cx={cse_id}"
        else:
            url = f"https://www.googleapis.com/customsearch/v1?q={keywords[i][0]}&key={api_key}&cx={cse_id}"

        # Richiedi i risultati di ricerca in formato JSON
        response = requests.get(url)
        results = response.json()

        item = results.get("items", [])[0]  # Access the first item in the list
        link = item.get("link")
        if i == len(keywords)-1:
            content_proposition[keywords[i][1]] = link
        else:
            content_proposition[keywords[i][0]] = link


    return content_proposition

#Esempio

keywords = [
    ("Python programming",),
    ("Machine Learning",),
    ("Data Science",)
]

# Predicted content (a single tuple)
predicted_content = (0,"Artificial Intelligence")

print(web_content_proposition(keywords, predicted_content))


