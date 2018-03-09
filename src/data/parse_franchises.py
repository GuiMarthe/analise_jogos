import re
import pandas as pd
from highest_grossing_franchises import get_highest_grossing_franchises

def parse_frachises(fp):
   '''
    Parse the wikipedia file with franchises.
   '''
   regex = re.compile("\*.+\[\[(.+)\]\].+\\n$")
   franchises = [line for line in fp if line.startswith('*')]
   franchises = [re.findall(regex, line) for line in franchises]
   tidy_franchises = []
   for name in franchises:
       if len(name) == 0 :
           continue
       name = name[0]
       maybe_split_name = name.split('|')
       if len(maybe_split_name) == 1:
           tidy_franchises.append(maybe_split_name)
       else:
           tidy_franchises.append(maybe_split_name[-1:])

   return list(map(lambda x: x[0], tidy_franchises))


if __name__ == '__main__':
    with open('./data/raw/raw_franchises.txt') as raw_franchises:
        tidy_franchises = parse_frachises(raw_franchises)

    df = pd.DataFrame(data = tidy_franchises, columns = ['franchise_name'])
    df.to_csv('./data/processed/franchises.csv', index = False)
    hgf = get_highest_grossing_franchises()
    hgf.to_csv('./data/processed/highest_selling_franchises.csv', index = False)
