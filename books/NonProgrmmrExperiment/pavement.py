import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
from runestone.server import get_dburl
from sphinxcontrib import paverutils
import pkg_resources
from socket import gethostname
from runestone import get_master_url

sys.path.append(os.getcwd())

# The project name, for use below.
project_name = 'Subgoals'

master_url = None
if master_url is None:
    master_url = get_master_url()

dynamic_pages=True

if dynamic_pages:
    dest = './published'
else:
    dest = '../../static'

# The root directory for ``runestone serve``.
serving_dir = "./build/" + project_name
# The destination directory for ``runestone deploy``.
dest = "./published"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir=serving_dir,
        sourcedir="_sources",
        outdir=serving_dir,
        confdir=".",
        template_args={'login_required':'true',
                       'loglevel': 10,
                       'course_title': project_name,
                       'python3': 'true',
                       'dburl': 'postgresql://runestone:runestone@localhost/runestone',
                       'default_ac_lang': 'java',
                       'downloads_enabled': 'false',
                       'enable_chatcodes': 'False',
                       'allow_pairs': 'False',
                       'dynamic_pages': dynamic_pages,
                       'use_services': 'true',
                       'basecourse': project_name,
                       'course_id': project_name,
                       # These are used for non-dynamic books.
                       'appname': 'runestone',
                       'course_url': master_url,
                      }
    )
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# If DBURL is in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.
