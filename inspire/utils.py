import requests
import json
import textwrap


class NinjaAPI:
    def __init__(self, api_key) -> None:
        self.api_url = "https://api.api-ninjas.com/v1/quotes"
        self.api_key = api_key

        self._categories = (
            "age",
            "alone",
            "amazing",
            "anger",
            "architecture",
            "art",
            "attitude",
            "beauty",
            "best",
            "birthday",
            "business",
            "car",
            "change",
            "communication",
            "computers",
            "cool",
            "courage",
            "dad",
            "dating",
            "death",
            "design",
            "dreams",
            "education",
            "environmental",
            "equality",
            "experience",
            "failure",
            "faith",
            "family",
            "famous",
            "fear",
            "fitness",
            "food",
            "forgiveness",
            "freedom",
            "friendship",
            "funny",
            "future",
            "god",
            "good",
            "government",
            "graduation",
            "great",
            "happiness",
            "health",
            "history",
            "home",
            "hope",
            "humor",
            "imagination",
            "inspirational",
            "intelligence",
            "jealousy",
            "knowledge",
            "leadership",
            "learning",
            "legal",
            "life",
            "love",
            "marriage",
            "medical",
            "men",
            "mom",
            "money",
            "morning",
            "movies",
            "success",
        )

    def _make_request(self, category=None):
        if category:
            assert category in self._categories, ValueError(
                "Only valid categories are listed on https://api-ninjas.com/api/quotes"
            )
            category_suffix = f"?category={category}"
        else:
            category_suffix = ""

        response = requests.get(
            self.api_url + category_suffix, headers={"X-Api-Key": self.api_key}
        )

        return response

    def get_quote(self, category=None) -> None:
        response = self._make_request(category)

        if response.status_code == requests.codes.ok:
            cont = json.loads(response.text)[0]
            author = cont["author"]
            quote = cont["quote"]
            # wrap quote
            quote = "\n".join(textwrap.wrap(quote, width=40))

            # print output
            print()
            print(quote)
            print()
            print(f"--- \x1B[3m{author}\x1B[0m")  # italic
            print()
        else:
            print("Error:", response.status_code, response.text)

        return None
