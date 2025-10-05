import requests

def fetch_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        time_updated = data.get("time", {}).get("updated", "unknown")
        usd_rate = data.get("bpi", {}).get("USD", {}).get("rate", "unknown")
        return {"time": time_updated, "usd": usd_rate}
    except requests.exceptions.RequestException as e:
        print("[Network error]", e)
    except ValueError:
        print("[Parse error] Response not valid JSON")
    except Exception as e:
        print("[Unexpected error]", e)
    return None

def fetch_weather(latitude, longitude):
    # Open-Meteo returns JSON and requires no API key
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        cw = data.get("current_weather")
        if not cw:
            print("[API] No current_weather found in response")
            return None
        return {
            "time": cw.get("time"),
            "temperature_c": cw.get("temperature"),
            "windspeed": cw.get("windspeed"),
            "winddirection": cw.get("winddirection"),
        }
    except requests.exceptions.RequestException as e:
        print("[Network error]", e)
    except ValueError:
        print("[Parse error] Response not valid JSON")
    except Exception as e:
        print("[Unexpected error]", e)
    return None

def main():
    while True:
        print("\nOptions:")
        print("1) Get Bitcoin price (USD)")
        print("2) Get current weather (by coordinates)")
        print("3) Quit")
        choice = input("Choose 1/2/3: ").strip()
        if choice == "1":
            res = fetch_bitcoin_price()
            if res:
                print(f"Bitcoin (USD): {res['usd']} (updated: {res['time']})")
        elif choice == "2":
            lat = input("Latitude (e.g., 28.6139): ").strip()
            lon = input("Longitude (e.g., 77.2090): ").strip()
            try:
                latf = float(lat); lonf = float(lon)
            except ValueError:
                print("Invalid coordinates; please enter numbers.")
                continue
            w = fetch_weather(latf, lonf)
            if w:
                print(f"Time: {w['time']}")
                print(f"Temperature: {w['temperature_c']} °C")
                print(f"Wind: {w['windspeed']} m/s, direction {w['winddirection']}°")
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
