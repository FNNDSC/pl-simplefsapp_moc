#!/usr/bin/env python                                            
#                                                            _
# simplefsapp_moc fs app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import  sys
import  os

# import the Chris app superclass
from    chrisapp.base   import ChrisApp

Gstr_title = """


     _                 _       __                                             
    (_)               | |     / _|                                            
 ___ _ _ __ ___  _ __ | | ___| |_ ___  __ _ _ __  _ __   _ __ ___   ___   ___ 
/ __| | '_ ` _ \| '_ \| |/ _ \  _/ __|/ _` | '_ \| '_ \ | '_ ` _ \ / _ \ / __|
\__ \ | | | | | | |_) | |  __/ | \__ \ (_| | |_) | |_) || | | | | | (_) | (__ 
|___/_|_| |_| |_| .__/|_|\___|_| |___/\__,_| .__/| .__/ |_| |_| |_|\___/ \___|
                | |                        | |   | |______                    
                |_|                        |_|   |_|______|                   


"""

Gstr_synopsis = """

    NAME

       simplefsapp_moc.py 

    SYNOPSIS

        python simplefsapp_moc.py                                       \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            [--man]                                                     \\
            [--meta]                                                    \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            mkdir in out && chmod 777 out
            python simplefsapp_moc.py out

    DESCRIPTION

        `simplefsapp_moc.py` is a testing/demo application for an FS-type
        application on the Massachusetts Open Cloud (MOC) remote computing
        environment.

    ARGS

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number. 
        
        [--man]
        If specified, print (this) man page.

        [--meta]
        If specified, print plugin meta data.

"""

class Simplefsapp_moc(ChrisApp):
    """
    A demo/testing simplefsapp for the MOC compute environment..
    """
    AUTHORS                 = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'SimpleFSapp_moc'
    CATEGORY                = 'testing'
    TYPE                    = 'fs'
    DESCRIPTION             = 'A demo/testing simplefsapp for the MOC compute environment.'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictinary is saved when plugin is called with a ``--saveoutputmeta`` 
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}
 
    def manPage_show(self):
        """
        Print some quick help.
        """
        print(Gstr_synopsis)

    def metaData_show(self):
        """
        Print the plugin meta data
        """
        l_metaData  = dir(self)
        l_classVar  = [x for x in l_metaData if x.isupper() ]
        for str_var in l_classVar:
            str_val = getattr(self, str_var)
            print("%20s: %s" % (str_var, str_val))

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument("-v", "--verbosity",
                            help        = "verbosity level for app",
                            type        = str,
                            dest        = 'verbosity',
                            optional    = True,
                            default     = "0")
        self.add_argument('--man',
                            help        = 'if specified, print man page',
                            type        = bool,
                            dest        = 'b_man',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument('--meta',
                            help        = 'if specified, print plugin meta data',
                            type        = bool,
                            dest        = 'b_meta',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)
        self.add_argument('--version',
                            help        = 'if specified, print version number',
                            type        = bool,
                            dest        = 'b_version',
                            action      = 'store_true',
                            optional    = True,
                            default     = False)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        if options.b_man:
            self.manPage_show()
            sys.exit(0)

        if options.b_meta:
            self.metaData_show()
            sys.exit(0)

        if options.b_version:
            print('Plugin Version: %s' % Simplefsapp_moc.VERSION)
            sys.exit(0)

        print(Gstr_title)
        print('Version: %s' % Simplefsapp_moc.VERSION)

# ENTRYPOINT
if __name__ == "__main__":
    app = Simplefsapp_moc()
    app.launch()