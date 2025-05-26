# File... makefile
# Auth... Toby J. van den Herik 2025
# Desc... Make the xgui for x2 monitoring

# Version and default install directory
INSTALL_DIR ?= $(HOME)/xguiinst
XGUIS_VER_STRING ?= "1.0.1"

# Flavour
NC = '\033[0m'
Purple = '\033[0;35m'
Green = '\033[0;32m'
Gray = '\033[1;30m'
Yellow='\033[0;33m'

# Programs
uninstall:
	make remove

remove:
	rm -r $(INSTALL_DIR)
	@echo "XGUI removed / uninstalled."

installprocess:
	@echo "--------------------------------------------------------\nInstalling xgui..."
	@echo "Placing package in $(INSTALL_DIR)..."

	@mkdir -p $(INSTALL_DIR)/lib/
	@mkdir -p $(INSTALL_DIR)/share/
	
	@cp xgui.py $(INSTALL_DIR)/lib/
	
	@cp xgui.py $(INSTALL_DIR)/lib/xgui; chmod +x $(INSTALL_DIR)/lib/xgui

	@mkdir -p $(INSTALL_DIR)/lib/xgui_func

	@cp ./xgui_func/*.py $(INSTALL_DIR)/lib/xgui_func

	@echo -n -e ${Purple} 
	@echo "X G U I - XLABS GUI FOR X2 FACILITY"

	@echo --- Version ${Green}"$(xgui_VER_STRING)"${NC} - See the docs for information ---

	@echo
	@echo -e ${Yellow} Attention: ${NC}in your .bashrc or .bash_aliases file put..
	@echo -n -e ${Gray}
	@echo  " export XGUI=$$ \bHOME/xguiinst"
	@echo  " export PATH=$$ \bPATH:$$ \b{XGUI}/lib"
	@echo  " export PYTHONPATH=$$ \b{PYTHONPATH}:$$ \b{XGUI}/lib"
	
	@echo -n -e ${NC}
	@echo "--------------------------------------------------------\n"
	@echo "--- xgui now installed. --- \n"
	
install:
	@echo -n "\nRemove/replace existing installation of xgui (if any)? [Y/n]: " && read ans && if [ $${ans:-'Y'} = 'n' ]; then \
		echo "Stopping as user does not wish to replace existing installation." \
        exit 1; \
    else \
		make installprocess; \
    fi