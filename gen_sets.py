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


        # Get the pieces, find the universe and create mapping
        # So we can get the 1024 without overlapping hint names
        sheet_ranges = ['P1!A2:B', 'P2!A2:B', 'P3!A2:B', 'Enemy!A2:B']
        result = sheet.values().batchGet(
            spreadsheetId=sheet_ids['mad space'],
            ranges=sheet_ranges).execute()
        values = result.get('valueRanges', [])

        piece_ids = set()
        piece_map = list()

        for idx, v in enumerate(values[:-1]):
            print(v['values'])
            d = dict()
            for hint_val in v['values']:
                val = int(hint_val[1], 0)
                d[hint_val[0]] = val
                piece_ids.add(val)
            piece_map.append(d)

        for hint_val in values[-1]['values']:
            val = int(hint_val[1], 0)
            piece_ids.add(val)
            piece_map[0][hint_val[0]] = val
            piece_map[1][hint_val[0]] = val


        # 1024 processing
        dict_1024 = dict()
        inv_dict_1024 = dict()

        sheet_range = '1024!A2:D'
        result = sheet.values().get(
            spreadsheetId=sheet_ids['mad space'],
            range=sheet_range).execute()

        unf_1024 = result.get('values', [])

        # In case there are some pieces not in 1024
        pieces_1024 = set()

        for combo in unf_1024:
            combo_pieces = {
                piece_map[0][combo[1]],
                piece_map[1][combo[2]],
                piece_map[2][combo[3]]}
            dict_1024[int(combo[0])] = combo_pieces
            inv_dict_1024[tuple(combo_pieces)] = int(combo[0])

            pieces_1024.update(combo_pieces)

        diff = piece_ids.difference(pieces_1024)

        # Set cover
        # Yay NP problems, we bitcoin now
        # Greedy algo so not guaranteed minimum

        cover_1024 = set()
        cover_ids = []

        bucket_queue = [list(dict_1024.values()),[],[]]

        # We know that this will always exit
        # As this will eventually become pieces_1024
        # If we let it continue
        while(len(pieces_1024 - cover_1024) != 0):
            print(f'Difference: {len(pieces_1024 - cover_1024)}')
            for bucket in bucket_queue:
                if bucket:
                    cover_1024.update(bucket[0])
                    cover_ids.append(inv_dict_1024[tuple(bucket[0])])
                    break
            next_bucket_queue = [[], [], []]
            for bucket in bucket_queue:
                for combo in bucket:
                    intersect = combo & cover_1024
                    if len(intersect) < 3:
                        next_bucket_queue[len(intersect)].append(combo)
            bucket_queue = next_bucket_queue

        print(f'Use these {len(cover_ids)} sets to practice:')
        print(f'{cover_ids}')

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
