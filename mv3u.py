from beets.plugins import BeetsPlugin
import os

rename_cache = os.path.expanduser('~/.cache/beets_mv3u_renames')

class MV3U(BeetsPlugin):
    def __init__(self):
        super(MV3U, self).__init__()

        self.register_listener('item_moved', self.add_rename)
        self.register_listener('item_copied', self.add_rename)
        self.register_listener('import_task_created', self.clear_persistence)
        #self.register_listener('import', self.mv3u)
    
    
    """
    This has been moved to a standalone program because I felt like it. ¯\_(ツ)_/¯
    """
    def mv3u(self):
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


    def clear_persistence(self, task, session):
        if os.path.isfile(rename_cache):
            os.remove(rename_cache)


    def add_rename(self, item):
        src = item.path.decode()
        dst = item.destination().decode()
        with open(rename_cache, 'a') as cache:
            cache.write(f'{src}\t\t{dst}\n')

    
    '''
    def mv3u(self, lib, paths):
        def read_renames() -> dict:
            with open(rename_cache) as cache:
                return dict([line.rstrip('\n').split('\t\t') for line in cache])
'''
        #print(read_renames())

