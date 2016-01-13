## Requirements

Unirest for Python
`$ pip install unirest`

My plan

- App should get current latitude and longitude
- perform a search with current location as center of a rectangle
- find all bus stops within 300 meters, if didn't find anything increase this distance and continue until finding at least 1
- then the app should perform bus search queries from this station to user destinations (user specifies them in the beginning, can later update)
- App lists buses based on their arriving time including delay. also in case user has selected no destinations the app can simply check the station schedule and suggest buses.
- App widget will display this info on touch, a button to perform a "later" search or refresh results based on current time should also be there in the widget.

