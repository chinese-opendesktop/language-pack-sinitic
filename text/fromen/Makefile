build:
	msgchi -t prg -l eng2cmn Desktop.strings -o Desktop_cmn_TW.strings
	msgchi -t prg -l cmn2yue Desktop_cmn_TW.strings -o Desktop_yue_HK.strings
	msgchi -t txt -x '^;.*' -l eng2cmn Messages -o Messages.cmn_TW
	msgchi -t txt -x '^;.*' -l cmn2yue Messages.cmn_TW -o Messages.yue_HK

install:
	install -d $(DESTDIR)$(DATADIR)/Telegram
	install -m644 Desktop_*.strings $(DESTDIR)$(DATADIR)/Telegram
	install -d $(DESTDIR)$(DATADIR)/logo/logolib
	install -m644 Messages.* $(DESTDIR)$(DATADIR)/logo/logolib

