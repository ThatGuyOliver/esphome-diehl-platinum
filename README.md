⚠️ **UNSTABLE - WORK IN PROGRESS** - Use at your own risk!

This component is in active development.

    Use at your own risk

    No guarantees provided

    Test thoroughly before relying on it

    Backup your configuration before installing
    
# esphome-diehl-platinum

ESPHome custom component to read out Diehl Platinum S-series solar inverters via RS232.

## Features:

- Real-time power monitoring (DC/AC voltage, current, power)

- Daily energy production

- Inverter status and event codes

- Temperature monitoring (3 sensors)

- Native ESPHome integration (works with Home Assistant)
## Detail-mode (15-minute data)

| Quantity | Unit | ESPHome config key |
|----------|------|--------------------|
| Day energy | Wh | `day_energy` |
| Power | W | `power` |
| Status | – (raw code) | `status` |
| Event | – (raw code) | `event` |
| DC Voltage | V | `dc_voltage` |
| DC Current | A | `dc_current` |
| DC Power | W | `dc_power` |
| AC Voltage | V | `ac_voltage` |
| AC Current | A | `ac_current` |
| AC Power | W | `ac_power` |
| Temperature 1 | °C | `temp_1` |
| Temperature 2 | °C | `temp_2` |
| Temperature 3 | °C | `temp_3` |

## Summary-mode (Daily data)

| Quantity | Unit | ESPHome config key |
|----------|------|--------------------|
| Date | YYYY-MM-DD | `date` |
| DC Voltage Peak | V | `dc_voltage_peak` |
| DC Voltage Mean | V | `dc_voltage_mean` |
| DC Current Peak | A | `dc_current_peak` |
| DC Current Mean | A | `dc_current_mean` |
| DC Power Peak | W | `dc_power_peak` |
| DC Power Mean | W | `dc_power_mean` |
| AC Voltage Peak | V | `ac_voltage_peak` |
| AC Voltage Mean | V | `ac_voltage_mean` |
| AC Current Peak | A | `ac_current_peak` |
| AC Current Mean | A | `ac_current_mean` |
| AC Power Peak | W | `ac_power_peak` |
| AC Power Mean | W | `ac_power_mean` |
| Day Energy | Wh | `day_energy` |
| Total Energy Sum | Wh | `energy_sum` |
| Temperature Peak | °C | `temp_peak` |


### Status & Event Codes

See [STATUS_EVENT_CODES.md](STATUS_EVENT_CODES.md) for the list of Error and Event codes.

## Example YAML (used in ESPHome)

```yaml
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
      name: "Power"
    day_energy:
      name: "Day energy"
    status:
      name: "Status"
    event:
      name: "Event"
    dc_voltage:
      name: "DC Voltage"
    dc_current:
      name: "DC Current"
    dc_power:
      name: "DC Power"
    ac_voltage:
      name: "AC Voltage"
    ac_current:
      name: "AC Current"
    ac_power:
      name: "AC Power"
    temp_1:
      name: "Temperature 1"
    temp_2:
      name: "Temperature 2"
    temp_3:
      name: "Temperature 3"
```

### Hardware

### ESP32 Board
An ESP32 board that runs ESPHome

### RS232 Adapter
Connect to the inverter through a **MAX232 TTL ⇄ RS232** converter:
- Example: [AliExpress](https://aliexpress.com/item/1005006513010110.html)

### Connector/Cable
You need a connector/cable with **2 MALE DB9 connectors**:
- Example: [AliExpress](https://aliexpress.com/item/1005002471223441.html)

### Wiring Diagram

## Disclaimer
This is a community project. Use at your own risk.
This project is based on Roeland Lutters’ original ESPHome Diehl Platinum component and includes reverse engineering of Stendec’s RS_diehl.c.
