DIR="$(dirname "${BASH_SOURCE[0]}")"  # get the directory name
DIR="$(realpath "${DIR}")"    # resolve its full path if need be
echo $DIR
python3 $DIR/Codes/01_extra/03_openResultsFromGoogleSearch.py "$@"
