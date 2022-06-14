# ranger-fzf-filter
This is a plugin for [`ranger`](https://github.com/ranger/ranger) that add a fuzzy filter.  It depends on [`fzf`](https://github.com/junegunn/fzf)

https://user-images.githubusercontent.com/49554020/173509108-dc3edca4-8949-4026-a3ca-0ba8dac9bbce.mp4


## Install

For ranger >= 1.9.3, use Git to clone this repository into your `~/.config/ranger/plugins` folder. For example:

```sh
git clone git@github.com:MuXiu1997/ranger-fzf-filter.git ~/.config/ranger/plugins/ranger_fzf_filter
```

**Legacy Install**

For ranger versions older than 1.9.3, or to install without Git, download `__init__.py` to your `~/.config/ranger/plugins` directory. For example:

```shell
mkdir -p ~/.config/ranger/plugins
wget -O ~/.config/ranger/plugins/ranger_fzf_filter.py https://raw.githubusercontent.com/MuXiu1997/ranger-fzf-filter/main/__init__.py
```



## Usage

Command:

- `:fzf_filter [query]`: filtering files with fzf, see this [search syntax](https://github.com/junegunn/fzf#search-syntax)



## Keyboard Shortcut

Add a binding to your `~/.config/ranger/rc.conf` file to quickly use `:fzf_filter`:

```
map f console fzf_filter%space
```



## License

[MIT](LICENSE)

