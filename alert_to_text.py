from nws_api import fetch_alerts, parse_alerts

def main():
  xml_data = fetch_alerts()
  if xml_data:
    alerts = parse_alerts(xml_data)
    if alerts:
      with open('alerts.txt', 'w') as file:
        for alert in alerts:
          file.write(alert['title'] + '\n')

if __name__ == "__main__":
  main()
