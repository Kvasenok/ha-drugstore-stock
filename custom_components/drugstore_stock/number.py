"""Number platform for Drugstore Stock integration."""
from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = entry.data
    async_add_entities([
        DrugstoreStockNumber(
            name=data["name"],
            min_value=data.get("min", 0),
            max_value=data.get("max", 100),
            unit=data.get("unit_of_measurement", "units"),
            value=data.get("initial_quantity", 0)
        )
    ])

class DrugstoreStockNumber(NumberEntity):
    def __init__(self, name, min_value, max_value, unit, value):
        self._attr_name = name
        self._attr_native_min_value = min_value
        self._attr_native_max_value = max_value
        self._attr_native_unit_of_measurement = unit
        self._attr_native_value = value
        self._attr_unique_id = f"drugstore_stock_{name.lower().replace(' ', '_')}"

    async def async_set_native_value(self, value: float) -> None:
        self._attr_native_value = value
        self.async_write_ha_state()
