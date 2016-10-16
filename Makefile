BIN = /usr/bin
SYSTEMD = /lib/systemd/system

all:
	@echo "Run 'make install'  as super user (or using sudo) to install the script"
	@echo "Run 'make uninstall' as super user (or using sudo) to uninstall the script"

install:
	[ -d ${BIN} ] && cp fnauth.py ${BIN}/
	[ -d ${SYSTEMD} ] && cp fnauth.service ${SYSTEMD}/

uninstall:
	[ -f ${BIN}/fnauth.py ] && rm  ${BIN}/fnauth.py
	[ -f ${SYSTEMD}/fnauth.service ] && rm  ${SYSTEMD}/fnauth.service

.PHONY: all
