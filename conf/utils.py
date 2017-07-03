import os
from shutil import copyfile


def patch_app(app_path):
    # check if source info.plist exists
    source_plist_path = os.path.join(app_path, "Contents")
    source_plist_path = os.path.join(source_plist_path, "Info.plist")
    if not os.path.exists(source_plist_path):
        raise OSError(source_plist_path + " doesn't exist")

    # find patch
    local_path = os.path.dirname(os.path.realpath(__file__))
    patch_path = local_path + "/Info.plist.patch"

    # merge !
    # -- get plist line number
    line_number = 0
    with open(source_plist_path, 'r') as source:
        for line in source:
            line_number += 1

    res_content = ""
    with open(source_plist_path, 'r') as source:
        # plist content but last 2 lines
        for line_idx in range(line_number - 2):
            res_content += source.readline()
        # patch content
        with open(patch_path) as patch_source:
            res_content += patch_source.read()
        # last two lines
        for line_idx in range(line_number - 2, line_number):
            res_content += source.readline()

    # write result
    with open(source_plist_path, 'w') as result:
        result.write(res_content)


def package_app(app_path):
    # check if app exists
    if not os.path.exists(app_path):
        raise OSError(app_path + " doesn't exist")

    # copy script
    local_path = os.path.dirname(os.path.realpath(__file__))
    copyfile(os.path.join(local_path, "../src/urlhandler.py"),
             os.path.join(app_path, "Contents/Resources/Scripts/urlhandler.py"))
