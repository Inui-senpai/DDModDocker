python early:
    import json
    try:
        with open(renpy.config.basedir + "/selectedmod.json", "r") as mod_json:
            temp = json.load(mod_json)
            selectedMod = temp['modName']
    except:
        selectedMod = "DDLC"

    renpy.config.savedir = renpy.config.basedir + "/game/MLSaves/" + selectedMod