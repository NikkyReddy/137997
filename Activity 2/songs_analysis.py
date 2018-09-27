import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
excel = '/home/NikhilReddy/songs_data.xls'

songs = pd.read_excel(excel,rows = [x for x in range(7576)])
Album = pd.DataFrame(songs)
print(Album.describe())


Album.to_excel('Al.xls')
print(Album.head())

Album_Top10 = (Album[['year','songtitle','artistname','Top10']])
Album_sorted_Top10 = Album_Top10.sort_values('Top10',ascending=False)
Album_sorted_Top10.loc[Album_sorted_Top10.Top10 == 1, 'Reached top TEN'] = 'Yes'
Album_sorted_Top10.loc[Album_sorted_Top10.Top10 == 0, 'Reached top TEN'] = 'No'
print(Album_sorted_Top10)

# separating Michael Jackson songs which topped in the year
michael_songs = Album_sorted_Top10.loc[Album_sorted_Top10['artistname'] == 'Michael Jackson']
michael_songs.to_excel('michael.xls')

#songs released in 2010
songs_in_2010 = Album.loc[Album['year'] == 2010]
songs_in_2010.to_excel('songs in 2010.xls')
#taking average tempo value
mean_tempo = Album['tempo'].mean()

#seperating tempo
Album_tempo = (Album[['year','songtitle','artistname','tempo']])
#tempo greater than mean values
tempo_greater_than_mean = Album_tempo.loc[Album['tempo'] > mean_tempo]

# sorting tempo greater than mean values
tempo_greater_than_mean_sorted = tempo_greater_than_mean.sort_values('tempo',ascending=False)
tempo_greater_than_mean_sorted.to_excel('tempo_greater_than_mean.xls')