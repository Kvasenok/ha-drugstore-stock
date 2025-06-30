![hacs custom](https://img.shields.io/badge/hacs-custom-orange.svg)
![Validate with hassfest](https://github.com/BigPiloto/ha-drugstore-stock/actions/workflows/hassfest.yaml/badge.svg)
![HACS Action](https://github.com/BigPiloto/ha-drugstore-stock/actions/workflows/validate.yaml/badge.svg)
![Release](https://img.shields.io/github/v/release/BigPiloto/ha-drugstore-stock.svg)
![Last commit](https://img.shields.io/github/last-commit/BigPiloto/ha-drugstore-stock.svg)

# Drugstore Stock

[🇧🇷 Read in Brazilian Portuguese](README.pt-br.md)

Manage your household medicine stock with Home Assistant!

Drugstore Stock is an integration (custom component) for Home Assistant. It runs on the back-end, processing and exposing stock list data as entities in Home Assistant.

To view Drugstore Stock data directly on your dashboard (Lovelace), it is recommended to also install the custom card [Drugstore Stock Card](https://github.com/BigPiloto/ha-drugstore-stock-card). This card makes it easier to visualize and manage your stock lists through the Home Assistant interface.

## Overview

Drugstore Stock integration allows you to register and monitor your medicine inventory in Home Assistant, helping you keep track of available quantities and identify when it’s time to restock.

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=BigPiloto&repository=ha-drugstore-stock&category=Integration)

### Method 1: HACS Installation (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance
2. Go to **`HACS` > `3 dots` > `Custom repositories`**
3. Add this repository URL: `https://github.com/BigPiloto/ha-drugstore-stock`
3. Select category (Type): **`Integration`**
4. Click **`ADD`**
5. Find and click on `Drugstore Stock` in the integrations list
6. Click **`Download`** and install it
7. Restart Home Assistant

### Method 2: Manual Installation

1. Download this repository
2. Copy the `custom_components/drugstore_stock` folder to your Home Assistant's `custom_components/` directory
3. Restart Home Assistant

## Configuration

1. Access **`Settings` > `Devices and Services` > `Add integration` > look for `Drugstore Stock`**
2. From a name for your list - (optional) choose an area (registered in ha)
3. Click **`Send` > `Finish`**
4. Click **`Configure`**
5. Select if you want **Add, edit or remove a medicine**
6. Follow the card instructions by filling the columns

## Screenshots & Examples

> [Examples](documentation/examples.md)

## Support & Issues

- Report bugs or suggestions at: [Issues](https://github.com/BigPiloto/ha-drugstore-stock/issues)

## License

This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.

