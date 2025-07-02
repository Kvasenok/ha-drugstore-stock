![hacs custom](https://img.shields.io/badge/hacs-custom-orange.svg)
<!-- ![HACS Default](https://img.shields.io/badge/HACS-Default-blue.svg) -->
![HACS Action](https://github.com/BigPiloto/ha-drugstore-stock/actions/workflows/validate.yaml/badge.svg)
![Validate with hassfest](https://github.com/BigPiloto/ha-drugstore-stock/actions/workflows/hassfest.yaml/badge.svg)
![Release](https://img.shields.io/github/v/release/BigPiloto/ha-drugstore-stock.svg)
![Downloads](https://img.shields.io/github/downloads/BigPiloto/ha-drugstore-stock/total.svg)
![Last commit](https://img.shields.io/github/last-commit/BigPiloto/ha-drugstore-stock.svg)

### _Текст переведен с помощью искусственного интеллекта_ - _Text translated by AI_
# Аптечный Запас (Drugstore Stock)

Управляйте домашним запасом медикаментов с помощью Home Assistant!

**Drugstore Stock** — это интеграция (кастомный компонент) для Home Assistant. Она работает на сервере, обрабатывая и предоставляя данные о запасах медикаментов в виде сущностей Home Assistant.

Для просмотра данных Drugstore Stock напрямую на вашей панели управления (Lovelace), рекомендуется также установить кастомную карточку [Drugstore Stock Card](https://github.com/BigPiloto/ha-drugstore-stock-card). Эта карточка упрощает визуализацию и управление списками запасов через интерфейс Home Assistant.

## Обзор

Интеграция Drugstore Stock позволяет регистрировать и контролировать ваш аптечный запас в Home Assistant, помогая отслеживать доступные количества и своевременно пополнять лекарства.

## Установка

[![Откройте свой экземпляр Home Assistant и откройте репозиторий внутри Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=BigPiloto&repository=ha-drugstore-stock&category=Integration)

### Способ 1: Установка через HACS (рекомендуется)

1. Убедитесь, что у вас установлен [HACS](https://hacs.xyz/) в вашей инстанции Home Assistant
2. Перейдите в **`HACS` > `3 точки` > `Custom repositories`**
3. Добавьте этот URL репозитория: `https://github.com/BigPiloto/ha-drugstore-stock`
4. Выберите категорию (тип): **`Integration`**
5. Нажмите **`ADD`**
6. Найдите и выберите `Drugstore Stock` в списке интеграций
7. Нажмите **`Download`** и установите
8. Перезапустите Home Assistant

### Способ 2: Ручная установка

1. Скачайте этот репозиторий
2. Скопируйте папку `custom_components/drugstore_stock` в каталог `custom_components/` вашего Home Assistant
3. Перезапустите Home Assistant

## Настройка

1. Перейдите в **`Настройки` > `Устройства и сервисы` > `Добавить интеграцию` > найдите `Drugstore Stock`**
2. Введите название для вашего списка — (опционально) выберите зону (зарегистрированную в HA)
3. Нажмите **`Отправить` > `Готово`**
4. Нажмите **`Настроить`**
5. Выберите, хотите ли вы **добавить, редактировать или удалить медикамент**
6. Следуйте инструкциям на карточке, заполняя поля

## Скриншоты и примеры

> [Примеры](documentation/examples.md)

## Поддержка и вопросы

- Сообщайте об ошибках или предлагайте улучшения здесь: [Issues](https://github.com/BigPiloto/ha-drugstore-stock/issues)

## Лицензия

Этот проект распространяется по лицензии MIT — подробнее смотрите в файле [MIT License](LICENSE).
