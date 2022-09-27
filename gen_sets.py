from key import GOOGLE_API_KEY

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

stages = [
    'wild canyon', 'pumpkin hill', 'aquatic mine', 'death chamber',
    'meteor herd', 'dry lagoon', 'egg quarters', 'security hall',
    'mad space']

sheet_ids = {
    stages[0]: '1TRSzEhM3dA5-lxJSuvH69yIp_q6jeyr2IAzD82ntsWc',
    stages[1]: '1SnxHaSy6QdcC5H5p2REDaUH16SQmSuQe25gUQrYHPYw',
    stages[2]: '1bgfRrV-7_uLisVOsMJsumvqRn_v_ZcTgi_wo8hLts1I',
    stages[3]: '1mu96EXwd-QjTaCMF51DDbdC_FyMT8c2rwiBeErhNzMY',
    stages[4]: '1BlaVewvlDiZzeDZKbvnPKwh5shFNTXROxIR9PhQFMus',
    stages[5]: '1cshE5NSWTEn2EqyqIayxqkNoaQsmwQcj172z6xJtC8M',
    stages[6]: '12oyypJ5ntB6Jf7mAwVXBf9nt1VTxbHybovtGTDkWCYk',
    stages[7]: '1NtosoocEfRRxfr35ZONXh-k7KxtAmVszbuLygTkXZBY',
    stages[8]: '1Srs2AA4XyMtimZ4n2SBUQqKAP0jL1VuPb3kkQvkPjeM'}

def main():
    try:
        service = build('sheets', 'v4', developerKey=GOOGLE_API_KEY)
        sheet = service.spreadsheets()
        sheet_ranges = ['P1!A2:A', 'P2!A2:A', 'P3!A2:A', 'Enemy!A2:A']
        result = sheet.values().batchGet(
            spreadsheetId=sheet_ids['egg quarters'], ranges=sheet_ranges).execute()
        values = result.get('valueRanges', [])
        print(values)
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
