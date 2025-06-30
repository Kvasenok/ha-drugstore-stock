# Adding new list 📋

1. Go to Integration `Drugstore Stock`
2. Click **`Add entry`**
3. Put a name to the list (required) and select an area (optional)
4. Click **`Submit` > `Finish`**

<br>

# Adding new medicine 💊

1. Go to Integration `Drugstore Stock`
2. Click **`Configure`** in the desired list
3. Select **`Add new medicine` > `Send`**
4. Fill in the information: 
- Name of the medicine 
- Initial quantity 
- Minimum quantity 
- Maximum quantity 
- Unit of measurement
5. Click **`Send` > `Finish`**

<br>

# Editing existing medicine 🩹💊

1. Go to Integration `Drugstore Stock`
2. Click **`Configure`** in the desired list
3. Select **`Edit existing medicine` > `Send`**
4. Select the **medicine you want to change > `Submit`**
5. Fill in the information: 
- Name of the medicine 
- Initial quantity 
- Minimum quantity 
- Maximum quantity 
- Unit of measurement
6. Click **`Submit` > `Finish`**

<br>

# Removing existing medicine ❌

1. Go to Integration `Drugstore Stock`
2. Click **`Configure`** in the desired list
3. Select **`Remove existing medicine` > `Send`**
4. Select the **medicine you want to remove > `Submit`**
5. Select **`Confirm removal` > `Send` > `Finish`**

Note: For security the home assistant does not allow to delete an orphan entity automatically, because in the future if it returns will still have its history, if you are sure you want to delete the entity, proceed as follows:

## Removing orphan entity of removed medicine

1. After removing the medicine by the previous instruction, click **`Entity`** and look for the entity removed
2. Click **`Settings` > `Delete` > `Delete`**
