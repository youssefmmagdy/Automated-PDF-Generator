import datetime
import json

import PDF4RoomKey
from PDF4RoomKey.settings import CLIENT_ID, CLIENT_SECRET, BASE_API_URL


# Generate the bearer token
token = PDF4RoomKey.Authenticator.generate_bearer_token(CLIENT_ID, CLIENT_SECRET)

if not token:
    print("Error: Could not generate a bearer token.")
    exit(1)

fetcher = PDF4RoomKey.DataFetcher(BASE_API_URL, token)

today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")
arrivals = fetcher.get_arrivals(formatted_date)

print(arrivals)

# Print the stripped arrivals
# for stripped_arrival in arrivals:
#     print(json.dumps(stripped_arrival, indent=4))

# # Write arrivals to a file as JSON
# with open("./stripped_arrivals.json", "w") as file:
#     json.dump(arrivals, file)

