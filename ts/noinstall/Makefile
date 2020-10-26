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
