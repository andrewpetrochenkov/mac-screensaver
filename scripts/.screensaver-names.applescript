#!/usr/bin/osascript

tell application "System Events"
    repeat with ss in screen savers
        log (name of ss as text)
    end repeat
end tell
