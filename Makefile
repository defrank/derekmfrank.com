###############################################################################
# $Id: Makefile,v 1.1 2013-06-30 17:02:40-07 dmf - $
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
DIR_STATIC      = ${DIR_DJANGO}static/
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
DIR_ACCOUNTS    = ${DIR_APPS}accounts/
DIR_FEED        = ${DIR_APPS}feed/
DIR_PORTFOLIO   = ${DIR_APPS}portfolio/
DIR_BLOG        = ${DIR_APPS}blog/
DIR_BUSINESS    = ${DIR_APPS}business/

## TEMPLATES
TEMPLATEFILES   = ${DIR_TEMPLATES}base.html     ${DIR_TEMPLATES}home.html      \
				  ${DIR_TEMPLATES}admin/base_site.html                         \
				  ${DIR_TEMPLATES}admin/inc/userlinks.html

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
UTILS_TAGS      = ${DIR_UTILS}templatetags/
APP_UTILS       = ${DIR_UTILS}__init__.py       ${DIR_UTILS}urls.py            \
                  ${DIR_UTILS}models.py         ${DIR_UTILS}views.py           \
				  ${UTILS_TAGS}__init__.py      ${UTILS_TAGS}utils_tags.py
WEBMASTER_TEMP  = ${DIR_WEBMASTER}templates/webmaster/
APP_WEBMASTER   = ${DIR_WEBMASTER}__init__.py   ${DIR_WEBMASTER}urls.py        \
				  ${DIR_WEBMASTER}views.py                                     \
				  ${WEBMASTER_TEMP}google0a2e75908547fa0e.html                 \
				  ${WEBMASTER_TEMP}BingSiteAuth.xml
ACCOUNTS_TEMP   = ${DIR_ACCOUNTS}templates/accounts/
ACCOUNTS_TAGS   = ${DIR_ACCOUNTS}templatetags/
APP_ACCOUNTS    = ${DIR_ACCOUNTS}__init__.py    ${DIR_ACCOUNTS}urls.py         \
				  ${DIR_ACCOUNTS}views.py       ${DIR_ACCOUNTS}models.py       \
				  ${DIR_ACCOUNTS}tests.py       ${DIR_ACCOUNTS}admin.py        \
				  ${ACCOUNTS_TAGS}__init__.py                                  \
				  ${ACCOUNTS_TAGS}accounts_tags.py                             \
				  ${ACCOUNTS_TEMP}about_content.html                           \
				  ${ACCOUNTS_TEMP}source_display.html                          \
				  ${ACCOUNTS_TEMP}user.html                                    \
				  ${ACCOUNTS_TEMP}aboutme.html                                 
FEED_TEMP       = ${DIR_FEED}templates/feed/
APP_FEED        = ${DIR_FEED}__init__py         ${DIR_FEED}urls.py             \
				  ${DIR_FEED}views.py           ${DIR_FEED}models.py           \
				  ${DIR_FEED}tests.py
PORTFOLIO_TEMP  = ${DIR_PORTFOLIO}templates/portfolio/
APP_PORTFOLIO   = ${DIR_PORTFOLIO}__init__.py   ${DIR_PORTFOLIO}urls.py        \
				  ${DIR_PORTFOLIO}views.py      ${DIR_PORTFOLIO}models.py      \
				  ${DIR_PORTFOLIO}tests.py                                     \
				  ${PORTFOLIO_TEMP}portfolio.html                              \
				  ${PORTFOLIO_TEMP}sources.html                                \
				  ${PORTFOLIO_TEMP}projects.html                               \
				  ${PORTFOLIO_TEMP}education.html
BLOG_TEMP       = ${DIR_BLOG}templates/blog/
APP_BLOG        = ${DIR_BLOG}__init__.py        ${DIR_BLOG}urls.py             \
				  ${DIR_BLOG}views.py           ${DIR_BLOG}models.py           \
				  ${DIR_BLOG}tests.py                                          \
				  ${BLOG_TEMP}blog.html                                        \
				  ${BLOG_TEMP}recent.html                                      \
				  ${BLOG_TEMP}entries.html                                     \
				  ${BLOG_TEMP}entry.html                                       \
				  ${BLOG_TEMP}links.html                                       \
				  ${BLOG_TEMP}previous.html                                    \
				  ${BLOG_TEMP}index.html                                       
BUSINESS_TEMP   = ${DIR_BUSINESS}templates/business/
APP_BUSINESS    = ${DIR_BUSINESS}__init__.py    ${DIR_BUSINESS}urls.py         \
				  ${DIR_BUSINESS}views.py       ${DIR_BUSINESS}models.py       \
				  ${BUSINESS_TEMP}business.html                                \
				  ${BUSINESS_TEMP}mff.html
APPSFILES       = ${APP_UTILS}  ${APP_WEBMASTER}   ${APP_ACCOUNTS}             \
				  ${APP_FEED}   ${APP_PORTFOLIO}   ${APP_BLOG} ${APP_BUSINESS}
				  

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
all : clean save

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
	- git commit -m "First commit"
	git remote add origin git@bitbucket.org:dmfrank/${CWD}.git
	git push -u origin master

#
# Sync local and remote repositories
#
save : clean ci
	git add --all
	git status
	- git commit -a

push : save
	git status
	git push

pull :
	git status
	git pull
	git status

sync : pull push

#
# Clean and spotless remove genereated files
#
clean :
	find . -name "blah*" -exec rm -r {} + ;
	find . -name "__pycache__" -exec rm -r {} + ;
	find . -name "*.pyc" -exec rm {} + ;

spotless : clean
