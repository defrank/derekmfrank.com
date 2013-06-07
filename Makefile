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
DIR_TEMPLATES   = ${DIR_DJANGO}templates/
DIR_STATIC      = ${DIR_DJANGO}staticfiles/
DIR_IMG         = ${DIR_STATIC}img/
DIR_DOC         = ${DIR_STATIC}doc/
DIR_JS          = ${DIR_STATIC}js/
DIR_ICO         = ${DIR_STATIC}ico/
DIR_CSS         = ${DIR_STATIC}css/
DIR_LOGO        = ${DIR_IMG}logo/
# Apps
DIR_APPS        = mysite/
DIR_UTILS       = ${DIR_APPS}utils/
DIR_WEBMASTER   = ${DIR_APPS}webmaster/
DIR_LIMN        = ${DIR_APPS}limn/
DIR_PORJECT     = ${DIR_APPS}porject/
DIR_ABOUTME     = ${DIR_APPS}aboutme/
DIR_BLOG        = ${DIR_APPS}blog/
DIR_MFF         = ${DIR_APPS}mff/

## TEMPLATES
TEMPLATEFILES   = ${DIR_TEMPLATES}base.html     ${DIR_TEMPLATES}home.html

## MEDIA/STATIC
IMGFILES        =
LOGOFILES       = 
ICOFILES        = ${DIR_ICO}favicon.ico         ${DIR_ICO}favicon.gif
JSFILES         = 
CSSFILES        = ${DIR_CSS}style.css           ${DIR_CSS}navbar.css
STATICFILES     = ${IMGFILES} ${LOGOFILES} ${ICONFILES} ${JSFILES} ${CSSFILES} 

## DJANGO
DJANGOFILES     = ${DIR_APPS}manage.py          ${DIR_DJANGO}settings.py       \
                  ${DIR_DJANGO}urls.py          ${DIR_VIEWS}views.py           \
				  ${DIR_DJANGO}context_processors.py                           \
				  ${DIR_DJANGO}mysite.db                                       \
				  ${TEMPLATEFILES} ${STATICFILES}

## APPS
APP_UTILS       = ${DIR_UTILS}__init__.py       ${DIR_UTILS}urls.py            \
                  ${DIR_UTILS}models.py         ${DIR_UTILS}views.py           \
                  ${DIR_UTILS}functions.py 
WEBMASTER_TEMP  = ${DIR_WEBMASTER}templates/webmaster/
APP_WEBMASTER   = ${DIR_WEBMASTER}__init__.py   ${DIR_WEBMASTER}urls.py        \
				  ${DIR_WEBMASTER}views.py                                     \
				  ${WEBMASTER_TEMP}google0a2e75908547fa0e.html                 \
				  ${WEBMASTER_TEMP}BingSiteAuth.xml
LIMN_TEMP       = ${DIR_LIMN}templates/limn/
APP_LIMN        = ${DIR_LIMN}__init__.py        ${DIR_LIMN}urls.py             \
				  ${DIR_LIMN}views.py          ${DIR_LIMN}models.py            \
				  ${LIMN_TEMP}about.html
PORJECT_TEMP    = ${DIR_PORJECT}templates/porject/
APP_PORJECT     = ${DIR_PORJECT}__init__.py     ${DIR_PORJECT}urls.py          \
				  ${DIR_PORJECT}views.py        ${DIR_PORJECT}models.py        \
				  ${PORJECT_TEMP}portfolio.html
ABOUTME_TEMP    = ${DIR_ABOUTME}templates/aboutme/
APP_ABOUTME     = ${DIR_ABOUTME}__init__.py     ${DIR_ABOUTME}urls.py          \
				  ${DIR_ABOUTME}views.py        ${DIR_ABOUTME}models.py        \
				  ${ABOUTME_TEMP}aboutme.html
BLOG_TEMP       = ${DIR_BLOG}templates/blog/
APP_BLOG        = ${DIR_BLOG}__init__.py        ${DIR_BLOG}urls.py             \
				  ${DIR_BLOG}views.py           ${DIR_BLOG}models.py           \
				  ${BLOG_TEMP}posts.html                                       \
				  ${BLOG_TEMP}entry.html                                       \
				  ${BLOG_TEMP}links.html                                       \
				  ${BLOG_TEMP}post_detail.html                                 \
				  ${BLOG_TEMP}index.html                                       \
				  ${BLOG_TEMP}archive/post_all.html                            \
				  ${BLOG_TEMP}archive/post_id.html                             \
				  ${BLOG_TEMP}archive/post_date.html
MFF_TEMP        = ${DIR_MFF}templates/mff/
APP_MFF         = ${DIR_MFF}__init__.py         ${DIR_MFF}urls.py              \
				  ${DIR_MFF}views.py            ${DIR_MFF}models.py            \
				  ${MFF_TEMP}mff.html
APPSFILES       = ${APP_UTILS} ${APP_WEBMASTER} ${APP_LIMN} ${APP_PORJECT}     \
				  ${APP_BLOG} ${APP_ABOUTME} ${APP_MFF} 

## MISC
SERVFILES       = .htaccess
TXT             = README
FILES           =
CHKSRC          = ${MKFILE}
CHKFILES        =

## ALL
ALLFILES        = ${MKFILE}    ${TXT}        ${SERVFILES}  ${DJANGOFILES}      \
				  ${APPSFILES}

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
