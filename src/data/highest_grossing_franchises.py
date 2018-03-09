import wikitables
import pandas as pd

def get_highest_grossing_franchises():

    tbs = wikitables.import_tables(
                    'List of best-selling video game franchises')
    categories = {
        0:'100 millions',
        1:'50 millions',
        2:'20 millions',
        3:'10 millions',
        4:'5 millions'
    }

    games = []
    grossing_category = []

    for i,  tb in enumerate(tbs):
        fn = [row.get('Franchise name') for row in tb.rows][::2]
        games.extend(fn)
        grossing_category.extend([categories.get(i)]*len(fn))


    df = pd.DataFrame.from_dict(
            {
                'franchise':games,
                'copies_sold':grossing_category,
            }
    )
    return df

if __name__ == '__main__':
    hgf = get_highest_grossing_franchises()
