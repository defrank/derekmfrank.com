###############################################################################
# $Id: Makefile,v 1.7 2013-05-31 23:55:22-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
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
DIR_MEDIA       = ${DIR_DJANGO}media/
DIR_VIEWS       = ${DIR_DJANGO}views/
# Apps
DIR_APPS        = mysite/
DIR_UTILS       = ${DIR_APPS}utils/
DIR_TEMPLATES   = ${DIR_APPS}templates/
DIR_STATIC      = ${DIR_APPS}staticfiles/
DIR_IMG         = ${DIR_STATIC}img/
DIR_DOC         = ${DIR_STATIC}doc/
DIR_JS          = ${DIR_STATIC}js/
DIR_ICO         = ${DIR_STATIC}ico/
DIR_CSS         = ${DIR_STATIC}css/
DIR_LOGO        = ${DIR_IMG}logo/
DIR_WEBMASTER   = ${DIR_APPS}webmaster/
DIR_ABOUTME     = ${DIR_APPS}aboutme/
DIR_BLOG        = ${DIR_APPS}blog/
DIR_MFF         = ${DIR_APPS}mff/
DIR_PORTFOLIO   = ${DIR_APPS}portfolio/

## DJANGO
VIEWFILES       = ${DIR_VIEWS}views.py
DJANGOFILES     = ${DIR_APPS}manage.py          ${DIR_DJANGO}settings.py       \
                  ${DIR_DJANGO}urls.py     ${DIR_DJANGO}context_processors.py  \
				  ${DIR_DJANGO}mysite.db        ${VIEWFILES} ${TEMPLATESFILES}

## APPS
APP_UTILS       = ${DIR_UTILS}__init__.py       ${DIR_UTILS}urls.py            \
                  ${DIR_UTILS}models.py         ${DIR_UTILS}views.py           \
                  ${DIR_UTILS}functions.py 
APP_TEMPLATES   = ${DIR_TEMPLATES}__init__.py   ${DIR_TEMPLATES}urls.py        \
                  ${DIR_TEMPLATES}models.py     ${DIR_TEMPLATES}views.py       \
                  ${DIR_TEMPLATES}base.html     ${DIR_TEMPLATES}home.html
## MEDIA/STATIC
IMGFILES        = ${DIR_IMG}favicon.ico         ${DIR_IMG}favicon.gif
DOCFILES        = 
JSFILES         = 
ICOFILES        = ${DIR_ICO}favicon.ico         ${DIR_ICO}favicon.gif
LOGOFILES       = 
CSSFILES        = ${DIR_CSS}style.css           ${DIR_CSS}navbar.css
STATICFILES     = 
APP_STATIC      = ${DIR_STATIC}__init__.py      ${DIR_STATIC}urls.py           \
                  ${DIR_STATIC}models.py        ${DIR_STATIC}views.py          \
                  ${CSSFILES} ${ICONFILES} ${LOGOFILES} ${IMGFILES} ${JSFILES} \
                  ${DOCFILES}
APP_WEBMASTER   = ${DIR_WEBMASTER}__init__.py   ${DIR_WEBMASTER}urls.py        \
				  ${DIR_WEBMASTER}views.py                                     \
				  ${DIR_WEBMASTER}templates/google0a2e75908547fa0e.html        \
				  ${DIR_WEBMASTER}templates/BingSiteAuth.xml
APP_ABOUTME     = ${DIR_ABOUTME}__init__.py     ${DIR_ABOUTME}urls.py          \
				  ${DIR_ABOUTME}views.py        ${DIR_ABOUTME}models.py        \
				  ${DIR_ABOUTME}templates/aboutme.html
APP_BLOG        = ${DIR_BLOG}__init__.py        ${DIR_BLOG}urls.py             \
				  ${DIR_BLOG}views.py           ${DIR_BLOG}models.py           \
				  ${DIR_BLOG}templates/blog.html                               \
				  ${DIR_BLOG}templates/blogpost.html                           \
				  ${DIR_BLOG}templates/bloglinks.html                          \
				  ${DIR_BLOG}templates/blogsingle.html
APP_MFF         = ${DIR_MFF}__init__.py         ${DIR_MFF}urls.py              \
				  ${DIR_MFF}views.py            ${DIR_MFF}models.py            \
				  ${DIR_MFF}templates/mff.html
APP_PORTFOLIO   = ${DIR_PORTFOLIO}__init__.py   ${DIR_PORTFOLIO}urls.py        \
				  ${DIR_PORTFOLIO}views.py      ${DIR_PORTFOLIO}models.py      \
				  ${DIR_PORTFOLIO}templates/portfolio.html
APPSFILES       = ${APP_UTILS} ${APP_TEMPLATES} ${APP_STATIC} ${APP_WEBMASTER} \
				  ${APP_ABOUTME} ${APP_BLOG} ${APP_MFF} ${APP_PORTFOLIO}

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
	#rcs -U ${ALLFILES}
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
    #for i in `find . -name "__pycache__"` ; do rm -r "$i" ; done
    #for i in `find . -name "*.pyc"` ; do rm "$i" ; done

spotless : clean
