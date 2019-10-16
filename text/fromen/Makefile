build:
	msgchi -t prg -l eng2cmn telegram:Desktop.strings -o telegram:Desktop_cmn_TW.strings
	msgchi -t prg -l cmn2yue telegram:Desktop_cmn_TW.strings -o telegram:Desktop_yue_HK.strings
	msgchi -t txt -x '^;.*' -l eng2cmn ucblogo:Messages -o ucblogo:Messages.cmn_TW
	msgchi -t txt -x '^;.*' -l cmn2yue ucblogo:Messages.cmn_TW -o ucblogo:Messages.yue_HK
	msgchi -t ini -a _ -l eng2cmn textadept:locale.conf -o textadept:locale.cmn_TW.conf
	msgchi -t ini -a _ -l cmn2yue textadept:locale.cmn_TW.conf -o textadept:locale.yue_HK.conf

install:
	install -d $(DESTDIR)$(DATADIR)/Telegram
	install -m644 telegram:Desktop_cmn_TW.strings $(DESTDIR)$(DATADIR)/Telegram/Desktop_cmn_TW.strings
	install -m644 telegram:Desktop_yue_HK.strings $(DESTDIR)$(DATADIR)/Telegram/Desktop_yue_HK.strings
	install -d $(DESTDIR)$(DATADIR)/logo/logolib
	install -m644 ucblogo:Messages.cmn_TW $(DESTDIR)$(DATADIR)/logo/logolib/Messages.cmn_TW
	install -m644 ucblogo:Messages.yue_HK $(DESTDIR)$(DATADIR)/logo/logolib/Messages.yue_HK
	install -d $(DESTDIR)$(LIBDIR)/textadept/core/locales
	install -m644 textadept:locale.cmn_TW.conf $(DESTDIR)$(LIBDIR)/textadept/core/locales/locale.cmn_TW.conf
	install -m644 textadept:locale.yue_HK.conf $(DESTDIR)$(LIBDIR)/textadept/core/locales/locale.yue_HK.conf

