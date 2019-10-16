Name: language-pack-sinitic
Summary: Translations for some sinitic languages
Version: 2019.10
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

%prep
%setup -q

%build
make

%install
%make_install

%files
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_libdir}/R/library/translations/*/LC_MESSAGES/*.mo
%{_libdir}/textadept/core/locales/locale.*.conf
%{_datadir}/0ad/l10n/*.engine.po
%{_datadir}/FBReader/resources/*.xml
%{_datadir}/Telegram/Desktop_*.strings
%{_datadir}/locale/*/LC_MESSAGES/*.qm
%{_datadir}/*/*/*.qm
%{_libexecdir}/*/Translations/*.qm
%{_datadir}/zlibrary/resources/*.xml
%{_datadir}/childsplay_sp/*/*/words-*
%{_datadir}/*/locale/*/LC_MESSAGES/*.mo
%{_datadir}/liblunar/holiday.dat-*
%{_datadir}/logo/logolib/Messages.*
/var/www/html/clipbucket/includes/langs/*.lang
/etc/joe/joerc.*

%changelog
* Tue Oct 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2019.10
- Initial package
