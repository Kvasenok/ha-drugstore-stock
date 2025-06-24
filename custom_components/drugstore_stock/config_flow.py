"""Config flow for Drugstore Stock integration."""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
from .const import DOMAIN

class DrugstoreStockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Drugstore Stock."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("name"): str,
                vol.Required("initial_quantity", default=0): int,
                vol.Optional("min", default=0): int,
                vol.Optional("max", default=100): int,
                vol.Optional("unit_of_measurement", default="units"): str,
            }),
        )
