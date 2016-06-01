rm replace_lists/*
for l in $(grep -o -E "[A-Z]?[a-z]+[-][a-z]+(\s)?" text/*)
do 
	f=$(awk -v line="$l" 'BEGIN{split(line, orig, ":"); split(orig[1], fname, "/"); print fname[2]}')
	w=$(awk -v line="$l" 'BEGIN{split(line, word, ":"); print word[2]}')
	echo "$w" >> replace_lists/"$f"
done
