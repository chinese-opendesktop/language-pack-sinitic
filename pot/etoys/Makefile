build:
	mkdir -p cmn_TW yue_HK
	for i in *.pot; do msgchi $$i -l eng2cmn -F -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do msgfmt $$i -o $${i%.po}.mo; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done
	cd yue_HK; for i in *.po; do msgfmt $$i -o $${i%.po}.mo; done

install:
	for i in ???_??; do mkdir -p $(DESTDIR)$(DATADIR)/etoys/locale/$$i/LC_MESSAGES; cp -a $$i/*.mo $(DESTDIR)$(DATADIR)/etoys/locale/$$i/LC_MESSAGES; done
