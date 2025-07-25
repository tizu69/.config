#!/usr/bin/env python3

from typing import Literal
from pyquery import PyQuery  # install using `pip install pyquery`
import json, re

# set your location_id
# to get your location_id, go to https://weather.com & search for your location.
# once you choose your location, you can see the location_id in the URL
location_id = "923384cba96c0abcacb928de8bbe17a0ec29b0855bec918a63da0b6dbcda0d66"
unit: Literal["metric", "imperial"] = "metric"
forecast_type: Literal["Hourly", "Daily"] = "Hourly"

##################################################################################

weather_icons = {
    "sunnyDay": "",
    "clearNight": "",
    "cloudyFoggyDay": "",
    "cloudyFoggyNight": "",
    "rainyDay": "",
    "rainyNight": "",
    "snowyIcyDay": "󰼶",
    "snowyIcyNight": "󰼶",
    "severe": "",
    "default": "󰖐",
}

_l = "en-IN" if unit == "metric" else "en-US"
url = f"https://weather.com/{_l}/weather/today/l/{location_id}"

html_data = PyQuery(url=url)
temp = html_data("span[data-testid='TemperatureValue']").eq(0).text()
status = html_data("div[data-testid='wxPhrase']").text()
status = f"{status[:16]}.." if len(status) > 17 else status
status_code_class = html_data("#regionHeader").attr("class")
status_code = str(status_code_class).split(" ")[2].split("-")[2]
icon = weather_icons[status_code] if status_code in weather_icons else weather_icons["default"]
temp_feel = html_data(
    "div[data-testid='FeelsLikeSection'] > span > span[data-testid='TemperatureValue']"
).text()
temp_min = (
    html_data("div[data-testid='wxData'] > span[data-testid='TemperatureValue']").eq(1).text()
)
temp_max = (
    html_data("div[data-testid='wxData'] > span[data-testid='TemperatureValue']").eq(0).text()
)
wind_speed = str(html_data("span[data-testid='Wind']").text())
humidity = html_data("span[data-testid='PercentageValue']").text()
visbility = html_data("span[data-testid='VisibilityValue']").text()
air_quality_index = html_data("text[data-testid='DonutChartValue']").text()

temp_feel_text = f"Feels like {temp_feel}{'c' if unit == 'metric' else 'f'}"
temp_min_max = f" {temp_min}\t\t {temp_max}"
wind_text = f"󰶥 {wind_speed}"
humidity_text = f" {humidity}"
visbility_text = f"  {visbility}"
air_quality_index_text = f"AQI {air_quality_index}"

tooltip_text = str.format(
    "{}\n{}\n\n{}\n{}\n{}",
    f'<span size="xx-large">{icon} {temp} {status}</span>',
    f"<small>{temp_feel_text}</small>",
    f"{temp_min_max}",
    f"{wind_text}\t{humidity_text}",
    f"{visbility_text}\t{air_quality_index_text}",
)

out_data = {
    "text": f"{icon} {temp}",
    "alt": status,
    "tooltip": tooltip_text,
    "class": status_code,
}
print(json.dumps(out_data))
