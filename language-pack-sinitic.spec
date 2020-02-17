Name: language-pack-sinitic
Summary: Translations for some sinitic languages
Version: 2020.1
Release: 1
License: Open Source
Group: Translations
URL: https://github.com/chinese-opendesktop/%{name}
Source0: https://github.com/chinese-opendesktop/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: msghack
BuildRequires: translate-toolkit
BuildRequires: qt5-linguist
BuildRequires: msgchi
BuildArch: noarch

%description
Translation data for all supported packages for some sinitic languages.

%package -n language-pack-cmn
Summary: Translations for Mandarin Chinese
Requires: glibc-langpack-cmn

%description -n language-pack-cmn
Translation data for all supported packages for Mandarin Chinese.

%package -n language-pack-yue
Summary: Translations for Yue Chinese
Requires: glibc-langpack-yue

%description -n language-pack-yue
Translation data for all supported packages for Yue Chinese.

%prep
%setup -q

%build
make

%install
%make_install

%files -n language-pack-cmn
%{_datadir}/locale/cmn*/LC_MESSAGES/*.mo
%{_libdir}/R/library/translations/cmn*/LC_MESSAGES/*.mo
%{_libdir}/textadept/core/locales/locale.cmn*.conf
%{_datadir}/0ad/l10n/cmn*.engine.po
%{_datadir}/FBReader/resources/cmn*.xml
%{_datadir}/Telegram/Desktop_cmn*.strings
%{_datadir}/locale/cmn*/LC_MESSAGES/*.qm
%{_datadir}/*/*cmn*.qm
%{_datadir}/*/*/*cmn*.qm
%{_datadir}/*/*/*/*cmn*.qm
%{_libexecdir}/*/Translations/*cmn*.qm
%{_datadir}/zlibrary/resources/cmn*.xml
%{_datadir}/childsplay_sp/*/*/words-cmn*
%{_datadir}/*/*/cmn*/LC_MESSAGES/*.mo
%{_datadir}/liblunar/holiday.dat-cmn*
%{_datadir}/logo/logolib/Messages.cmn*
/var/www/html/clipbucket/includes/langs/cmn*.lang
/etc/joe/joerc.cmn*
%{python3_sitelib}/openshot_qt/language/OpenShot.cmn*.qm
%{_libdir}/libreoffice/program/resource/cmn*/LC_MESSAGES/*.mo

%files -n language-pack-yue
%{_datadir}/locale/yue*/LC_MESSAGES/*.mo
%{_libdir}/R/library/translations/yue*/LC_MESSAGES/*.mo
%{_libdir}/textadept/core/locales/locale.yue*.conf
%{_datadir}/0ad/l10n/yue*.engine.po
%{_datadir}/FBReader/resources/yue*.xml
%{_datadir}/Telegram/Desktop_yue*.strings
%{_datadir}/locale/yue*/LC_MESSAGES/*.qm
%{_datadir}/*/*yue*.qm
%{_datadir}/*/*/*yue*.qm
%{_datadir}/*/*/*/*yue*.qm
%{_libexecdir}/*/Translations/*yue*.qm
%{_datadir}/zlibrary/resources/yue*.xml
%{_datadir}/childsplay_sp/*/*/words-yue*
%{_datadir}/*/*/yue*/LC_MESSAGES/*.mo
%{_datadir}/liblunar/holiday.dat-yue*
%{_datadir}/logo/logolib/Messages.yue*
/var/www/html/clipbucket/includes/langs/yue*.lang
/etc/joe/joerc.yue*
%{python3_sitelib}/openshot_qt/language/OpenShot.yue*.qm
%{_libdir}/libreoffice/program/resource/yue*/LC_MESSAGES/*.mo

%changelog
* Thu Jan 16 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2020.1
- Initial package
