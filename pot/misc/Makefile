build:
	mkdir -p cmn_TW yue_HK
	for i in *.pot; do msgchi $$i -l eng2cmn | msgattrib --clear-fuzzy -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do msgfmt $$i -o $${i%.po}.mo; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done
	cd yue_HK; for i in *.po; do msgfmt $$i -o $${i%.po}.mo; done

install:
	for i in ???_??; do install -Dm644 $$i/openscad.mo $(DESTDIR)$(DATADIR)/openscad/locale/$$i/LC_MESSAGES/openscad.mo; done
	for i in ???_??; do install -Dm644 $$i/icaro.mo $(DESTDIR)$(DATADIR)/icaro/locale/$$i/LC_MESSAGES/icaro.mo; done
