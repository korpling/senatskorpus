./0_create_repl_lists.sh
python 1_clean_text.py
./2_tag.sh
python 3_after_tagging.py
./4_convert.sh

zip -r Berliner_Parlamentsprotokolle.zip annis/*
