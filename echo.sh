#!/bin/bash

#!/bin/sh
while true
do
  if test -f "data/new.csv"; then
      mv data/new.csv data/old.csv
      mv data/new_token.csv data/old_token.csv
      python engine.py --days=0,1,2
      if cmp -s  data/old_token.csv  data/new_token.csv ; then
        echo "Nothing changed"
      else
        echo "Something changed"
        telegram-send --file data/new.csv --caption "Possible slots in coming 3 days"
      fi
  else
      python engine.py --days=0,1,2
      if test -f "data/new.csv"; then
        telegram-send --file data/new.csv --caption "Possible slots in coming 3 days"
      fi
  fi
  sleep 300
done