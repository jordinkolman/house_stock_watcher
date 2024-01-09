import requests
import json


def main():
    response = requests.get(
        "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"
    )
    disclosures = json.loads(response.text)

    for i in range(5):
        (
            year,
            disclosure_date,
            transaction_date,
            owner,
            ticker,
            company,
            type,
            amount,
            name,
            district,
            state,
            ptr_link,
            over_200_cap_gains,
            industry,
            sector,
            party,
        ) = disclosures[i].values()
        print(
            f"""Year: {year}
Date: {transaction_date}
Disclosed: {disclosure_date}
Representative: {name}
Party: {party}
State: {state}
District: {district}
Stock Symbol: {ticker}
Company: {company}
Industry: {industry}
Sector: {sector}
Owner: {owner}
Purchase Amount: {amount}
Sale Type: {type}
Disclosure Link: {ptr_link}
Over $200 in Capital Gains: {'No' if over_200_cap_gains == False else 'Yes'}
"""
        )


if __name__ == "__main__":
    main()
