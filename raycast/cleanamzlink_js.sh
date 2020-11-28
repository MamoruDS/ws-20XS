#!/bin/bash

# @raycast.schemaVersion 1
# @raycast.title Clean Amazon link
# @raycast.author MamoruDS <mamoruds.io@gmail.com>
# @raycast.authorURL https://github.com/MamoruDS/ws-20XS/tree/raycast/raycast
# @raycast.description Purify Amazon goods' link

# @raycast.mode compact
# @raycast.currentDirectoryPath ~
# @raycast.packageName MSScript

version=0.1.0
SCRIPT=$HOME/.config/raycast/scripts
# To using different language preference, override line below
LANG=ja_JP
RT=node
# To using nvm, uncomment line below
# RT=$NVM_DIR/versions/node/$NVM_CUR_VERSION/bin/node
# To using deno, uncomment line below
# RT=deno

# echo $SCRIPT/cleanamzlink.js
link=$($RT $SCRIPT/cleanamzlink.js $(pbpaste))
if [ ! -z $link ]; then
    echo "$link?language=$LANG" | pbcopy
    echo "Replace link successful"
    exit 0
else
    echo "Invalid URL in Clipboard"
    exit 0
fi
# echo $(printenv)
