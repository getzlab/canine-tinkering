from .base import AbstractLocalizer
from .local import BatchedLocalizer, LocalLocalizer
from .remote import RemoteLocalizer
from .nfs import NFSLocalizer

__all__ = [
    'BatchedLocalizer',
    'LocalLocalizer',
    'RemoteLocalizer',
    'NFSLocalizer'
]

# * `CANINE`: The current canine version
# * `CANINE_BACKEND`: The name of the current backend type
# * `CANINE_ADAPTER`: The name of the current adapter type
# * `CANINE_ROOT`: The path to the staging directory
# * `CANINE_COMMON`: The path to the directory where common files are localized
# * `CANINE_OUTPUT`: The path to the directory where job outputs will be staged during delocalization
# * `CANINE_JOB_VARS`: A colon separated list of the names of all variables generated by job inputs
# * `CANINE_JOB_INPUTS`: The path to the directory where job inputs are localized
# * `CANINE_JOB_WORKSPACE`: The path to the working directory for the job. Equal to CWD at the start of the job. Output files should be written here
# * `CANINE_JOB_ROOT`: The path to the job shard staging directory

# $CANINE_ROOT: staging dir
#   /common: common inputs                              $CANINE_COMMON
#   /outputs: output dir (unused?)                      $CANINE_OUTPUT
#       /{jobID}: job specific output
#   /jobs/{jobID}: job staging dir                      $CANINE_JOB_ROOT
#       setup.sh: setup script
#       script.sh: main script
#       teardown.sh: teardown script
#       /inputs: job specific input                     $CANINE_JOB_INPUTS
#       /workspace: job starting cwd and output dir     $CANINE_JOB_WORKSPACE
