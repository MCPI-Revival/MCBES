#!/bin/bash
DIR="$(cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
cd "$DIR"

if [ -f ./src/MCBES.py ]; then
  MCBES_FILE="./src/MCBES.py"
else
  echo "MCBES not found"
	echo "Downloads can be found at https://github.com/mcbes/mcbes/releases"
	exit 1
fi

python ${MCBES_FILE}
