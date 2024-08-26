"""Mapping module from the OpenWeatherMap API objects"""

# Map the icons to the weather codes
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈️",
    "13d": "❄️",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈️",
    "13n": "❄️",
    "50n": "🌫",
}

# Languages available
LANGUAGE_CODES = """
af Afrikaans
al Albanian
ar Arabic
az Azerbaijani
bg Bulgarian
ca Catalan
cz Czech
da Danish
de German
el Greek
en English
eu Basque
fa Persian (Farsi)
fi Finnish
fr French
gl Galician
he Hebrew
hi Hindi
hr Croatian
hu Hungarian
id Indonesian
it Italian
ja Japanese
kr Korean
la Latvian
lt Lithuanian
mk Macedonian
no Norwegian
nl Dutch
pl Polish
pt Portuguese
pt_br Português Brasil
ro Romanian
ru Russian
sv, se Swedish
sk Slovak
sl Slovenian
sp, es Spanish
sr Serbian
th Thai
tr Turkish
ua, uk Ukrainian
vi Vietnamese
zh_cn Chinese Simplified
zh_tw Chinese Traditional
zu Zulu
"""
