build:
	mkdir -p cmn_TW yue_HK
	for i in *.ts; do ts2po --progress none --pot $$i $${i%.ts}.pot; done
	for i in *.pot; do msgchi $$i -l eng2cmn -F -o cmn_TW/$${i%.pot}.po; done
	cd cmn_TW; for i in *.po; do po2ts --progress none $$i $${i%.po}.ts; done
	cd cmn_TW; for i in *.ts; do lrelease-qt5 -silent $$i; done
	cd cmn_TW; for i in *.po; do msgchi $$i -l cmn2yue -o ../yue_HK/$$i; done
	cd yue_HK; for i in *.po; do po2ts --progress none $$i $${i%.po}.ts; done
	cd yue_HK; for i in *.ts; do lrelease-qt5 -silent $$i; done

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
	for i in ???_??; do install -Dm644 $$i/OpenShot.qm $(DESTDIR)/usr/lib/python3.8/site-packages/openshot_qt/language/OpenShot.$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/otter-browser.qm $(DESTDIR)$(DATADIR)/otter-browser/locale/otter-browser_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/cortina.qm $(DESTDIR)$(DATADIR)/qt4/translations/cortina/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/dsbbg.qm $(DESTDIR)$(DATADIR)/dsbbg/dsbbg_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/photoflare.qm $(DESTDIR)$(DATADIR)/photoflare/languages/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qmetro.qm $(DESTDIR)$(DATADIR)/qmetro/locale/$$i.lng; done
	for i in ???_??; do install -Dm644 $$i/wazapp.ts $(DESTDIR)$(DATADIR)/wazapp/i18n/$$i.ts; done
	for i in ???_??; do install -Dm644 $$i/photivo.qm $(DESTDIR)$(DATADIR)/photivo/Translations/photivo_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/ktoon.qm $(DESTDIR)$(DATADIR)/ktoon/data/translations/ktoon_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/cobras.ts $(DESTDIR)$(DATADIR)/cobras/cobras_$$i.ts; done
	for i in ???_??; do install -Dm644 $$i/chains.qm $(DESTDIR)$(DATADIR)/chains/data/lang/chains_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/2mandvd.qm $(DESTDIR)$(DATADIR)/2ManDVD/2mandvd_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/cuneiform-qt.qm $(DESTDIR)$(DATADIR)/apps/cuneiform-qt/cuneiform-qt_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qsopcast.qm $(DESTDIR)$(DATADIR)/apps/qsopcast/language_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/arduide.qm $(DESTDIR)$(DATADIR)/arduino-ide/translations/arduide_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/basic256.qm $(DESTDIR)$(DATADIR)/basic256/basic256_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/canorus.qm $(DESTDIR)$(DATADIR)/canorus/lang/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/cr3.qm $(DESTDIR)$(DATADIR)/cr3/i18n/cr3_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/crosti.qm $(DESTDIR)$(DATADIR)/crosti/system/translations/crosti_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/cuberok.qm $(DESTDIR)$(DATADIR)/cuberok/locale/cuberok_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/drawpile.qm $(DESTDIR)$(DATADIR)/drawpile/drawpile/i18n/drawpile_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/everpad.qm $(DESTDIR)$(DATADIR)/everpad/i18n/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/feff.qm $(DESTDIR)$(DATADIR)/feff/languages/feff_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/Gambit.qm $(DESTDIR)$(DATADIR)/gambitchess/nls/Gambit_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/hotshots.qm $(DESTDIR)$(DATADIR)/hotshots/lang/hotshots_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/hplip.qm $(DESTDIR)$(DATADIR)/hplip/data/localization/hplip_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/jag.qm $(DESTDIR)$(DATADIR)/jag/data/lang/jag_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/kseg.qm $(DESTDIR)$(DATADIR)/kseg/locale/kseg_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/ldview.qm $(DESTDIR)$(DATADIR)/ldview/ldview_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/leechcraft_cpuload_qml.ts $(DESTDIR)$(DATADIR)/leechcraft/qml5/cpuload/ts/leechcraft_cpuload_qml_$$i.ts; done
	for i in ???_??; do install -Dm644 $$i/leechcraft_lemon_qml.ts $(DESTDIR)$(DATADIR)/leechcraft/qml5/lemon/ts/leechcraft_lemon_qml_$$i.ts; done
	for i in ???_??; do install -Dm644 $$i/librepcb.qm $(DESTDIR)$(DATADIR)/librepcb/i18n/librepcb_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/mandelbulber2.qm $(DESTDIR)$(DATADIR)/mandelbulber2/language/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/mandelbulber2:formula.qm $(DESTDIR)$(DATADIR)/mandelbulber2/language/formula_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/mando.qm $(DESTDIR)$(DATADIR)/mando/i18n/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/manslide.qm $(DESTDIR)$(DATADIR)/manslide/manslide_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/meteo_qt.qm $(DESTDIR)$(DATADIR)/meteo_qt/translations/meteo-qt_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/nem-nem.qm $(DESTDIR)$(DATADIR)/nem-nem/nem-nem_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/nmapsi4.qm $(DESTDIR)$(DATADIR)/nmapsi4/locale/nmapsi4_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/nootka.qm $(DESTDIR)$(DATADIR)/nootka/lang/nootka_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/octave.qm $(DESTDIR)$(DATADIR)/octave/5.2.0/locale/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/pege.qm $(DESTDIR)$(DATADIR)/peg-e/translations/pege_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/photivo.qm $(DESTDIR)$(DATADIR)/photivo/Translations/photivo_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/plume-creator.qm $(DESTDIR)$(DATADIR)/plume-creator/locale/plume-creator_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qantenna.qm $(DESTDIR)$(DATADIR)/qantenna/qantenna_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qaquarelle.qm $(DESTDIR)$(DATADIR)/qaquarelle/locale/$$i/qaquarelle.qm; done
	for i in ???_??; do install -Dm644 $$i/qgifer.qm $(DESTDIR)$(DATADIR)/qgifer/locale/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qgigaset.qm $(DESTDIR)$(DATADIR)/qgigaset/qgigaset_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qgo.qm $(DESTDIR)$(DATADIR)/qgo/languages/qgo_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qprogram-starter.qm $(DESTDIR)$(DATADIR)/qprogram-starter/translations/qprogram-starter-$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtqr.qm $(DESTDIR)$(DATADIR)/qr-tools/qtqr_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qshutdown.qm $(DESTDIR)$(DATADIR)/qshutdown/translations/qshutdown-$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/schatd-ui.qm $(DESTDIR)$(DATADIR)/schat/translations/schatd-ui_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/schatd.qm $(DESTDIR)$(DATADIR)/schat/translations/schatd_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/sddm.qm $(DESTDIR)$(DATADIR)/sddm/translations/$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/sigram.qm $(DESTDIR)$(DATADIR)/sigram/translations/lang-$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/skydmin.qm $(DESTDIR)$(DATADIR)/skylendar/skydmin_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/skylendar.qm $(DESTDIR)$(DATADIR)/skylendar/skylendar_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/tbe.qm $(DESTDIR)$(DATADIR)/tbe/i18n/tbe_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/qtstalker.qm $(DESTDIR)$(DATADIR)/qtstalker/i18n/qtstalker_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/videoporama.qm $(DESTDIR)$(DATADIR)/videoporama/locale/videoporama_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/wg.qm $(DESTDIR)$(DATADIR)/winegame/translations/wg_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/lwg.qm $(DESTDIR)$(DATADIR)/winestuff/l10n/lwg_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/wiznote.qm $(DESTDIR)$(DATADIR)/wiznote/locales/wiznote_$$i.qm; done
	for i in ???_??; do install -Dm644 $$i/xmodconfig.qm $(DESTDIR)$(DATADIR)/xmodconfig/xmodconfig_$$i.qm; done
