build:
	mkdir -p cmn-TW yue-TW
	for i in *.properties; do msgchi -t ini -l eng2cmn $$i -o cmn-TW/$$i.native; done
	cd cmn-TW; for i in *.native; do uni2ascii -a U -l $$i > $${i%.native}; done
	cd cmn-TW; for i in *.native; do msgchi -t ini -l cmn2yue $$i -o ../yue-TW/$$i; done
	cd yue-TW; for i in *.native; do uni2ascii -a U -l $$i > $${i%.native}; done

install:
	for i in ???-??; do install -Dm644 $$i/lucidor:brand.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/branding/$$i/brand.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:viewweb.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/viewweb.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:bookcase.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/bookcase.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:main.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/main.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:booklist.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/booklist.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:preferences.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/preferences.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:viewepub.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/viewepub.properties; done
	for i in ???-??; do install -Dm644 $$i/lucidor:shared.properties $(DESTDIR)$(DATADIR)/lucidor/chrome/locale/$$i/shared.properties; done
	for i in ???-??; do install -Dm644 $$i/openfire:openfire_i18n.properties $(DESTDIR)$(DATADIR)/openfire/resources/i18n/openfire_i18n_$$i.properties; done
	for i in ???-??; do install -Dm644 $$i/biogenesis:messages.properties $(DESTDIR)$(DATADIR)/biogenesis/messages/messages_$$i.properties; done
	for i in ???-??; do install -Dm644 $$i/jsoko:texts.properties $(DESTDIR)$(DATADIR)/jsoko/texts/texts_$$i.properties; done
	for i in ???-??; do install -Dm644 $$i/azardi:brand.properties $(DESTDIR)$(DATADIR)/azardi/chrome/locale/branding/$$i/brand.properties; done
	for i in ???-??; do install -Dm644 $$i/azardi:azardi2.properties $(DESTDIR)$(DATADIR)/azardi/chrome/locale/$$i/azardi2.properties; done
	for i in ???-??; do install -Dm644 $$i/tuxguitar:messages.properties $(DESTDIR)$(DATADIR)/tuxguitar/lang/messages_$$i.properties; done
	for i in ???-??; do install -Dm644 $$i/libreoffice-wizards:resources.properties $(DESTDIR)$(LIBDIR)/libreoffice/share/wizards/resources_$${i/-/_}.properties; done
