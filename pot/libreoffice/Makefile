# https://dev-www.libreoffice.org/l10n/latest-pot/ 

build:
	for i in `find . -name messages.pot`; do msgchi $$i -l eng2cmn -a "~" -F -o $${i%.pot}.cmn_TW.po; done
	for i in `find . -name messages.cmn_TW.po`; do msgfmt $$i -o $${i%.po}.mo; done
	for i in `find . -name messages.cmn_TW.po`; do msgchi $$i -l cmn2yue -o $${i%.cmn_TW.po}.yue_HK.po; done
	for i in `find . -name messages.yue_HK.po`; do msgfmt $$i -o $${i%.po}.mo; done

install:
	for i in cmn_TW yue_HK; do install -Dm644 accessibility/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/acc.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 avmedia/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/avmedia.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 basctl/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/basctl.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 basic/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sb.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 chart2/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/chart.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 connectivity/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/cnr.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 cui/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/cui.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 dbaccess/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/dba.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 desktop/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/dkt.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 editeng/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/editeng.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 extensions/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/pcr.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 filter/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/flt.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 forms/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/frm.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 formula/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/for.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 fpicker/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/fps.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 framework/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/fwk.mo; done
#	for i in cmn_TW yue_HK; do install -Dm644 oox/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 reportdesign/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/rpt.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 scaddins/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sca.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 sccomp/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/scc.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 sc/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sc.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 sd/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sd.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 sfx2/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sfx.mo; done
#	for i in cmn_TW yue_HK; do install -Dm644 shell/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 starmath/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sm.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 svl/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/svl.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 svtools/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/svt.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 svx/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/svx.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 sw/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/sw.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 uui/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/uui.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 vcl/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/vcl.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 wizards/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/wiz.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 writerperfect/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/wpt.mo; done
	for i in cmn_TW yue_HK; do install -Dm644 xmlsecurity/messages.$$i.mo $(DESTDIR)$(LIBDIR)/libreoffice/program/resource/$$i/LC_MESSAGES/xsc.mo; done
