#!/bin/bash

# @raycast.schemaVersion 1
# @raycast.title GoodLinks Save
# @raycast.author MamoruDS <mamoruds.io@gmail.com>
# @raycast.authorURL https://github.com/MamoruDS/ws-20XS/tree/raycast/raycast
# @raycast.description Save URL from your clipboard to GoodLinks by using url-scheme

# @raycast.mode compact
# @raycast.icon https://goodlinks.app/images/app-icon@2x.png
# @raycast.currentDirectoryPath ~
# @raycast.packageName MSScript
# @raycast.argument1 { "type": "text", "placeholder": "tags" }

version=0.1.2
CONFIG=$HOME/.config/raycast
config=$CONFIG/goodlinks_save.config
# To enable quick sive, change `quick_save=` in your config

if test -f "$config"; then
    source $config
else
    echo "quick_save=false" >$config
fi

# echo "ENV: $RAYCAST_CONFIG"

regex='^https?://'
url=$(pbpaste)
if [[ $url =~ $regex ]]; then
    open "goodlinks://x-callback-url/save?tags=$1&url=$url&quick=$quick_save"
else
    echo "Invalid URL in Clipboard" >&2
    exit 0
fi
