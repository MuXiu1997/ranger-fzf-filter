# ranger-fzf-filter
This is a [`ranger`](https://github.com/ranger/ranger) plugin that adds a fuzzy filter(depends on [`fzf`](https://github.com/junegunn/fzf)), allowing for the interactive real-time display of filtered files. Unlike the built-in `find` command, which requires pressing `Enter` to execute and display filtered files, this plugin shows them instantaneously.(Translated by ChatGPT)

这是一个 [`ranger`](https://github.com/ranger/ranger) 插件，添加了一个模糊过滤器（依赖 [`fzf`](https://github.com/junegunn/fzf)），可以交互式实时过滤出显示的文件，而不是像内置的`find`命令需要输入回车执行后才过滤出显示的文件。


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


