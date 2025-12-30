#!/bin/bash

# OBS WebSocket Mic Mute -- requires websocat. No authentication rn.
# ./obs-mute.sh mute -> mutes Mic/Aux
# ./obs-mute.sh unmute -> unmutes Mic/Aux
# ./obs-mute.sh foobar -> unmutes Mic/Aux

OBS_HOST="${OBS_HOST:-localhost}"
OBS_PORT="${OBS_PORT:-4455}"
INPUT_NAME="${INPUT_NAME:-Mic/Aux}"
MUTED=$([[ "$1" == "mute" ]] && echo true || echo false)

{ # HACK: I could for the life of me not figure out how to wait for OBS to respond.
  sleep 0.01 # This is my solution to that problem!
  echo '{"op":1,"d":{"rpcVersion":1}}'
  sleep 0.01
  echo '{"op":6,"d":{"requestType":"SetInputMute","requestId":"1","requestData":{"inputName":"'$INPUT_NAME'","inputMuted":'$MUTED'}}}'
  # we're done here
} | websocat "ws://$OBS_HOST:$OBS_PORT"