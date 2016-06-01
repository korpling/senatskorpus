# run tagger
TAGGER_DIR='../tools/tree-tagger-linux-3.2/cmd/'

cd "$TAGGER_DIR"
for f in ../../../senat/clean/*; do tf=$(awk -v var="$f" 'BEGIN{split(var, file, "/"); split(file[6], arr, "."); print arr[1]}');./tree-tagger-german "$f" > ../../../senat/Berliner_Parlamentsprotokolle/"$tf".tt ; done
