build:
	mkdir -p cmn_TW yue_TW
	for i in *.ts; do ts2po --progress none --pot $$i $${i%.ts}.pot; done
	for i in *.pot; do msgchi $$i -l eng2cmn -F -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do po2ts --progress none $$i $${i%.po}.ts; done
	cd cmn_TW; for i in *.ts; do lrelease-qt5 -silent $$i; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_TW/$$i; done
	cd yue_TW; for i in *.po; do po2ts --progress none $$i $${i%.po}.ts; done
	cd yue_TW; for i in *.ts; do lrelease-qt5 -silent $$i; done

install:
	cd cmn_TW; for i in l*.qm; do install -Dm644 $$i $(DESTDIR)$(DATADIR)/lxqt/translations/$${i%.qm}/$${i%.qm}_cmn_TW.qm; done
	cd yue_TW; for i in l*.qm; do install -Dm644 $$i $(DESTDIR)$(DATADIR)/lxqt/translations/$${i%.qm}/$${i%.qm}_yue_TW.qm; done
	cd cmn_TW; for i in [!l]*.qm; do install -Dm644 $$i $(DESTDIR)$(DATADIR)/lxqt/translations/lxqt-panel/$${i%.qm}/$${i%.qm}_cmn_TW.qm; done
	cd yue_TW; for i in [!l]*.qm; do install -Dm644 $$i $(DESTDIR)$(DATADIR)/lxqt/translations/lxqt-panel/$${i%.qm}/$${i%.qm}_yue_TW.qm; done
