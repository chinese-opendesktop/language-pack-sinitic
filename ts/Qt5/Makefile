# http://l10n-files.qt.io/l10n-files
# https://code.qt.io/cgit/qt/qttranslations.git/tree/translations

build:
	mkdir -p cmn_TW yue_HK
	for i in *.ts; do ts2po --progress none --pot $$i $${i%.ts}.pot; done
	for i in *.pot; do msgchi $$i -l eng2cmn -F -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do po2ts $$i $${i%.po}.ts; done
	cd cmn_TW; for i in *.ts; do lrelease-qt5 $$i; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done
	cd yue_HK; for i in *.po; do po2ts $$i $${i%.po}.ts; done
	cd yue_HK; for i in *.ts; do lrelease-qt5 $$i; done

install:
	for i in ???_??; do install -Dm644 $$i/assistant.qm $(DESTDIR)$(DATADIR)/qt5/translations/assistant_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/designer.qm $(DESTDIR)$(DATADIR)/qt5/translations/designer_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/linguist.qm $(DESTDIR)$(DATADIR)/qt5/translations/linguist_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qt.qm $(DESTDIR)$(DATADIR)/qt5/translations/qt_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qt_help.qm $(DESTDIR)$(DATADIR)/qt5/translations/qt_help_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtbase.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtbase_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtconnectivity.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtconnectivity_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtdeclarative.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtdeclarative_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtlocation.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtlocation_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtmultimedia.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtmultimedia_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtquickcontrols.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtquickcontrols_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtquickcontrols2.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtquickcontrols2_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtscript.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtscript_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtserialport.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtserialport_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtwebengine.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtwebengine_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtwebsockets.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtwebsockets_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtxmlpatterns.qm $(DESTDIR)$(DATADIR)/qt5/translations/qtxmlpatterns_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/ifw.qm $(DESTDIR)$(DATADIR)/ifw/translations/ifw_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtcreator.qm $(DESTDIR)$(DATADIR)/qtcreator/translations/qtcreator_$$i.qm; done
