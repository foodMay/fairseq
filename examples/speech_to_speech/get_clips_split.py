# get_clips_split

import argparse
import os
from pathlib import Path
from re import S
import shutil
from tqdm import tqdm
import pandas as pd
import csv

def get_list(args):
    
    train_list = []
    dev_list = []
    test_list =[]
    
    with open(args.train_tsv_path, 'r') as tsv_train:
        file_train = csv.reader(tsv_train)
        for line in file_train:
            id = ','.join(line).split('\t')[0]
            train_list.append(id)
        print(train_list[:3])
 
    with open(args.dev_tsv_path, 'r') as tsv_dev:
        file_dev = csv.reader(tsv_dev)
        for line in file_dev:
            id = ','.join(line).split('\t')[0]
            dev_list.append(id)
        print(dev_list[:3])     

    with open(args.test_tsv_path, 'r') as tsv_test:
        file_test = csv.reader(tsv_test)
        for line in file_test:
            id = ','.join(line).split('\t')[0]
            test_list.append(id)
        print(test_list[:3])
        
    print('train list len:', len(train_list))
    print('den list len:', len(dev_list))
    print('test list len:', len(test_list))

    return train_list, dev_list, test_list


def get_clips_split(args):

    train_list, dev_list, test_list = get_list(args)
    missing_list = []
    
    for clip in tqdm(os.listdir(args.clips_path)):
        if clip in train_list:
            # pass
            base = args.clips_path
            clip_src = os.path.join(base, clip)
            # print(base)
            # print(clip_src)
            dest = args.train_dir
            output = os.path.join(dest, clip)
            # print(dest)
            # print(output)
            # break
            shutil.move(clip_src, output)
            # break

        elif clip in dev_list:
            # pass
            base = args.clips_path
            clip_src = os.path.join(base, clip)
            dest = args.dev_dir
            output = os.path.join(dest, clip)
            shutil.move(clip_src, output)

        elif clip in test_list:
            # pass
            base = args.clips_path
            clip_src = os.path.join(base, clip)
            dest = args.test_dir
            output = os.path.join(dest, clip)
            shutil.move(clip_src, output)

        else:
            missing_list.append(clip)
    print('missing list len:', len(missing_list))

def main():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--train_tsv_path", required=True, type=str, help="train audio tsv directory"
    )
    parser.add_argument(
        "--dev_tsv_path", required=True, type=str, help="dev audio tsv directory"
    )
    parser.add_argument(
        "--test_tsv_path", required=True, type=str, help="test audio tsv directory"
    )
    parser.add_argument(
        "--clips_path", required=True, type=str, help=" audio clips directory"
    )
    parser.add_argument(
        "--train_dir", required=True, type=str, help="output split train directory"
    )
    parser.add_argument(
        "--dev_dir", required=True, type=str, help="output split dev directory"
    )
    parser.add_argument(
        "--test_dir", required=True, type=str, help="output split test directory"
    )

    args = parser.parse_args()

    get_clips_split(args)


if __name__ == '__main__':
	main()