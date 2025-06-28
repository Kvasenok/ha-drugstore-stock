# Drugstore Stock

[🇧🇷 Read in Brazilian Portuguese](README.pt-br.md)

Manage your household medicine stock with Home Assistant!

## Overview

Drugstore Stock integration allows you to register and monitor your medicine inventory in Home Assistant, helping you keep track of available quantities and identify when it’s time to restock.

## Installation

### Method 1: HACS Installation (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance;
2. Go to **HACS > 3 dots > Custom repositories**;
3. Add this repository URL: `https://github.com/BigPiloto/ha-drugstore-stock`;
3. Select category (Type): `Integration`;
4. Click `ADD`;
5. Find and click on `Drugstore Stock` in the integrations list;
6. Click Download and install it;
7. Restart Home Assistant.

### Method 2: Manual Installation

1. Download this repository.
2. Copy the `custom_components/drugstore_stock` folder to your Home Assistant's `custom_components/` directory.
3. Restart Home Assistant.

## Configuration

1. Access ** Settings> Devices and Services> Add integration> look for `Drugstore Stock` **;
2. From a name for your list - (optional) choose an area (registered in ha);
3. Click ** `send`>` finish` **;
4. Click `Configure`
5. Select if you want ** Add, edit or remove a medicine **
6. Follow the card instructions by filling the columns.

## Screenshots & Examples

> [Examples](documentation/examples.md)

## Support & Issues

- Report bugs or suggestions at: [Issues](https://github.com/BigPiloto/ha-drugstore-stock/issues)

## License

This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.

