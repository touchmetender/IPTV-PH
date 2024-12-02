import json

def generate_m3u():
    playlist_file = 'PHPlaylist'
    output_file = 'playlist.m3u'

    with open(output_file, 'w') as m3u:
        m3u.write("#EXTM3U\n")
        with open(playlist_file, 'r') as file:
            for idx, line in enumerate(file.readlines()):
                line = line.strip()
                if line:
                    m3u.write(f"#EXTINF:-1,Channel {idx + 1}\n")
                    m3u.write(f"{line}\n")

def generate_xtream():
    playlist_file = 'PHPlaylist'
    output_file = 'xtream_playlist.json'

    channels = []
    with open(playlist_file, 'r') as file:
        for idx, line in enumerate(file.readlines()):
            line = line.strip()
            if line:
                channels.append({
                    "name": f"Channel {idx + 1}",
                    "stream_id": idx + 1,
                    "stream_url": line,
                    "category_id": 1,
                    "category_name": "Default Category"
                })

    response = {
        "user_info": {
            "username": "example",
            "password": "example"
        },
        "server_info": {
            "url": "http://example.com",
            "port": 8000
        },
        "channels": channels
    }

    with open(output_file, 'w') as outfile:
        json.dump(response, outfile, indent=4)

if __name__ == '__main__':
    generate_m3u()
    generate_xtream()
