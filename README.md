# Phone Book (Tkinter)

A prime desktop phone book built with Python and Tkinter. Add, search, update, and delete contacts with a clean two-panel layout and persistent storage in `contacts.json`.

## Features
- Add contacts with name, phone, location, and email
- Search by name (case-insensitive, partial matches)
- Edit contacts by double-clicking a list item
- Delete selected contacts
- Auto-save to `contacts.json`

## Tech Stack
- Python 3
- Tkinter (built-in)
- JSON for local storage

## Getting Started

### Prerequisites
- Python 3.8+ (Tkinter included with standard Python on Windows)

### Run
```powershell
python "phone book 1.py"
```

## Usage Tips
- Double-click a contact to edit it, then click **Update Contact**
- Use the **Search** button to filter by name
- To reset the list after a search, close and reopen the app

## Data File
- Contacts are stored locally in `contacts.json` in the same folder as the app

## Project Structure
- `phone book 1.py` - main Tkinter app
- `contacts.json` - saved contacts (auto-created)
- `qrt.png` - asset (if used)

## Roadmap (Ideas)
- Export/import contacts as CSV
- Add duplicate detection
- Improve search to include phone and email
- Add sorting (A-Z, recent)

## License
MIT
