import requests
import xml.etree.ElementTree as ET

def fetch_alerts():
  url = "https://api.weather.gov/alerts/active.atom"
  url += "?zone=ILC201&certainty=Observed,Possible,Likely&severity=Extreme,Moderate,Severe&urgency=Expected,Immediate,Future"

  headers = {"Accept": "application/atom+xml"}
  response = requests.get(url, headers=headers)
  print(f"Status code: {response.status_code}")

  if response.status_code == 200:
    return response.content
  else:
    print(f"Failed to fetch data: {response.status_code}")
    return None

def parse_alerts(xml_data):
  ns = {'atom': 'http://www.w3.org/2005/Atom', 'cap': 'urn:oasis:names:tc:emergency:cap:1.2'}

  def parse_cap_entry(entry):
    cap_data = {}
    title = entry.find('atom:title', ns)
    summary = entry.find('atom:summary', ns)
    cap_event = entry.find('cap:event', ns)
    cap_sent = entry.find('cap:sent', ns)
    cap_effective = entry.find('cap:effective', ns)
    cap_expires = entry.find('cap:expires', ns)
    
    if cap_event is not None and cap_sent is not None:
      cap_data = {
        'title': title.text if title is not None else None,
        'summary' : summary.text if summary is not None else None,
        'event': cap_event.text if cap_event is not None else None,
        'effective': cap_effective.text if cap_effective is not None else None,
        'expires': cap_expires.text if cap_expires is not None else None,
      }
    return cap_data

  root = ET.fromstring(xml_data)
  entries = root.findall('atom:entry', ns)
  alerts = [parse_cap_entry(entry) for entry in entries if parse_cap_entry(entry)]
  
  return alerts
