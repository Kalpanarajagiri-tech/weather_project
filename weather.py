import streamlit as st
import requests

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #36d1dc, #5b86e5);
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: white;
    margin-bottom: 30px;
}

.weather-card {
    background: white;
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    color: #222;
}

.city {
    font-size: 32px;
    font-weight: bold;
}

.temperature {
    font-size: 60px;
    font-weight: bold;
    color: #2563eb;
    margin: 10px;
}

.weather {
    font-size: 24px;
    margin-bottom: 20px;
}

.info {
    font-size: 20px;
    margin: 12px;
}

.footer {
    text-align: center;
    color: white;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">🌤️ Weather App</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Check the current weather of any city</div>',
    unsafe_allow_html=True
)


API_KEY = "e7a8c41f6d091d433ef78f3290b85fc5"


city = st.text_input(
    "🏙️ Enter City Name",
    placeholder="Example: Hyderabad"
)


if st.button("🔍 Get Weather", use_container_width=True):

    if not city.strip():
        st.warning("⚠️ Please enter a city name.")

    else:

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        try:

            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()

                city_name = data["name"]
                country = data["sys"]["country"]
                temperature = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                weather = data["weather"][0]["description"]
                icon = data["weather"][0]["icon"]

                icon_url = (
                    f"https://openweathermap.org/img/wn/"
                    f"{icon}@2x.png"
                )

                html = f"""
<div class="weather-card">
<div class="city">📍 {city_name}, {country}</div>
<img src="{icon_url}" width="100">
<div class="temperature">{temperature:.1f}°C</div>
<div class="weather">☁️ {weather.title()}</div>
<div class="info">🌡️ Feels Like: {feels_like:.1f}°C</div>
<div class="info">💧 Humidity: {humidity}%</div>
<div class="info">💨 Wind Speed: {wind_speed} m/s</div>
</div>
"""

                st.markdown(
                    html,
                    unsafe_allow_html=True
                )

            elif response.status_code == 401:

                st.error("❌ Invalid API key.")

            elif response.status_code == 404:

                st.error("❌ City not found.")

            else:

                st.error(
                    f"❌ Error: {response.status_code}"
                )

        except requests.exceptions.RequestException:

            st.error(
                "❌ Could not connect to the weather service."
            )


st.markdown(
    '<div class="footer">🌍 Live Weather • Built with Streamlit 🐍</div>',
    unsafe_allow_html=True
)