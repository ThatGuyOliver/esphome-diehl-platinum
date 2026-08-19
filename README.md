#UNSTABLE - WORK IN PROGRESS

# esphome-diehl-platinum
Esphome component to readout diehl platinum solar inverters

## example yaml:
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
      name: 'Power'
    day_energy:
      name: 'Day energy' 
```

## hardware
Connect to the inverter trough a Max232 TTL => RS232 converter like [this one].(https://nl.aliexpress.com/item/1005006513010110.html?gatewayAdapt=glo2nld)
