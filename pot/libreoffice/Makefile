build:
	for i in `find . -name *.pot`; do msgchi $$i -l eng2cmn -a "~"| msgattrib --clear-fuzzy -o $${i%.pot}.cmn_TW.po; done
	for i in `find . -name *.cmn_TW.po`; do msgchi $$i -l cmn2yue -o $${i%.cmn_TW.po}.yue_HK.po; done

install:
