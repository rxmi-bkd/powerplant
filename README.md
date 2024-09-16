Hello,

Here is what I was able to accomplish in 4 hours.

# Tools
- Python
- Django (Django REST framework)

# Running the Project
Run `py src/manage.py runserver 8888` to start the server.

Endpoint: `http://localhost:8888/api/powerplant/productionplan/`

You can test the endpoint with the `test.py` script.

# Code
The algorithm that computes the production plan is in the file ``src/powerplant/utils.py`` and the associated endpoint is in the file ``src/powerplant/views.py``.

# Bugs

## Payload
I was unable to serialize the `fuels` attribute of the payload with my framework due to special characters.

So instead of having the payload like this:
```json
{
  "load": 480,
  "fuels": {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [...]
}
```

We will have:
```json
{
  "load": 480,
  "fuels": {
    "gas": 13.4,
    "kerosine": 50.8,
    "co2": 20,
    "wind": 60
  },
  "powerplants": [...]
}
```

# Improvements to be Made

My algorithm works for payloads 1 and 3, but for payload 2, it might be better to produce the remaining energy using `gasfiredsomewhatsmaller` instead of `gasfiredbig2`, even though the latter is more efficient. Indeed, with `gasfiredbig2`, we produce 80 MWh of excess energy, while with `gasfiredsomewhatsmaller`, we would have only produced 20.

# Notes

I wanted to do the Docker part, but since I did this project while at work, I couldn't use Docker with my work PC. If you want, I can send you the project tomorrow with the Docker part fully functional.