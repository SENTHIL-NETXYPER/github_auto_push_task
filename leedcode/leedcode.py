import requests
import webbrowser

url = "https://leetcode.com/graphql"

query = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    question {
      title
      titleSlug
    }
  }
}
"""

response = requests.post(url, json={"query": query})
data = response.json()

slug = data["data"]["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]

problem_url = f"https://leetcode.com/problems/{slug}/"

print("Today's Problem:", problem_url)

webbrowser.open(problem_url)