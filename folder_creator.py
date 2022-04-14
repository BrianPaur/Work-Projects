import os
import pandas as pd

def create_list():
    #reads csv then creates list based on first column
    #empties empty space and formats list names to each be capitalized
    try:
        df = pd.read_csv('Folder_List.csv',delimiter=',')
        df = df.iloc[:,0].str.strip()
        df = df.str.title()
        folders = list(set(df.tolist()))
        return folders
    except:
        print("no Folder_List.csv file found")
        close = int(input("press enter to close"))

def write_folder():
    #uses create_list() and loops through list to create folders
    #if folder already exists it skips to the next item on the list
    folder_names = create_list()
    parent_dir = os.getcwd()
    for items in folder_names:
        if os.path.exists(os.path.join(parent_dir,items)) == True:
            pass
        else:
            path = os.path.join(parent_dir,items)
            os.mkdir(path)

if __name__ == '__main__':
    write_folder()






