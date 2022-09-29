# ref: gist
# https://gist.github.com/knadh/123bca5cfdae8645db750bfb49cb44b0?permalink_comment_id=3556104#gistcomment-3556104
function preexec() {
  cmd_start=$(($(print -P %D{%s%6.}) / 1000))
}

function precmd() {
  if [ $cmd_start ]; then
    local now=$(($(print -P %D{%s%6.}) / 1000))
    local d_ms=$(($now - $cmd_start))
    if [ $d_ms -ge $_jasminetea_exectime_thld_ms ]; then
        local d_s=$((d_ms / 1000))
        local ms=$((d_ms % 1000))
        local s=$((d_s % 60))
        local m=$(((d_s / 60) % 60))
        local h=$((d_s / 3600))

        if   ((h > 0)); then cmd_time=${h}h${m}m
        elif ((m > 0)); then cmd_time=${m}m${s}s
        elif ((s > 9)); then cmd_time=${s}.$(printf %03d $ms | cut -c1-2)s # 12.34s
        elif ((s > 0)); then cmd_time=${s}.$(printf %03d $ms)s # 1.234s
        else cmd_time=${ms}ms
        fi
    else
        unset cmd_time
    fi
    unset cmd_start
  else
    # Clear previous result when hitting Return with no command to execute
    unset cmd_time
  fi
}

# ------------------------------------

eval _jasminetea_prompt_prefix="$'\n'"

eval _jasminetea_char_symbol="$': '"
eval _jasminetea_char_symbol_root="$'$ '"
eval _jasminetea_char_fg_success='$FG[000]'
eval _jasminetea_char_fg_failure='$FG[009]'
eval _jasminetea_char_fg_secondary='$FG[011]'

eval _jasminetea_user_show='false'
eval _jasminetea_user_fg='$FG[003]'
eval _jasminetea_user_style="%B"

eval _jasminetea_host_show='false'
eval _jasminetea_host_fg='$FG[006]'
eval _jasminetea_host_style="%B"
eval _jasminetea_host_prefix="%Bau$' '"

eval _jasminetea_dir_show='true'
eval _jasminetea_dir_fg='$FG[015]'
eval _jasminetea_dir_style="%B"
eval _jasminetea_dir_prefix="%Bin$' '"

eval _jasminetea_time_show='true'
eval _jasminetea_time_fg='$FG[000]'
eval _jasminetea_time_style="%B"
eval _jasminetea_time_prefix=""

eval _jasminetea_exectime_show='true'
eval _jasminetea_exectime_fg='$FG[216]'
eval _jasminetea_exectime_style="%B"
eval _jasminetea_exectime_prefix=""
eval _jasminetea_exectime_thld_ms=1000

eval _jasminetea_jobs_show='true'
eval _jasminetea_jobs_fg='$FG[013]'
eval _jasminetea_jobs_style="%B"
eval _jasminetea_jobs_prefix="%B$'$BG[013]$FG[255]'B"

eval _jasminetea_conda_show='true'
eval _jasminetea_conda_fg='$FG[081]'
eval _jasminetea_conda_prefix="@"

_jasminetea_cur_username() {
    if [[ $_jasminetea_user_show == 'true' ]]; then
        echo "%{$_jasminetea_user_fg%}$_jasminetea_user_style%n$reset_color "
    fi
}

_jasminetea_cur_host() {
    if [[ $_jasminetea_host_show == 'true' ]]; then
        echo "$_jasminetea_host_prefix$_jasminetea_host_style$_jasminetea_host_fg%m$reset_color "
    fi
}

_jasminetea_cur_directory() {
    if [[ $_jasminetea_dir_show == 'true' ]]; then
        echo "$_jasminetea_dir_prefix$_jasminetea_dir_style$_jasminetea_dir_fg%3~$reset_color "
    fi
}

_jasminetea_cur_time() {
    if [[ $_jasminetea_time_show == 'true' ]]; then
        echo "$_jasminetea_time_prefix$_jasminetea_time_style$_jasminetea_time_fg%*%{$reset_color%} "
    fi
}

_jasminetea_jobs() {
    _show() {
        if [[ $_jasminetea_jobs_show == 'true' ]]; then
            echo "$_jasminetea_jobs_prefix$reset_color$_jasminetea_jobs_fg$_jasminetea_jobs_style%j$reset_color"
        fi
    }
    echo "%(1j.$(_show).)"
}

_jasminetea_exec_time() {
    if [[ $_jasminetea_exectime_show == 'true' && $cmd_time ]]; then
        echo "$_jasminetea_exectime_prefix$_jasminetea_exectime_style$_jasminetea_exectime_fg$cmd_time$reset_color "
    fi
}

_jasminetea_conda() {
    if [[ $_jasminetea_conda_show == 'true' && ! -z $CONDA_DEFAULT_ENV ]]; then
        echo "$_jasminetea_conda_prefix$_jasminetea_conda_fg$CONDA_DEFAULT_ENV$reset_color "
    fi
}

_jasminetea_char() {
    _ok() {
        echo "%{$_jasminetea_char_fg_success%}$_jasminetea_char_symbol$reset_color"
    }
    _err() {
        echo "%{$_jasminetea_char_fg_failure%}$_jasminetea_char_symbol$reset_color"
    }
    echo "%(?.$(_ok).$(_err))"
}


if [[ -n $SSH_CLIENT || -n $SSH_TTY ]]; then
    _jasminetea_user_show='true'
    _jasminetea_host_show='true'
fi

if [ -z "$TMUX" -a -z "$VSCODE_INTEGRATED_TERMINAL" ]; then
    # _jasminetea_user_show='true'
    # _jasminetea_host_show='true'
else
    _jasminetea_user_show='false'
    _jasminetea_host_show='false'
fi


PROMPT='\
$_jasminetea_prompt_prefix\
$(_jasminetea_cur_username)\
$(_jasminetea_cur_host)\
$(_jasminetea_cur_directory)\
$(_jasminetea_conda)\
$(_jasminetea_exec_time)\
$(_jasminetea_cur_time)\

$(_jasminetea_jobs)\
$(_jasminetea_char)'
