## Copyright 2022 Azariel Del Carmen (GanstaKingofSA)

python early:
    import os
    import json

    def save_path(save_directory):
        if renpy.macintosh:
            rv = "~/Library/RenPy/DD-ModDocker/" + save_directory
            return os.path.expanduser(rv)

        elif renpy.windows:
            if 'APPDATA' in os.environ:
                return os.environ['APPDATA'] + "/RenPy/DD-ModDocker/" + save_directory
            else:
                rv = "~/RenPy/DD-ModDocker/" + renpy.config.save_directory
                return os.path.expanduser(rv)

        else:
            rv = "~/.renpy/DD-ModDocker/" + save_directory
            return os.path.expanduser(rv)
    
    try:
        with open(renpy.config.basedir + "/selectedmod.json", "r") as mod_json:
            temp = json.load(mod_json)
            selectedMod = temp['modName']
    except IOError:
        selectedMod = "DDLC"

    renpy.config.savedir = save_path(selectedMod)

    if os.path.exists(renpy.config.basedir + "/game/MLSaves"):
        for src, dirs, files in os.walk(renpy.config.basedir + "/game/MLSaves"):
            for d in dirs:
                src_dir = os.path.join(src, d)
                dst_dir = src_dir.replace(src, renpy.config.savedir)
                shutil.move(src_dir, dst_dir)