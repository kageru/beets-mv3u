from beets.plugins import BeetsPlugin
import os


class MV3U(BeetsPlugin):
    def __init__(self):
        super(MV3U, self).__init__()

        self.register_listener('item_moved', self.mv3u)


    def mv3u(self, item):
        # TODO: cache renames, don’t write playlists for every single file
        # TODO: sorted caching
        src = item.path.decode()
        dst = item.destination().decode()

        playlist_dir = self.config['playlists'].get()
        
        if not playlist_dir:
            return

        for pl in os.listdir(playlist_dir):
            pl = os.path.join(playlist_dir, pl)
            p2 = None
            with open(pl, 'r') as p:
                p2 = [l.replace(src, dst) for l in p]
            with open(pl, 'w') as p:
                p.write(''.join(p2))
            #print(f'Changed entry {src} to {dst} in {pl}')

