from nws_api import fetch_alerts, parse_alerts



def main():
    xml_data = fetch_alerts()
    if xml_data:
        alerts = parse_alerts(xml_data)
        with open('alerts.txt', 'a') as file:
          for alert in alerts:
            # Write the desired text to the file
            file.write(alert + "\n")


if __name__ == "__main__":
    main()
