export PATH=/cvmfs/cms.cern.ch/common:/cvmfs/cms.cern.ch/bin:$PATH

here=/cvmfs/cms.cern.ch

if [ "$VO_CMS_SW_DIR" != ""  ] 
then
    here=$VO_CMS_SW_DIR
else
    if [ ! "X$OSG_APP" = "X" ] && [ -d "$OSG_APP/cmssoft/cms" ]; then
        here="$OSG_APP/cmssoft/cms"
    fi
fi

if [ ! $SCRAM_ARCH ]
then
    SCRAM_ARCH=`/cvmfs/cms.cern.ch/common/cmsarch`
    if [ ! -d $here/${SCRAM_ARCH}/etc/profile.d ]
    then
      SCRAM_ARCH=slc6_amd64_gcc530
    fi
    export SCRAM_ARCH
fi

if [ -d $here/${SCRAM_ARCH}/etc/profile.d ]
then
  for pkg in `/bin/ls $here/${SCRAM_ARCH}/etc/profile.d/ | grep 'S.*[.]sh'`
  do
	source $here/${SCRAM_ARCH}/etc/profile.d/$pkg
  done
fi

if [ ! $CMS_PATH ]
then
    export CMS_PATH=$here
fi

# aliases
alias cmsenv='eval `scramv1 runtime -sh`'
alias cmsrel='scramv1 project CMSSW'

if [ -f $CMS_PATH/SITECONF/local/JobConfig/cmsset_local.sh ]; then
        . $CMS_PATH/SITECONF/local/JobConfig/cmsset_local.sh
fi

if [ ! $CVSROOT ]
then
    CVSROOT=:gserver:cmssw.cvs.cern.ch:/local/reps/CMSSW
    export CVSROOT
fi

MANPATH=${CMS_PATH}/share/man:${MANPATH}
export MANPATH

