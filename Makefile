###############################################################################
# $Id: Makefile,v 1.1 2013-04-11 22:19:33-07 dmfrank - $
# Derek Frank (dmfrank@greenghoti.com)
#
# NAME
#   Makefile
#
# DESCRIPTION
#   A common Makefile
#
###############################################################################

MKFILE          = Makefile
WHOAMI         ?= $(shell whoami)
PWD             = $(shell pwd)
CWD             = $(shell basename ${PWD})
#
# Define the "ci" command with respect to the current user.
# dmfrank, derekmfrank, dmf, ghoti, fain are all aliases.
#
CICMD           = ci
ifeq (${WHOAMI},dmf)
CICMD           = cil
endif

#
# Define checksource
#
CHK80           = checksource -l 80

#
# Variables
#

## DIRECTORIES
DIR_DJANGO      = mysite/mysite/
DIR_MEDIA       = public/media/
DIR_STATIC      = ${DIR_DJANGO}static/
DIR_IMG         = ${DIR_STATIC}img/
DIR_JS          = ${DIR_STATIC}js/
DIR_ICO         = ${DIR_STATIC}ico/
DIR_LOGO        = ${DIR_STATIC}css/navbar/
DIR_CSS         = ${DIR_STATIC}css/
DIR_VIEWS       = ${DIR_DJANGO}views/
DIR_HTML        = ${DIR_DJANGO}templates/
DIR_APPS        = mysite/
DIR_WEBMASTER   = mysite/

## MEDIA/STATIC
IMGFILES        = ${DIR_IMG}favicon.ico         ${DIR_IMG}favicon.gif          \
                  ${DIR_IMG}searchbutton3.xcf   ${DIR_IMG}searchbutton3.png
JSFILES         = 
ICOFILES        = ${DIR_ICO}favicon.ico         ${DIR_ICO}favicon.gif
LOGOFILES       = 
CSSFILES        = ${DIR_CSS}style.css           ${DIR_CSS}navbar/navbar.css
STATICFILES     = ${CSSFILES} ${ICONFILES} ${LOGOFILES} ${IMGFILES} ${JSFILES}

## DJANGO
HTMLFILES       = ${DIR_HTML}base.html          ${DIR_HTML}home.html           \
                  ${DIR_HTML}blog.html          ${DIR_HTML}portfolio.html      \
                  ${DIR_HTML}aboutme.html       ${DIR_HTML}mff.html
VIEWFILES       = ${DIR_VIEWS}view_functions.py ${DIR_VIEWS}views.py
DJANGOFILES     = mysite/manage.py              ${DIR_DJANGO}settings.py       \
                  ${DIR_DJANGO}urls.py     ${DIR_DJANGO}context_processors.py  \
				  ${VIEWFILES} ${HTMLFILES}

## APPS
APP_WEBMASTER   = ${DIR_WEBMASTER}__init__.py   ${DIR_WEBMASTER}urls.py        \
				  ${DIR_WEBMASTER}views.py                                     \
				  ${DIR_WEBMASTER}templates/google0a2e75908547fa0e.html        \
				  ${DIR_WEBMASTER}templates/.BingSiteAuth.xml
APPSFILES       = ${APP_WEBMASTER}

## MISC
SERVFILES       = .htaccess
TXT             = README
FILES           =
CHKSRC          = ${MKFILE}
CHKFILES        =

## ALL
ALLFILES        = ${MKFILE}    ${TXT}        ${SERVFILES}  ${DJANGOFILES}      \
				  ${STATICFILES}             ${APPSFILES}

#
# make all
#
all : clean sync

#
# Run checksource on the files
#
check : ${CHKSRC}
	- ${CHK80} ${CHKSRC}

#
# Check files into an RCS subdirectory
#
ci :
ifeq (${WHOAMI},dmf)
	${CICMD} + ${ALLFILES}
endif

#
# Initialize git repository
#
gitinit :
	touch README
	git init
	git add README Makefile
	git commit -m "First commit"
	git remote add origin git@bitbucket.org:dmfrank/${CWD}.git
	git push -u origin master

#
# Sync local and remote repositories
#
sync : ci
	git add --all
	git commit -a
	git status
	git push
#	git pull

#
# Clean and spotless remove genereated files
#
clean :
	- rm blah

spotless : clean
