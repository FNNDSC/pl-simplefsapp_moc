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

import os
import time
# import the Chris app superclass
from chrisapp.base import ChrisApp


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

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
            [--sleepLength <sleepLength>]                               \\

            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            mkdir out && chmod 777 out
            python simplefsapp_moc.py out

    DESCRIPTION

        `simplefsapp_moc.py` is a testing/demo application for an FS-type
        application on the Massachusetts Open Cloud (MOC) remote computing
        environment.

        The application simply "touches" new files in its output directory
        which are the names of the files in the '--dir <path>' target 
        directory.

    ARGS

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number. 
        
        [--man]
        If specified, print (this) man page.

        [--meta]
        If specified, print plugin meta data.

        [--dir <path>]
        A directory on the process filesystem (if run outside ChRIS) or a 
        path inside openstorage (if run within ChRIS) to examine.

        [--sleepLength <sleepLength>]
        If specified, sleep for <sleepLength> seconds before starting
        script processing. This is to simulate a possibly long running 
        process.



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
    VERSION                 = '1.0.3'
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

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument('--dir', 
                            dest        = 'dir', 
                            type        = ChrisApp.path, 
                            default     = './',
                            optional    = True, 
                            help        = 'directory to examine')
        self.add_argument('--sleepLength',
                           dest         = 'sleepLength',
                           type         = str,
                           optional     = True,
                           help         = 'time to sleep before performing plugin action',
                           default      = '0')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % Simplefsapp_moc.VERSION)
        print('Sleeping for %s' % options.sleepLength)
        time.sleep(int(options.sleepLength))

        str_outFile = os.path.join(options.outputdir, 'out.txt')
        print(os.system('ls ' + options.dir + '>' + str_outFile))

        # Create a 'dummy' listing of empty files mirroring the target dir listing
        with open(str_outFile) as f:
            l_ls    = f.readlines()
        print(l_ls)
        l_ls = map(str.strip, l_ls)
        for str_file in l_ls:
            str_fullPath    = os.path.join(options.outputdir, str_file)
            print('touching file... %s' % str_fullPath)
            touch(str_fullPath)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    app = Simplefsapp_moc()
    app.launch()
