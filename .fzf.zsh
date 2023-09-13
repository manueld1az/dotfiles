# Setup fzf
# ---------
if [[ ! "$PATH" == */home/manueld1az/.fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}/home/manueld1az/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/home/manueld1az/.fzf/shell/completion.zsh" 2> /dev/null

# Key bindings
# ------------
source "/home/manueld1az/.fzf/shell/key-bindings.zsh"
