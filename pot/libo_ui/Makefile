build:
	cp -a templates cmn_TW
	cd templates; for i in `find . -name *.pot`; do msgchi $$i -l eng2cmn -a "~"| msgattrib --clear-fuzzy -o ../cmn_TW/$${i%.pot}.po; rm ../cmn_TW/$$i; done
	cp -a cmn_TW yue_HK
	cd cmn_TW; for i in `find . -name *.po`; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done

install:
