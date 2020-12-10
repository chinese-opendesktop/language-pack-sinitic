VERSION = 2020.12
PACKAGE = language-pack-sinitic
DESTDIR =
PREFIX = /usr
DATADIR = $(PREFIX)/share
LBITS := $(shell getconf LONG_BIT)
ifeq ($(LBITS), 64)
  LIBDIR = $(PREFIX)/lib64
else
  LIBDIR = $(PREFIX)/lib
endif
export

build:
	make -C pot build
	make -C ts build
	make -C text build

install:
	make -C pot install
	make -C ts install
	make -C text install

rpm: $(PACKAGE).spec
	rsync -aC --delete . $(HOME)/rpmbuild/SOURCES/$(PACKAGE)-$(VERSION)
	tar czf $(HOME)/rpmbuild/SOURCES/$(PACKAGE)-$(VERSION).tar.gz -C $(HOME)/rpmbuild/SOURCES $(PACKAGE)-$(VERSION)
	rpmbuild -ta $(HOME)/rpmbuild/SOURCES/$(PACKAGE)-$(VERSION).tar.gz
