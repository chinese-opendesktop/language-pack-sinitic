build:
	mkdir -p cmn_TW yue_HK
	msgchi -t prg -l eng2cmn telegram:Desktop.strings -o cmn_TW/telegram:Desktop.strings
	msgchi -t prg -l cmn2yue cmn_TW/telegram:Desktop.strings -o yue_HK/telegram:Desktop.strings
	msgchi -t txt -x '^;.*' -l eng2cmn ucblogo:Messages -o cmn_TW/ucblogo:Messages
	msgchi -t txt -x '^;.*' -l cmn2yue cmn_TW/ucblogo:Messages -o yue_HK/ucblogo:Messages
	msgchi -t ini -a _ -l eng2cmn textadept:locale.conf -o cmn_TW/textadept:locale.conf
	msgchi -t ini -a _ -l cmn2yue cmn_TW/textadept:locale.conf -o yue_HK/textadept:locale.conf
	msgchi -t txt -l eng2cmn pebl-battery-SNARC:en.txt -o cmn_TW/pebl-battery-SNARC:en.txt
	msgchi -t txt -l cmn2yue cmn_TW/pebl-battery-SNARC:en.txt -o yue_HK/pebl-battery-SNARC:en.txt

install:
	for i in ???_??; do install -Dm644 $$i/telegram:Desktop.strings $(DESTDIR)$(DATADIR)/Telegram/Desktop_$$i.strings; done
	for i in ???_??; do install -Dm644 $$i/ucblogo:Messages $(DESTDIR)$(DATADIR)/logo/logolib/Messages.$$i; done
	for i in ???_??; do install -Dm644 $$i/textadept:locale.conf $(DESTDIR)$(LIBDIR)/textadept/core/locales/locale.$$i.conf; done
	for i in ???_??; do install -Dm644 $$i/pebl-battery-SNARC:en.txt $(DESTDIR)$(DATADIR)/pebl/battery/SNARC/translations/$$i.txt; done
