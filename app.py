from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import random

app = Flask(__name__)

# ------------------------------------------------
# Fetch product data from BooksToScrape
# ------------------------------------------------
def fetch_product(url):

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("h1").text

        price_tag = soup.find("p", class_="price_color")
        price_text = price_tag.text.strip()
        base_price = float(price_text.replace("£","").replace("Â",""))

        rating_tag = soup.find("p", class_="star-rating")
        rating = rating_tag["class"][1]

        availability = soup.find("p", class_="instock availability").text.strip()

        img = soup.find("img")["src"]
        image = "https://books.toscrape.com/" + img.replace("../","")

        return title, base_price, rating, availability, image

    except Exception as e:
        print("Error:", e)
        return None, None, None, None, None


# ------------------------------------------------
# Price analysis
# ------------------------------------------------
def analyze_prices(prices):

    highest = max(prices)
    lowest = min(prices)
    average = round(sum(prices)/len(prices),2)

    if prices[-1] > prices[0]:
        trend = "Increasing"
        recommendation = "WAIT (price rising)"

    elif prices[-1] < prices[0]:
        trend = "Decreasing"
        recommendation = "GOOD TIME TO BUY"

    else:
        trend = "Stable"
        recommendation = "SAFE TO BUY"

    return highest, lowest, average, trend, recommendation


# ------------------------------------------------
# Welcome Page
# ------------------------------------------------
@app.route("/")
def welcome():
    return render_template("welcome.html")


# ------------------------------------------------
# Home Page
# ------------------------------------------------
@app.route("/home")
def home():
    return render_template("home.html")


# ------------------------------------------------
# Price Check
# ------------------------------------------------
@app.route("/check", methods=["POST"])
def check():

    url = request.form["url"]

    title, base_price, rating, availability, image = fetch_product(url)

    prices = []

    last_price = None

    try:
        with open("price_history.csv") as f:
            rows = list(csv.reader(f))
            if rows:
                last_price = float(rows[-1][1])
    except:
        pass


    if base_price:

        # simulate unstable price snapshots
        for i in range(5):

            simulated_price = base_price + random.uniform(-3, 3)
            simulated_price = round(simulated_price,2)

            prices.append(simulated_price)

            with open("price_history.csv","a",newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), simulated_price])


        highest, lowest, average, trend, recommendation = analyze_prices(prices)

        current_price = prices[-1]

        alert = None
        if last_price and current_price < last_price:
            alert = "Price Drop Alert! Good time to buy."


        return render_template(
            "result.html",
            title=title,
            price=current_price,
            rating=rating,
            availability=availability,
            image=image,
            highest=highest,
            lowest=lowest,
            average=average,
            trend=trend,
            recommendation=recommendation,
            alert=alert
        )

    return render_template("result.html", price="Price not found")


# ------------------------------------------------
# History Page
# ------------------------------------------------
@app.route("/history")
def history():

    rows = []

    try:
        with open("price_history.csv") as f:
            reader = csv.reader(f)
            rows = list(reader)
    except:
        rows = []

    return render_template("history.html", rows=rows)


# ------------------------------------------------
# Statistics Page
# ------------------------------------------------
@app.route("/stats")
def stats():

    prices = []

    try:
        with open("price_history.csv") as f:
            reader = csv.reader(f)

            for r in reader:
                prices.append(float(r[1]))

    except:
        prices = []

    if prices:

        return render_template(
            "stats.html",
            count=len(prices),
            max=max(prices),
            min=min(prices)
        )

    else:

        return render_template(
            "stats.html",
            count=0,
            max="N/A",
            min="N/A"
        )


# ------------------------------------------------
# About Page
# ------------------------------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# ------------------------------------------------
# Run Server
# ------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)