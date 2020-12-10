# http://l10n-files.qt.io/l10n-files
# https://code.qt.io/cgit/qt/qttranslations.git/tree/translations

build:
	mkdir -p cmn_TW yue_HK
	for i in *.ts; do ts2po --progress none --pot $$i $${i%.ts}.pot; done
	for i in *.pot; do msgchi $$i -l eng2cmn -F -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do po2ts --progress none $$i $${i%.po}.ts; done
	cd cmn_TW; for i in *.ts; do lrelease-qt4 -silent $$i; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done
	cd yue_HK; for i in *.po; do po2ts --progress none $$i $${i%.po}.ts; done
	cd yue_HK; for i in *.ts; do lrelease-qt4 -silent $$i; done

install:
	for i in ???_??; do install -Dm644 $$i/assistant.qm $(DESTDIR)$(DATADIR)/qt4/translations/assistant_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/designer.qm $(DESTDIR)$(DATADIR)/qt4/translations/designer_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/linguist.qm $(DESTDIR)$(DATADIR)/qt4/translations/linguist_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qt.qm $(DESTDIR)$(DATADIR)/qt4/translations/qt_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qt_help.qm $(DESTDIR)$(DATADIR)/qt4/translations/qt_help_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtconfig.qm $(DESTDIR)$(DATADIR)/qt4/translations/qtconfig_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtmobility.qm $(DESTDIR)$(DATADIR)/qt4/translations/qtmobility_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtscript.qm $(DESTDIR)$(DATADIR)/qt4/translations/qtscript_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qscintilla.qm $(DESTDIR)$(DATADIR)/qt4/translations/qscintilla_$$i.qm; done
