# esphome-diehl-platinum
Esphome component to readout one standalone diehl platinum solar inverter (to use in Home Assistant).

| Quantity | Unit |
|----------|----------|
| Day energy   | Wh   |
| Power   | W   |

## Example YAML (used in ESPHome):
```YAML
external_components:
   - source: github://ThatGuyOliver/esphome-diehl-platinum@main
     components: [ diehl ]

uart:
  - baud_rate: 19200
    tx_pin: GPIO17
    rx_pin: GPIO16
    
time:
  - platform: homeassistant

sensor:
  - platform: diehl
    power:
      name: 'Power'
    day_energy:
      name: 'Day energy' 
```

## Hardware
### ESP board
An ESP board that will run the ESPHome program
### Adapter
Connect to the inverter trough a Max232 TTL => RS232 converter. ( e.g. https://aliexpress.com/item/1005006513010110.html)
### Cable
You also need a connector/cable with 2 MALE DB9 connectors. (e.g. https://aliexpress.com/item/1005002471223441.html)
