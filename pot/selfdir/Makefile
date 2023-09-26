build:
	mkdir -p cmn_TW yue_TW
	for i in *.pot; do msgchi $$i -l eng2cmn -F -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do msgfmt $$i -o $${i%.po}.mo; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_TW/$$i; done
	cd yue_TW; for i in *.po; do msgfmt $$i -o $${i%.po}.mo; done

install:
	for i in ???_??; do install -Dm644 $$i/lenmus.mo $(DESTDIR)$(DATADIR)/lenmus/5.6.2/locale/$$i/lenmus_$$i.mo; done
	for i in ???_??; do install -Dm644 $$i/wxmidi.mo $(DESTDIR)$(DATADIR)/lenmus/5.6.2/locale/$$i/wxmidi_$$i.mo; done
	for i in ???_??; do install -Dm644 $$i/openscad.mo $(DESTDIR)$(DATADIR)/openscad/locale/$$i/LC_MESSAGES/openscad.mo; done
	for i in ???_??; do install -Dm644 $$i/icaro.mo $(DESTDIR)$(DATADIR)/icaro/locale/$$i/LC_MESSAGES/icaro.mo; done
	for i in ???_??; do install -Dm644 $$i/openastro.mo $(DESTDIR)$(DATADIR)/openastro.org/locale/$$i/LC_MESSAGES/openastro.mo; done
	for i in ???_??; do install -Dm644 $$i/sunflower.mo $(DESTDIR)$(DATADIR)/sunflower/translations/$$i/LC_MESSAGES/sunflower.mo; done
	for i in ???_??; do install -Dm644 $$i/smc.mo $(DESTDIR)$(DATADIR)/smc/translations/$$i/LC_MESSAGES/Secret\ Maryo\ Chronicles.mo; done
	for i in ???_??; do install -Dm644 $$i/bCNC.mo $(DESTDIR)$(DATADIR)/bcnc/locale/$$i/LC_MESSAGES/bCNC.mo; done
	for i in ???_??; do install -Dm644 $$i/engine.po $(DESTDIR)$(DATADIR)/0ad/l10n/$$i.engine.po; done
	for i in ???_??; do install -Dm644 $$i/joe.po $(DESTDIR)$(DATADIR)/joe/lang/$$i.po; done
	for i in ???_??; do install -Dm644 $$i/winff.po $(DESTDIR)$(DATADIR)/winff/languages/winff.$$i.po; done
	for i in ???_??; do install -Dm644 $$i/skychart.po $(DESTDIR)$(DATADIR)/skychart/data/language/skychart.$$i.po; done
	for i in ???_??; do install -Dm644 $$i/cups.po $(DESTDIR)$(DATADIR)/locale/$$i/cups_$$i.po; done
	for i in ???_??; do install -Dm644 $$i/exe.po $(DESTDIR)$(DATADIR)/exe/locale/$$i/exe_$$i.po; done
	for i in ???_??; do install -Dm644 $$i/universal-applets.mo $(DESTDIR)$(DATADIR)/locale/applets/LC_MESSAGES/universal-$$i.mo; done
	for i in ???_??; do install -Dm644 $$i/screenlets-manager.mo $(DESTDIR)$(DATADIR)/locale/manager/LC_MESSAGES/screenlets-$$i.mo; done
	for i in ???_??; do install -Dm644 $$i/mcm.mo $(DESTDIR)/usr/lib/mcm/i18n/locale/$$i/LC_MESSAGES/mcm.mo; done
	for i in ???_??; do install -Dm644 $$i/Viewmol.mo $(DESTDIR)/usr/lib64/viewmol/locale/$$i/LC_MESSAGES/Viewmol.mo; done
	for i in ???_??; do install -Dm644 $$i/yudit.mo $(DESTDIR)$(DATADIR)/yudit/locale/$$i/LC_MESSAGES/messages.mo; done
	for i in ???_??; do install -Dm644 $$i/discwrapper.mo $(DESTDIR)$(DATADIR)/discwrapper/po/$$i/discwrapper.mo; done
	for i in ???_??; do install -Dm644 $$i/oqapy.mo $(DESTDIR)$(DATADIR)/oqapy/locale/$$i/LC_MESSAGES/oqapy.mo; done
	for i in ???_??; do install -Dm644 $$i/ulipad.mo $(DESTDIR)$(DATADIR)/ulipad/lang/$$i/ulipad_$$i.mo; done
	for i in ???_??; do install -Dm644 $$i/doublecmd.po $(DESTDIR)/usr/lib64/doublecmd/language/doublecmd.$$i.po; done
	for i in ???_??; do install -Dm644 $$i/easymp3gain.po $(DESTDIR)$(DATADIR)/easymp3gain/lang/easymp3gain.$$i.po; done
	for i in ???_??; do install -Dm644 $$i/lazpaint.po $(DESTDIR)$(DATADIR)/lazpaint/i18n/lazpaint.$$i.po; done
	for i in ???_??; do install -Dm644 $$i/meandmyshadow.po $(DESTDIR)$(DATADIR)/meandmyshadow/data/locale/$$i.po; done
	for i in ???_??; do install -Dm644 $$i/ufo2000.po $(DESTDIR)$(DATADIR)/ufo2000/translations/ufo2000-$$i.po; done
	for i in ???_??; do install -Dm644 $$i/WikidPad.po $(DESTDIR)$(DATADIR)/wikidpad/WikidPad_$$i.po; done
	for i in ???_??; do install -Dm644 $$i/nelson.mo $(DESTDIR)/usr/libexec/nelson/locale/$$i/LC_MESSAGES/nelson.mo; done
	for i in ???_??; do install -Dm644 $$i/tlpkg.mo $(DESTDIR)$(DATADIR)/texlive/tlpkg/translations/$$i.po; done
	for i in ???_??; do install -Dm644 $$i/AC.mo $(DESTDIR)$(DATADIR)/assaultcube/packages/locale/$$i/LC_MESSAGES/AC.mo; done
	for i in ???_??; do install -Dm644 $$i/Editra.mo $(DESTDIR)$(LIBDIR)/python2.7/site-packages/Editra/locale/$$i/LC_MESSAGES/Editra.mo; done
	for i in ???_??; do install -Dm644 $$i/humanize.mo $(DESTDIR)/lib/$(PYTHON)/site-packages/humanize/locale/$$i/LC_MESSAGES/humanize.mo; done
	for i in ???_??; do install -Dm644 $$i/mu.mo $(DESTDIR)/lib/$(PYTHON)/site-packages/mu/locale/$$i/LC_MESSAGES/mu.mo; done
	for i in ???_??; do install -Dm644 $$i/thonny.mo $(DESTDIR)/lib/$(PYTHON)/site-packages/thonny/locale/$$i/LC_MESSAGES/thonny.mo; done
	for i in ???_??; do install -Dm644 $$i/notebook.mo $(DESTDIR)/lib/$(PYTHON)/site-packages/notebook/i18n/$$i/LC_MESSAGES/notebook.mo; done
	for i in ???_??; do install -Dm644 $$i/safeeyes.mo $(DESTDIR)/lib/$(PYTHON)/site-packages/safeeyes/config/locale/$$i/LC_MESSAGES/safeeyes.mo; done
	for i in ???_??; do install -Dm644 $$i/phpmyadmin.mo $(DESTDIR)$(DATADIR)/phpMyAdmin/locale/$$i/LC_MESSAGES/phpmyadmin.mo; done
	for i in ???_??; do install -Dm644 $$i/sqlparser.mo $(DESTDIR)$(DATADIR)/phpMyAdmin/SqlParser5/locale/$$i/LC_MESSAGES/sqlparser.mo; done
	for i in ???_??; do install -Dm644 $$i/phpldapadmin.mo $(DESTDIR)$(DATADIR)/phpldapadmin/locale/$$i/LC_MESSAGES/messages.mo; done
	for i in ???_??; do install -Dm644 $$i/frontend.mo $(DESTDIR)$(DATADIR)/zabbix/locale/$$i/LC_MESSAGES/frontend.mo; done
	for i in ???_??; do install -Dm644 $$i/PrusaSlicer.mo $(DESTDIR)$(DATADIR)/PrusaSlicer/localization/$$i/PrusaSlicer.mo; done
	for i in ???_??; do install -Dm644 $$i/vim.mo $(DESTDIR)$(DATADIR)/vim/vim82/lang/$$i/LC_MESSAGES/vim.mo; done
