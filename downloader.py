from os import close


from pytube import YouTube

def parse_file(file) -> list:
  handle = open(file, 'r')
  lines = [line.strip('\n') for line in handle.readlines()]
  handle.close()
  return lines

def process_item(item: str):
  [song_name, yt_link] = item.split(' - ')
  print('Downloading {}\n'.format(song_name))
  audio_stream = YouTube(yt_link).streams.get_audio_only()
  audio_stream.download(output_path='videos/mp3', filename='{}.mp3'.format(song_name))
  print('Downloaded {}\n'.format(song_name))

lines = parse_file('songs.txt')
[process_item(line) for line in lines]