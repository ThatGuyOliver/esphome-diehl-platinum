⚠️ WORK IN PROGRESS - I have not confirmed these codes, it's a compilation of what I've found online.

# Diehl Platinum S-Series Status & Event Codes

> ℹ️ These codes are returned by the ESPHome component as `status` and `event` sensors.
## Overview

This document describes the status and event codes used by Diehl Platinum S-series inverters (2100 S, 3200 S, 3800 S, 4600 S, 4601 S). These codes correspond to "status" and "event" sensors in the ESPHome component.

**In ESPHome:**
```yaml
sensor:
  - platform: diehl
    status:
      name: "Status"  # Returns codes 0, 1, 2, 3, etc.
    event:
      name: "Event"   # Returns codes 0, 90, 91, 220, etc.
```

## Status Codes

| Code | LED | Meaning | Description |
|------|-----|---------|-------------|
| **0** | ❌ Red | **Off / Fault** | Inverter is off or in fault state |
| **1** | ✅ Green | **Normal Operation** | Inverter is producing normally (grid-tied) |
| **2** | ⚠️ Yellow | **Warning** | Inverter is operating with warnings |
| **3** | 🔄 Green blinking | **Starting** | Inverter is starting up (self-test) |
| **4** | 🔌 Blue | **Island Mode** | Inverter operating in island/off-grid mode (optional) |
| **5** | ⏸️ | **Paused** | Inverter is temporarily paused |
| **31** | 🔍 | **Diagnosis** | Service/diagnosis mode |

### Typical Status Combinations

| Status | Event | Meaning |
|--------|-------|---------|
| 0 | 0 | Inverter off (normal at night) |
| 1 | 0 | Normal operation, no faults ✅ |
| 1 | 90 | Operating, but AC voltage too high ⚠️ |
| 0 | 94 | Fault, inverter stopped (internal fault) ❌ |
| 2 | 220 | Operating with warning, temperature too high ⚠️ |
| 3 | 0 | Starting up (normal during startup) 🔄 |

---

## Event Codes

### Fatal Errors (90-127)

These errors cause the inverter to stop production.

| Event | Code | Description | Possible Cause | Action |
|-------|------|-------------|----------------|--------|
| **90** | AC High | AC voltage too high | Grid voltage exceeds limits | Check AC connection, measure grid voltage |
| **91** | DC High | DC voltage too high | PV array voltage exceeds limits | Check DC connection, measure PV voltage |
| **92** | DC Connection | DC connection not OK | DC polarity reversed | Disconnect DC, check polarity |
| **93** | Insulation | Insulation fault | DC insulation failure | Disconnect DC, check insulation |
| **94** | Internal Fault | Internal system fault | Hardware failure | Contact service |
| **95** | Internal Fault | Internal system fault | Hardware failure | Contact service |
| **101-102** | Internal Fault | Internal system fault | Hardware failure | Contact service |
| **106-108** | Internal Fault | Internal system fault | Hardware failure | Contact service |
| **110** | Relay Error | Relay fault | Relay malfunction | Contact service |
| **111-114** | Internal Fault | Internal system fault | Hardware failure | Contact service |
| **121-127** | Internal Fault | Internal fault / Country setting | Hardware or configuration | Contact service |
| **130** | L/N Swapped | L and N swapped | AC wiring error | Check AC connection (L/N) |

---

### Warnings (131-299)

These warnings may reduce performance but don't necessarily stop production.

| Event | Code | Description | Meaning |
|-------|------|-------------|---------|
| **131-139** | Warning | General warnings | Non-blocking warnings |
| **140** | Blocking Error | Blocking error | Production blocked |
| **200** | Temporary Shutdown | Temporary shutdown | Temporary production stop |
| **201-203** | Overvoltage AC | AC overvoltage | Grid voltage too high |
| **205** | Frequency Error | Frequency error | Grid frequency out of range |
| **220** | Temperature High | Temperature too high | Power section too hot |
| **221** | Internal Temperature | Internal temperature too high | Internal overheating |
| **236** | Internal Fault | Internal fault | Internal error |
| **239** | Measuring Error DC | DC measuring error | DC measurement fault |
| **274** | DC Voltage Low | DC voltage too low | PV voltage insufficient |
| **275** | Emergency Stop | Emergency stop | Emergency shutdown |
| **290** | Subsequent Message | Subsequent error | Follow-up error after shutdown |

---

### Information (300+)

Informational messages, typically stored in event memory.

| Event | Code | Description | Meaning |
|-------|------|-------------|---------|
| **301** | DC Voltage Dip | Sudden DC voltage dip | Temporary DC voltage drop |
| **352** | Internal Temperature | Internal temperature too high | Overheating event logged |
| **353** | Communication Error | Communication error | Operating unit - stringbox communication fault |
| **400-499** | Information Reset | Information reset | No action required |
| **501** | DC High | DC voltage too high | DC overvoltage event |
| **502** | Frequency Error | Frequency error | Grid frequency fault |
| **514** | Internal Fault | Internal fault | Internal error logged |
| **515** | Update Firmware | Firmware update | Firmware update required |

---

## Troubleshooting

### Status 0 (Off/Fault)

| Event | Action |
|-------|--------|
| 90 | Check AC grid voltage, verify AC breaker is ON |
| 91 | Check DC PV array voltage, verify DC switch is ON |
| 92 | Check DC polarity (+/-), reconnect DC |
| 93 | Check DC insulation, contact service |
| 94-95 | Contact service (internal fault) |

### Status 2 (Warning)

| Event | Action |
|-------|--------|
| 220-221 | Check ventilation, clean air filters, reduce load |
| 274 | Check PV array configuration, verify DC voltage |
| 353 | Check RS232/RS485 connections |

### Status 1 (Normal) with Event > 0

Inverter is still operating but logging warnings. Monitor the situation and address the underlying cause.

---

## References

- Diehl Platinum Event List (official documentation)
- Diehl Platinum S-series Installation and User Manual
- https://omvormerservice.be/index.html/error_code_diehl/
- https://inverterservice.gr/en/error_code_diehl-en/

---

## Notes

- Status and event codes are specific to **Diehl Platinum S-series** (2100 S, 3200 S, 3800 S, 4600 S, 4601 S)
- Codes may differ for other Diehl models (TL, TL3, etc.)
- Event code **0** means "no event" (normal operation)
- Multiple events can be logged simultaneously; the highest priority event is displayed
