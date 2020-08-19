build:
	mkdir -p cmn_TW yue_HK
	for i in *.ts; do ts2po --progress none --pot $$i $${i%.ts}.pot; done
	for i in *.pot; do msgchi $$i -l eng2cmn | msgattrib --clear-fuzzy -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do po2ts $$i $${i%.po}.ts; done
	cd cmn_TW; for i in *.ts; do lrelease-qt5 $$i; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done
	cd yue_HK; for i in *.po; do po2ts $$i $${i%.po}.ts; done
	cd yue_HK; for i in *.ts; do lrelease-qt5 $$i; done

install:
	for i in ???_??; do install -Dm644 $$i/minitube.qm $(DESTDIR)$(DATADIR)/minitube/locale/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qiviewer.qm $(DESTDIR)$(DATADIR)/qiviewer/locale/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/skype.qm $(DESTDIR)$(DATADIR)/skype/lang/skype_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/chessx.qm $(DESTDIR)$(DATADIR)/chessx/lang/chessx_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/vym.qm $(DESTDIR)$(DATADIR)/vym/lang/vym.$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/sonic-pi.qm $(DESTDIR)$(DATADIR)/sonic-pi/lang/sonic-pi_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/dooble.qm $(DESTDIR)/usr/libexec/dooble/Translations/dooble_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/ffDiaporama.qm $(DESTDIR)$(DATADIR)/ffDiaporama/locale/ffDiaporama_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtparted.qm $(DESTDIR)$(DATADIR)/qtparted/locale/qtparted_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/fontmatrix.qm $(DESTDIR)$(DATADIR)/fontmatrix/qm/fontmatrix-$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/instruments.qm $(DESTDIR)$(DATADIR)/mscore-2.2/locale/instruments_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/mscore.qm $(DESTDIR)$(DATADIR)/mscore-2.2/locale/mscore_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/muse.qm $(DESTDIR)$(DATADIR)/muse-3.0/locale/muse_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/vmpk.qm $(DESTDIR)$(DATADIR)/vmpk/locale/vmpk_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/librecad.qm $(DESTDIR)$(DATADIR)/librecad/qm/librecad_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/launchy.qm $(DESTDIR)$(DATADIR)/launchy/translations/launchy_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/retroshare.qm $(DESTDIR)$(DATADIR)/retroshare/translations/retroshare_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/shotcut.qm $(DESTDIR)$(DATADIR)/shotcut/translations/shotcut_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/sigil.qm $(DESTDIR)$(DATADIR)/sigil/translations/sigil_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/smplayer.qm $(DESTDIR)$(DATADIR)/smplayer/translations/smplayer_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/smtube.qm $(DESTDIR)$(DATADIR)/smtube/translations/smtube_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/stopmotion.qm $(DESTDIR)$(DATADIR)/stopmotion/translations/stopmotion_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qscreenshot.qm $(DESTDIR)$(DATADIR)/qscreenshot/translations/qscreenshot_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/pdfmixtool.qm $(DESTDIR)$(DATADIR)/pdfmixtool/translations/pdfmixtool_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/OpenShot.qm $(DESTDIR)/usr/lib/python3.8/site-packages/openshot_qt/language/OpenShot.$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/otter-browser.qm $(DESTDIR)$(DATADIR)/otter-browser/locale/otter-browser_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/cortina.qm $(DESTDIR)$(DATADIR)/qt4/translations/cortina/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/dsbbg.qm $(DESTDIR)$(DATADIR)/dsbbg/dsbbg_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/photoflare.qm $(DESTDIR)$(DATADIR)/photoflare/languages/$$i.qm; done
