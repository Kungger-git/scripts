import os
import shutil


class Manage_iso:
    
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def move(self, distributions):
        # the source directory is always the Downloads folder
        # and the target directory would be the Distributions
        # but there would be a user input for the base distro
        # to know where the iso will be transferred

        base_set = {}
        for index, base in enumerate(os.listdir(self.target), start=1):
            base_set[index] = base
            print(f'{index} - {base}')

        try:
            # user can select which directory the image should be transferred            
            assign_data_path = {}
            for distro in distributions:            
                fmt_path = os.path.split(distro)[-1]
                select_base = int(input(f'\nEnter index to move "{fmt_path}" to its respectful base: '))

                if select_base in base_set:
                    assign_data_path[distro] = os.path.join(self.target, base_set[select_base])
                else:
                    print('\nAbort!')

            for path in assign_data_path:
                fmt_distro = os.path.split(path)[-1]
                fmt_target = os.path.split(assign_data_path[path])[-1]
                print(f'[!] Moving: {fmt_distro} to {fmt_target}...')
                
                shutil.move(path, assign_data_path[path])
                if fmt_distro in os.listdir(os.path.join(self.target, fmt_target)):
                    print(f'[*] {fmt_distro} has been successfully moved!\n')
                else:
                    print(f'[!!] {fmt_distro} refused to move!\n')
        except KeyboardInterrupt:
            print('\nStopped!')

    def get_new_iso(self):
        # goes through the source directory; gets all .iso images
        images = []
        for root, dirs, files in os.walk(self.source):
            for f in files:
                if f.endswith('.iso'):
                    images.append(os.path.join(self.source, f))

        # i dont think this method of looking for iso images
        # is efficient when the image is in a folder
        #for iso in os.listdir(self.source):
        #    if iso.endswith('.iso'):
        #        images.append(os.path.join(self.source, iso))

        if images == []:
            print('[!] No new iso in source directory')
            quit()
        else:
            return images

    def delete(self, distribution):
        # for the delete function, all Distributions from all
        # the folders in the target directory will be listed down,
        # assigned with an index. Select that index,
        # and that distribution will be deleted
        
        fmt_path = os.path.split(distribution)[0]
        fmt_iso = os.path.split(distribution)[1]
        print(f'[!] Deleting: {fmt_iso} from {fmt_path}...')

        # deletes the iso image selected
        os.remove(distribution)

        if not os.path.exists(distribution):
            print(f'[*] {fmt_iso} has been successfully deleted!\n')
        else:
            print(f'[!!] {fmt_iso} refused to be deleted!\n')