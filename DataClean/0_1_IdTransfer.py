#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from Util import DataCleanUtil

def transferNumberFromId():
    action_path = '../Data/OutputFile/0_actions.csv'
    song_path = '../Data/OutputFile/0_songs.csv'
    action_file = pd.read_csv(action_path)
    song_file = pd.read_csv(song_path)

    song_dict = DataCleanUtil.id_transfer('song_id',song_path)
    artist_dict = DataCleanUtil.id_transfer('artist_id','../Data/OutputFile/0_songs.csv')
    user_dict = DataCleanUtil.id_transfer('user_id',action_path)

    songs_song_id = song_file['song_id']
    songs_song_number = songs_song_id.map(lambda x:song_dict[x])
    artist_id = song_file['artist_id']
    artist_number = artist_id.map(lambda x:artist_dict[x])

    user_id = action_file['user_id']
    user_number = user_id.map(lambda x:user_dict[x])
    actions_song_id = action_file['song_id']
    actions_song_number = actions_song_id.map(lambda x:song_dict[x])

    song_file['song_id'] = songs_song_number
    song_file['artist_id'] = artist_number

    action_file['user_id'] = user_number
    action_file['song_id'] = actions_song_number

    song_file.to_csv('../Data/OutputFile/0_1_songs.csv',index=False)
    action_file.to_csv('../Data/OutputFile/0_1_actions.csv',index=False)

if __name__=='__main__':
    transferNumberFromId()

