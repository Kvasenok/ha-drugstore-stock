"""Config flow for Drugstore Stock integration."""
from homeassistant import config_entries
import voluptuous as vol
from homeassistant.helpers import selector
from .const import DOMAIN

class DrugstoreStockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Drugstore Stock."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["list_name"],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("list_name"): selector.selector({
                    "type": "text",
                    "translation_key": "list_name"
                }),
                vol.Optional("location"): selector.selector({
                    "type": "area"
                }),
            }),
        )
