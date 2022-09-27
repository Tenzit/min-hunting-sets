# Minimum Hunting Sets

This repo is supposed to contain a script to find
the minimum sets needed to encounter each piece at least once.

Unfortunately that's a hard problem so we do a greedy
approximation instead.

For more information about why it's hard, see the [set-cover problem](https://en.wikipedia.org/wiki/Set_cover_problem)

## Requirements

This project was developed on Linux and uses python3-venv to manage
dependencies.

```bash
sudo apt install python3-venv
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

This project uses the [Google Sheets API](https://developers.google.com/sheets/api) to access the 1024 docs.
You will need to [make your own API key](https://stackoverflow.com/questions/46583052/http-google-sheets-api-v4-how-to-access-without-oauth-2-0/46583300#46583300) and place it in a file `key.py` in this directory.

```bash
echo "GOOGLE_API_KEY='<YOUR_API_KEY_HERE>'" > key.py
```

## Usage

The only gotcha here is the stage name needs to be in quotes

```bash
python3 gen_sets.py '<STAGE_NAME>'
```
