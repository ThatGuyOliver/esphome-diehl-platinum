import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart, time
from esphome.const import (
    CONF_TIME_ID,
    CONF_ID,
    CONF_POWER,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_WATT,
    UNIT_WATT_HOURS,
    DEVICE_CLASS_NONE,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_TEMPERATURE,
    UNIT_VOLT,
    UNIT_AMPERE,
    UNIT_CELSIUS
)

CODEOWNERS = ["@ThatGuyOliver"]
DEPENDENCIES = ["uart", "time"]

CONF_DAY_ENERGY = 'day_energy'
CONF_STATUS = "status"
CONF_EVENT = "event"
CONF_DC_VOLTAGE = "dc_voltage"
CONF_DC_CURRENT = "dc_current"
CONF_DC_POWER = "dc_power"
CONF_AC_VOLTAGE = "ac_voltage"
CONF_AC_CURRENT = "ac_current"
CONF_AC_POWER = "ac_power"
CONF_TEMP_1 = "temp_1"
CONF_TEMP_2 = "temp_2"
CONF_TEMP_3 = "temp_3"

diehl_ns = cg.esphome_ns.namespace("diehl")
DiehlComponent = diehl_ns.class_(
    "DiehlComponent", cg.PollingComponent, uart.UARTDevice
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(DiehlComponent),
            cv.GenerateID(CONF_TIME_ID): cv.use_id(time.RealTimeClock),
            cv.Optional(CONF_DAY_ENERGY): sensor.sensor_schema(

                accuracy_decimals=0,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
                unit_of_measurement=UNIT_WATT_HOURS,
            ),
            cv.Optional(CONF_POWER): sensor.sensor_schema(

                accuracy_decimals=1,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_WATT,
            ),
            cv.Optional(CONF_STATUS): sensor.sensor_schema(
                 accuracy_decimals=0,
                    device_class=DEVICE_CLASS_NONE,  # of een passende class
                 state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_EVENT): sensor.sensor_schema(
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_NONE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_DC_VOLTAGE): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_VOLT,
            ),
            cv.Optional(CONF_DC_CURRENT): sensor.sensor_schema(
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_AMPERE,
            ),
            cv.Optional(CONF_DC_POWER): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_WATT,
            ),
            cv.Optional(CONF_AC_VOLTAGE): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_VOLT,
            ),
            cv.Optional(CONF_AC_CURRENT): sensor.sensor_schema(
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_AMPERE,
            ),
            cv.Optional(CONF_AC_POWER): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_WATT,
            ),
            cv.Optional(CONF_TEMP_1): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_CELSIUS,
            ),
            cv.Optional(CONF_TEMP_2): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_CELSIUS,
            ),
            cv.Optional(CONF_TEMP_3): sensor.sensor_schema(
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement=UNIT_CELSIUS,
            )
        }
    )
    .extend(cv.polling_component_schema("32s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "diehl", baud_rate=19200, require_rx=True, require_tx=True
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    time_ = await cg.get_variable(config[CONF_TIME_ID])
    cg.add(var.set_time(time_))

    for key in [
        CONF_DAY_ENERGY,
        CONF_POWER,
        CONF_STATUS,
        CONF_EVENT,
        CONF_DC_VOLTAGE,
        CONF_DC_CURRENT,
        CONF_DC_POWER,
        CONF_AC_VOLTAGE,
        CONF_AC_CURRENT,
        CONF_AC_POWER,
        CONF_TEMP_1,
        CONF_TEMP_2,
        CONF_TEMP_3,
    ]:
        if key not in config:
            continue
        conf = config[key]
        sens = await sensor.new_sensor(conf)
        cg.add(getattr(var, f"set_{key}_sensor")(sens))
