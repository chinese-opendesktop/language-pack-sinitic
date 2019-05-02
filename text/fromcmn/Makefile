build:
	msgchi -t txt -l cmn2yue joe:joerc.cmn_TW -o joe:joerc.yue_HK
	msgchi -t txt -l cmn2yue childsplay:words-cmn_TW -o childsplay:words-yue_HK
	msgchi -t txt -l cmn2yue fbreader:cmn_TW.xml -o fbreader:yue_HK.xml
	msgchi -t txt -l cmn2yue clipbucket:cmn_TW.lang -o clipbucket:yue_HK.lang
	msgchi -t txt -l cmn2yue liblunar:holiday.dat-cmn_TW -o liblunar:holiday.dat-yue_HK
	msgchi -t txt -l cmn2yue zlibrary:cmn_TW.xml -o zlibrary:yue_HK.xml

install:
	install -Dm644 joe:joerc.cmn_TW $(DESTDIR)/etc/joe/joerc.cmn_TW
	install -Dm644 joe:joerc.yue_HK $(DESTDIR)/etc/joe/joerc.yue_HK
	install -Dm644 childsplay:words-cmn_TW $(DESTDIR)$(DATADIR)/childsplay_sp/CPData/PackidData/words-cmn_TW
	install -Dm644 childsplay:words-yue_HK $(DESTDIR)$(DATADIR)/childsplay_sp/CPData/PackidData/words-yue_HK
	install -Dm644 fbreader:cmn_TW.xml $(DESTDIR)$(DATADIR)/FBReader/resources/cmn_TW.xml
	install -Dm644 fbreader:yue_HK.xml $(DESTDIR)$(DATADIR)/FBReader/resources/yue_HK.xml
	install -Dm644 clipbucket:cmn_TW.lang $(DESTDIR)/var/www/html/clipbucket/includes/langs/cmn_TW.lang
	install -Dm644 clipbucket:yue_HK.lang $(DESTDIR)/var/www/html/clipbucket/includes/langs/yue_HK.lang
	install -Dm644 liblunar:holiday.dat-cmn_TW $(DESTDIR)$(DATADIR)/liblunar/holiday.dat-cmn_TW
	install -Dm644 liblunar:holiday.dat-yue_HK $(DESTDIR)$(DATADIR)/liblunar/holiday.dat-yue_HK
	install -Dm644 zlibrary:cmn_TW.xml $(DESTDIR)$(DATADIR)/zlibrary/resources/cmn_TW.xml
	install -Dm644 zlibrary:yue_HK.xml $(DESTDIR)$(DATADIR)/zlibrary/resources/yue_HK.xml
