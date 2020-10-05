"""
Compute average length of tweets
"""

import sys
import pandas
import argparse
import os.path as osp

script_dir = osp.dirname(__file__)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--num_rows', help='the number of rows to use in the mean calculation', default=10)
    parser.add_argument('tweet_file_index', help='the index number of the  tweet file sitting in the project data directory  that will be used')

    args = parser.parse_args()

    src_file = osp.join(script_dir, '..', 'data', f'IRAhandle_tweets_{args.tweet_file_index}.csv')

    print(f'src_file = {src_file}')
    
    df = pandas.read_csv(src_file, nrows=int(args.num_rows))

    df['content_length'] = df.apply(lambda row: len(row['content']), axis=1)

    print(df['content_length'].mean())

if __name__ == '__main__':
    main()
