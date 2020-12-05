#!/bin/bash

#!/bin/sh
while true
do
  if test -f "data/new.csv"; then
      mv data/new.csv data/old.csv
      python engine.py --days=1,2,3
      if cmp -s  data/old.csv  data/new.csv ; then
        echo "Nothing changed"
      else
        echo "Something changed"
        telegram-send --file data/new.csv --caption "Possible slots in coming 3 days"
      fi
  else
      python engine.py --days=1,2,3
      if test -f "data/new.csv"; then
        telegram-send --file data/new.csv --caption "Possible slots in coming 3 days"
      fi
  fi
  sleep 900
done