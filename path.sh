export KALDI_ROOT=/home1/trung/kaldi
export SRILM=/home1/trung/srilm/bin/i686-m64:/home1/trung/srilm/bin
export SWD_PATH=/data3/pums/Switchboard1

# export KALDI_ROOT=/Users/trungnt13/libs/kaldi
# export SRILM=/Users/trungnt13/libs/srilm/bin:/Users/trungnt13/libs/srilm/bin/macosx
# export SWD_PATH=/Volumes/backup/data/Switchboard/Switchboard-1

export ADDITION_TOOLS=$KALDI_ROOT/src/bin:$KALDI_ROOT/src/lmbin:$KALDI_ROOT/src/fstbin:$KALDI_ROOT/src/featbin

export PATH=$FSTBIN:$SRILM:$ADDITION_TOOLS:$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH

[ ! -f $KALDI_ROOT/tools/config/common_path.sh ] && echo >&2 "The standard file $KALDI_ROOT/tools/config/common_path.sh is not present -> Exit!" && exit 1
. $KALDI_ROOT/tools/config/common_path.sh

export LC_ALL=C
